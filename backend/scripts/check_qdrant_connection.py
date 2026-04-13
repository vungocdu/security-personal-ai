from __future__ import annotations

from app.qdrant import QdrantConfigError, build_qdrant_client


def main() -> int:
    try:
        client = build_qdrant_client()
    except QdrantConfigError as exc:
        print(f"CONFIG_ERROR: {exc}")
        return 2

    try:
        collections = client.get_collections()
    except Exception as exc:  # pragma: no cover - network surface
        print(f"CONNECTION_ERROR: {exc.__class__.__name__}: {exc}")
        return 3

    names = [item.name for item in collections.collections]
    print(f"collection_count={len(names)}")
    print(f"collections={names}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
