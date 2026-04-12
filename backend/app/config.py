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

    return AppConfig(
        qdrant_url=(os.getenv("QDRANT_URL") or "").strip() or None,
        qdrant_api_key=(os.getenv("QDRANT_API_KEY") or "").strip() or None,
        qdrant_timeout_seconds=timeout,
        auth_enforce=_as_bool(os.getenv("AUTH_ENFORCE"), default=True),
        firebase_project_id=(os.getenv("FIREBASE_PROJECT_ID") or "").strip() or None,
        firebase_service_account_json=(os.getenv("FIREBASE_SERVICE_ACCOUNT_JSON") or "").strip() or None,
        firebase_service_account_path=(os.getenv("FIREBASE_SERVICE_ACCOUNT_PATH") or "").strip() or None,
    )
