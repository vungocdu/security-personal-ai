from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class AppConfig:
    qdrant_url: str | None
    qdrant_api_key: str | None
    qdrant_timeout_seconds: float


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
    )
