from __future__ import annotations

from qdrant_client import QdrantClient

from app.config import AppConfig, load_config


class QdrantConfigError(RuntimeError):
    pass


def build_qdrant_client(config: AppConfig | None = None) -> QdrantClient:
    settings = config or load_config()
    missing_fields = []
    if not settings.qdrant_url:
        missing_fields.append("QDRANT_URL")
    if not settings.qdrant_api_key:
        missing_fields.append("QDRANT_API_KEY")
    if missing_fields:
        fields = ", ".join(missing_fields)
        raise QdrantConfigError(f"Missing required environment variables: {fields}")

    return QdrantClient(
        url=settings.qdrant_url,
        api_key=settings.qdrant_api_key,
        timeout=settings.qdrant_timeout_seconds,
    )
