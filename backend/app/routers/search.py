from __future__ import annotations

from fastapi import APIRouter, Depends

from app.auth import require_authenticated_user
from app.schemas import SearchRequest, SearchResponse
from app.services import SearchService

router = APIRouter(prefix="/api/v1/search", tags=["Search"], dependencies=[Depends(require_authenticated_user)])
service = SearchService()


@router.post("", response_model=SearchResponse, summary="Search documents or chunks without synthesis")
async def search_documents(request: SearchRequest) -> SearchResponse:
    return service.execute(request)
