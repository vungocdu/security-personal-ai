from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class AppConfig:
    qdrant_url: str | None
    qdrant_api_key: str | None
    qdrant_timeout_seconds: float
    auth_enforce: bool
    firebase_project_id: str | None
    firebase_service_account_json: str | None
    firebase_service_account_path: str | None
    firebase_storage_bucket: str | None
    preview_url_ttl_minutes: int
    cors_allow_origins: list[str]
    cors_allow_origin_regex: str | None


def _as_bool(raw: str | None, *, default: bool) -> bool:
    if raw is None:
        return default
    return raw.strip().lower() in {"1", "true", "yes", "y", "on"}


def load_config() -> AppConfig:
    timeout_raw = (os.getenv("QDRANT_TIMEOUT_SECONDS") or "10").strip()
    try:
        timeout = float(timeout_raw)
    except ValueError:
        timeout = 10.0
    if timeout <= 0:
        timeout = 10.0

    preview_ttl_raw = (os.getenv("PREVIEW_URL_TTL_MINUTES") or "15").strip()
    try:
        preview_ttl_minutes = int(preview_ttl_raw)
    except ValueError:
        preview_ttl_minutes = 15
    if preview_ttl_minutes <= 0:
        preview_ttl_minutes = 15

    cors_allow_origins_raw = (os.getenv("CORS_ALLOW_ORIGINS") or "").strip()
    cors_allow_origins = [item.strip() for item in cors_allow_origins_raw.split(",") if item.strip()]
    cors_allow_origin_regex = (os.getenv("CORS_ALLOW_ORIGIN_REGEX") or "").strip() or None

    return AppConfig(
        qdrant_url=(os.getenv("QDRANT_URL") or "").strip() or None,
        qdrant_api_key=(os.getenv("QDRANT_API_KEY") or "").strip() or None,
        qdrant_timeout_seconds=timeout,
        auth_enforce=_as_bool(os.getenv("AUTH_ENFORCE"), default=True),
        firebase_project_id=(os.getenv("FIREBASE_PROJECT_ID") or "").strip() or None,
        firebase_service_account_json=(os.getenv("FIREBASE_SERVICE_ACCOUNT_JSON") or "").strip() or None,
        firebase_service_account_path=(os.getenv("FIREBASE_SERVICE_ACCOUNT_PATH") or "").strip() or None,
        firebase_storage_bucket=(os.getenv("FIREBASE_STORAGE_BUCKET") or "").strip() or None,
        preview_url_ttl_minutes=preview_ttl_minutes,
        cors_allow_origins=cors_allow_origins,
        cors_allow_origin_regex=cors_allow_origin_regex,
    )
