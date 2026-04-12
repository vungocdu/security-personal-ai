from __future__ import annotations

from io import BytesIO

from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_healthcheck() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


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
    )
    assert response.status_code == 200
    payload = response.json()
    assert payload["answer"]["insufficient_evidence"] is False
    assert len(payload["citations"]) == 2
    assert payload["debug"]["retrieval_strategy"] == "dense+sparse+metadata+rerank"


def test_query_validation_error_uses_error_envelope() -> None:
    response = client.post("/api/v1/query", json={"query": ""})
    assert response.status_code == 422
    payload = response.json()
    assert payload["error"]["code"] == "validation_error"
    assert payload["error"]["details"]


def test_search_response_contains_union_results() -> None:
    response = client.post(
        "/api/v1/search",
        json={"query": "covenant", "filters": {"ticker": ["SSI"]}, "page": 1, "limit": 10},
    )
    assert response.status_code == 200
    payload = response.json()
    assert payload["total"] >= 1
    assert payload["results"][0]["preview_url"]
    assert payload["results"][0]["result_type"] in {"chunk", "document"}


def test_document_list_and_versions_support_workspace_tree() -> None:
    response = client.get("/api/v1/documents", params={"page": 1, "limit": 20})
    assert response.status_code == 200
    payload = response.json()
    assert payload["data"][0]["current_version_id"]
    assert payload["data"][0]["index_status"] in {"accepted", "indexing", "indexed", "failed", "superseded"}

    document_id = payload["data"][1]["document_id"]
    versions_response = client.get(f"/api/v1/documents/{document_id}/versions")
    assert versions_response.status_code == 200
    versions = versions_response.json()["data"]
    assert any(item["is_current_version"] for item in versions)
    assert any(item["parse_status"] == "superseded" for item in versions)


def test_document_upload_returns_accepted_payload() -> None:
    response = client.post(
        "/api/v1/documents",
        files={"file": ("new-note.pdf", BytesIO(b"fake-pdf"), "application/pdf")},
        data={"document_type": "internal_note", "ticker": "VNM", "company_name": "VNM Note"},
    )
    assert response.status_code == 202
    payload = response.json()
    assert payload["status"] == "accepted"
    assert payload["document_version_id"].startswith("docver_")


def test_document_upload_with_document_id_appends_new_version() -> None:
    before = client.get("/api/v1/documents/doc_hpg_ar_2024")
    assert before.status_code == 200
    previous_current_version = before.json()["current_version_id"]

    response = client.post(
        "/api/v1/documents",
        files={"file": ("hpg-ar-amended.pdf", BytesIO(b"fake-pdf"), "application/pdf")},
        data={"document_id": "doc_hpg_ar_2024", "publication_date": "2025-04-01"},
    )
    assert response.status_code == 202
    payload = response.json()
    assert payload["document_id"] == "doc_hpg_ar_2024"
    assert payload["document_version_id"] != previous_current_version

    versions_response = client.get("/api/v1/documents/doc_hpg_ar_2024/versions")
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
    )
    assert response.status_code == 404
    payload = response.json()
    assert payload["error"]["code"] == "document_not_found"


def test_citation_and_preview_endpoints_support_evidence_panel() -> None:
    citation = client.get("/api/v1/citations/cit_hpg_risk_001")
    assert citation.status_code == 200
    citation_payload = citation.json()
    assert citation_payload["viewer_anchor"].startswith("page=")

    preview = client.get(
        f"/api/v1/documents/{citation_payload['document_id']}/versions/{citation_payload['document_version_id']}/preview/{citation_payload['page_number']}"
    )
    assert preview.status_code == 200
    preview_payload = preview.json()
    assert preview_payload["preview_url"].startswith("https://signed.example.com")


def test_preview_returns_not_ready_for_non_indexed_version() -> None:
    response = client.get("/api/v1/documents/doc_fpt_fin_2024q4/versions/docver_fpt_fin_2024q4_v1/preview/3")
    assert response.status_code == 409
    payload = response.json()
    assert payload["error"]["code"] == "preview_not_ready"


def test_missing_document_returns_not_found_envelope() -> None:
    response = client.get("/api/v1/documents/doc_missing")
    assert response.status_code == 404
    payload = response.json()
    assert payload["error"]["code"] == "document_not_found"
