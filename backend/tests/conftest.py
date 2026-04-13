from __future__ import annotations

import os


# Tests import the FastAPI app at module import time, so any env-driven app
# middleware (CORS, etc.) must be configured before importing `app.main`.
os.environ.setdefault("CORS_ALLOW_ORIGIN_REGEX", r"^https://.*$")

