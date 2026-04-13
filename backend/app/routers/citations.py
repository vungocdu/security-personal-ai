from __future__ import annotations

from fastapi import APIRouter, Depends

from app.auth import require_authenticated_user
from app.schemas import CitationResource
from app.services import CitationService

router = APIRouter(prefix="/api/v1/citations", tags=["Citations"], dependencies=[Depends(require_authenticated_user)])
service = CitationService()


@router.get("/{citationId}", response_model=CitationResource, summary="Resolve citation for UI preview or rehydration")
async def get_citation(citationId: str) -> CitationResource:
    return service.get_citation(citationId)
