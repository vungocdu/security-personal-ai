from __future__ import annotations

from fastapi import APIRouter

from app.schemas import SearchRequest, SearchResponse
from app.services import SearchService

router = APIRouter(prefix="/api/v1/search", tags=["Search"])
service = SearchService()


@router.post("", response_model=SearchResponse, summary="Search documents or chunks without synthesis")
async def search_documents(request: SearchRequest) -> SearchResponse:
    return service.execute(request)
