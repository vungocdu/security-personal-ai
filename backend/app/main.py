from __future__ import annotations

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.config import load_config
from app.errors import install_error_handlers
from app.qdrant import QdrantConfigError, build_qdrant_client
from app.routers.auth import router as auth_router
from app.routers.citations import router as citations_router
from app.routers.documents import router as documents_router
from app.routers.query import router as query_router
from app.routers.search import router as search_router

app = FastAPI(
    title="Security Personal AI Query/Search/Document/Citation API",
    version="0.1.0",
    description="MVP FastAPI skeleton generated from the OpenAPI source of truth.",
)

config = load_config()
if config.cors_allow_origins or config.cors_allow_origin_regex:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=config.cors_allow_origins,
        allow_origin_regex=config.cors_allow_origin_regex,
        allow_methods=["*"],
        allow_headers=["*"],
        allow_credentials=False,
        max_age=86400,
    )

app.include_router(query_router)
app.include_router(search_router)
app.include_router(documents_router)
app.include_router(citations_router)
app.include_router(auth_router)
install_error_handlers(app)


@app.get("/health", tags=["Internal"], summary="Lightweight health check")
async def healthcheck() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/health/dependencies", tags=["Internal"], summary="Dependency health check")
async def dependency_healthcheck() -> JSONResponse:
    try:
        client = build_qdrant_client()
    except QdrantConfigError as exc:
        return JSONResponse(
            status_code=503,
            content={
                "status": "degraded",
                "qdrant": {
                    "configured": False,
                    "reachable": False,
                    "reason": str(exc),
                },
            },
        )

    try:
        collections = client.get_collections()
    except Exception as exc:  # pragma: no cover - network surface
        return JSONResponse(
            status_code=503,
            content={
                "status": "degraded",
                "qdrant": {
                    "configured": True,
                    "reachable": False,
                    "reason": f"{exc.__class__.__name__}",
                },
            },
        )

    return JSONResponse(
        status_code=200,
        content={
            "status": "ok",
            "qdrant": {
                "configured": True,
                "reachable": True,
                "collection_count": len(collections.collections),
            },
        },
    )
