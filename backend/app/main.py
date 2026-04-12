from __future__ import annotations

from fastapi import FastAPI

from app.routers.citations import router as citations_router
from app.routers.documents import router as documents_router
from app.routers.query import router as query_router
from app.routers.search import router as search_router

app = FastAPI(
    title="Security Personal AI Query/Search/Document/Citation API",
    version="0.1.0",
    description="MVP FastAPI skeleton generated from the OpenAPI source of truth.",
)

app.include_router(query_router)
app.include_router(search_router)
app.include_router(documents_router)
app.include_router(citations_router)


@app.get("/health", tags=["Internal"], summary="Lightweight health check")
async def healthcheck() -> dict[str, str]:
    return {"status": "ok"}
