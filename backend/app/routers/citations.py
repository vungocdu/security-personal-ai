from __future__ import annotations

from fastapi import APIRouter

from app.schemas import CitationResource
from app.stubs import build_citation

router = APIRouter(prefix="/api/v1/citations", tags=["Citations"])


@router.get("/{citation_id}", response_model=CitationResource, summary="Resolve citation for UI preview or rehydration")
async def get_citation(citation_id: str) -> CitationResource:
    return build_citation(citation_id)
