from __future__ import annotations

from io import BytesIO

import pytest
from fastapi.testclient import TestClient

import app.auth as auth_module
import app.services as services_module
from app.main import app


client = TestClient(app)
AUTH_HEADERS = {"Authorization": "Bearer valid-test-token"}


@pytest.fixture(autouse=True)
def patch_firebase_auth(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("AUTH_ENFORCE", "true")

    def fake_verify(token: str, config=None):  # noqa: ANN001
        if token == "valid-test-token":
            return auth_module.AuthenticatedUser(
                uid="uid_analyst_001",
                email="analyst@actiwell.co",
                name="Analyst",
            )
        return None

    monkeypatch.setattr(auth_module, "verify_firebase_token", fake_verify)
    monkeypatch.setattr(services_module, "store_uploaded_source", lambda **kwargs: None)


def test_healthcheck() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_cors_preflight_allows_browser_frontend_origin() -> None:
    origin = "https://frontend.example.com"
    response = client.options(
        "/api/v1/documents",
        headers={
            "Origin": origin,
            "Access-Control-Request-Method": "POST",
            "Access-Control-Request-Headers": "authorization,content-type",
        },
    )
    assert response.status_code == 200
    assert response.headers["access-control-allow-origin"] == origin
    assert "access-control-allow-methods" in response.headers


def test_dependency_healthcheck_degraded_without_qdrant_env() -> None:
    response = client.get("/health/dependencies")
    assert response.status_code == 503
    payload = response.json()
    assert payload["status"] == "degraded"
    assert payload["qdrant"]["configured"] is False


def test_query_response_contains_citations_and_debug() -> None:
    response = client.post(
        "/api/v1/query",
        json={
            "query": "Rui ro lon nhat cua HPG trong 2024 la gi?",
            "filters": {"ticker": ["HPG"], "document_type": ["annual_report"]},
            "options": {"include_debug": True, "max_citations": 2},
        },
        headers=AUTH_HEADERS,
    )
    assert response.status_code == 200
    payload = response.json()
    assert payload["answer"]["insufficient_evidence"] is False
    assert len(payload["citations"]) == 2
    assert payload["debug"]["retrieval_strategy"] == "dense+sparse+metadata+rerank"


def test_query_validation_error_uses_error_envelope() -> None:
    response = client.post("/api/v1/query", json={"query": ""}, headers=AUTH_HEADERS)
    assert response.status_code == 422
    payload = response.json()
    assert payload["error"]["code"] == "validation_error"
    assert payload["error"]["details"]


def test_search_response_contains_union_results() -> None:
    response = client.post(
        "/api/v1/search",
        json={"query": "covenant", "filters": {"ticker": ["SSI"]}, "page": 1, "limit": 10},
        headers=AUTH_HEADERS,
    )
    assert response.status_code == 200
    payload = response.json()
    assert payload["total"] >= 1
    assert payload["results"][0]["preview_url"]
    assert payload["results"][0]["result_type"] in {"chunk", "document"}


def test_document_list_and_versions_support_workspace_tree() -> None:
    response = client.get("/api/v1/documents", params={"page": 1, "limit": 20}, headers=AUTH_HEADERS)
    assert response.status_code == 200
    payload = response.json()
    assert payload["data"][0]["current_version_id"]
    assert payload["data"][0]["index_status"] in {"accepted", "indexing", "indexed", "failed", "superseded"}

    document_id = payload["data"][1]["document_id"]
    versions_response = client.get(f"/api/v1/documents/{document_id}/versions", headers=AUTH_HEADERS)
    assert versions_response.status_code == 200
    versions = versions_response.json()["data"]
    assert any(item["is_current_version"] for item in versions)
    assert any(item["parse_status"] == "superseded" for item in versions)


def test_document_upload_returns_accepted_payload() -> None:
    response = client.post(
        "/api/v1/documents",
        files={"file": ("new-note.pdf", BytesIO(b"fake-pdf"), "application/pdf")},
        data={"document_type": "internal_note", "ticker": "VNM", "company_name": "VNM Note"},
        headers=AUTH_HEADERS,
    )
    assert response.status_code == 202
    payload = response.json()
    assert payload["status"] == "accepted"
    assert payload["document_version_id"].startswith("docver_")


def test_document_upload_with_document_id_appends_new_version() -> None:
    before = client.get("/api/v1/documents/doc_hpg_ar_2024", headers=AUTH_HEADERS)
    assert before.status_code == 200
    previous_current_version = before.json()["current_version_id"]

    response = client.post(
        "/api/v1/documents",
        files={"file": ("hpg-ar-amended.pdf", BytesIO(b"fake-pdf"), "application/pdf")},
        data={"document_id": "doc_hpg_ar_2024", "publication_date": "2025-04-01"},
        headers=AUTH_HEADERS,
    )
    assert response.status_code == 202
    payload = response.json()
    assert payload["document_id"] == "doc_hpg_ar_2024"
    assert payload["document_version_id"] != previous_current_version

    versions_response = client.get("/api/v1/documents/doc_hpg_ar_2024/versions", headers=AUTH_HEADERS)
    assert versions_response.status_code == 200
    versions = versions_response.json()["data"]
    latest = next(item for item in versions if item["is_current_version"] is True)
    superseded = next(item for item in versions if item["document_version_id"] == previous_current_version)
    assert latest["document_version_id"] == payload["document_version_id"]
    assert latest["parse_status"] == "accepted"
    assert superseded["parse_status"] == "superseded"


def test_document_upload_with_unknown_document_id_returns_not_found() -> None:
    response = client.post(
        "/api/v1/documents",
        files={"file": ("missing-target.pdf", BytesIO(b"fake-pdf"), "application/pdf")},
        data={"document_id": "doc_missing"},
        headers=AUTH_HEADERS,
    )
    assert response.status_code == 404
    payload = response.json()
    assert payload["error"]["code"] == "document_not_found"


def test_citation_and_preview_endpoints_support_evidence_panel() -> None:
    citation = client.get("/api/v1/citations/cit_hpg_risk_001", headers=AUTH_HEADERS)
    assert citation.status_code == 200
    citation_payload = citation.json()
    assert citation_payload["viewer_anchor"].startswith("page=")

    preview = client.get(
        f"/api/v1/documents/{citation_payload['document_id']}/versions/{citation_payload['document_version_id']}/preview/{citation_payload['page_number']}",
        headers=AUTH_HEADERS,
    )
    assert preview.status_code == 200
    preview_payload = preview.json()
    assert preview_payload["preview_url"].startswith("https://signed.example.com")


def test_preview_returns_not_ready_for_non_indexed_version() -> None:
    response = client.get(
        "/api/v1/documents/doc_fpt_fin_2024q4/versions/docver_fpt_fin_2024q4_v1/preview/3",
        headers=AUTH_HEADERS,
    )
    assert response.status_code == 409
    payload = response.json()
    assert payload["error"]["code"] == "preview_not_ready"


def test_missing_document_returns_not_found_envelope() -> None:
    response = client.get("/api/v1/documents/doc_missing", headers=AUTH_HEADERS)
    assert response.status_code == 404
    payload = response.json()
    assert payload["error"]["code"] == "document_not_found"


def test_query_requires_authentication() -> None:
    response = client.post("/api/v1/query", json={"query": "Missing token"})
    assert response.status_code == 401
    payload = response.json()
    assert payload["error"]["code"] == "auth_missing_token"


def test_auth_me_returns_verified_firebase_principal() -> None:
    response = client.get("/api/v1/auth/me", headers=AUTH_HEADERS)
    assert response.status_code == 200
    payload = response.json()
    assert payload["uid"] == "uid_analyst_001"
    assert payload["email"] == "analyst@actiwell.co"
