from __future__ import annotations

import os
import time

from qdrant_client import models

from app.qdrant import QdrantConfigError, build_qdrant_client


def _as_bool(raw: str | None, *, default: bool = False) -> bool:
    if raw is None:
        return default
    return raw.strip().lower() in {"1", "true", "yes", "y", "on"}


def _score_of(point: object) -> float | None:
    score = getattr(point, "score", None)
    return float(score) if isinstance(score, (int, float)) else None


def _payload_of(point: object) -> dict[str, object]:
    payload = getattr(point, "payload", None)
    return payload if isinstance(payload, dict) else {}


def main() -> int:
    try:
        client = build_qdrant_client()
    except QdrantConfigError as exc:
        print(f"CONFIG_ERROR: {exc}")
        return 2

    vector_size_raw = os.getenv("QDRANT_TEST_VECTOR_SIZE", "4").strip()
    try:
        vector_size = int(vector_size_raw)
    except ValueError:
        print(f"CONFIG_ERROR: Invalid QDRANT_TEST_VECTOR_SIZE '{vector_size_raw}'")
        return 2
    if vector_size <= 0:
        print("CONFIG_ERROR: QDRANT_TEST_VECTOR_SIZE must be > 0")
        return 2

    keep_collection = _as_bool(os.getenv("QDRANT_TEST_KEEP_COLLECTION"), default=False)
    collection_name = (os.getenv("QDRANT_TEST_COLLECTION") or f"spai_smoke_{int(time.time())}").strip()
    if not collection_name:
        print("CONFIG_ERROR: QDRANT_TEST_COLLECTION must not be empty when provided")
        return 2

    print(f"collection_name={collection_name}")
    print(f"keep_collection={keep_collection}")

    if client.collection_exists(collection_name=collection_name):
        client.delete_collection(collection_name=collection_name, timeout=30)

    client.create_collection(
        collection_name=collection_name,
        vectors_config=models.VectorParams(size=vector_size, distance=models.Distance.COSINE),
        timeout=30,
    )

    seed_points = [
        models.PointStruct(
            id=1,
            vector=[0.91, 0.12, 0.02, 0.01][:vector_size],
            payload={"ticker": "HPG", "document_id": "doc_hpg_ar_2024", "section": "Risk Factors"},
        ),
        models.PointStruct(
            id=2,
            vector=[0.22, 0.81, 0.04, 0.11][:vector_size],
            payload={"ticker": "SSI", "document_id": "doc_ssi_research_2024q4", "section": "Balance Sheet"},
        ),
        models.PointStruct(
            id=3,
            vector=[0.18, 0.05, 0.87, 0.26][:vector_size],
            payload={"ticker": "FPT", "document_id": "doc_fpt_fin_2024q4", "section": "Financial Metrics"},
        ),
    ]
    if vector_size != 4:
        print("CONFIG_ERROR: This smoke script currently expects vector size 4 for sample data.")
        return 2

    client.upsert(collection_name=collection_name, points=seed_points, wait=True, timeout=30)

    query_vector = [0.88, 0.1, 0.03, 0.0]
    query_response = client.query_points(
        collection_name=collection_name,
        query=query_vector,
        limit=3,
        with_payload=True,
        timeout=30,
    )
    points = query_response.points

    print(f"search_result_count={len(points)}")
    for idx, point in enumerate(points, start=1):
        payload = _payload_of(point)
        print(
            f"result_{idx}=id:{getattr(point, 'id', '?')},"
            f"score:{_score_of(point)},"
            f"ticker:{payload.get('ticker')},"
            f"document_id:{payload.get('document_id')}"
        )

    if not points:
        print("ASSERTION_FAILED: query returned zero results")
        return 4

    top_payload = _payload_of(points[0])
    if top_payload.get("ticker") != "HPG":
        print(f"ASSERTION_FAILED: expected top result ticker HPG, got {top_payload.get('ticker')}")
        return 4

    print("E2E_OK: insert + search verification passed")

    if not keep_collection:
        client.delete_collection(collection_name=collection_name, timeout=30)
        print("cleanup=deleted_test_collection")
    else:
        print("cleanup=kept_test_collection")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
