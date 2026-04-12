from __future__ import annotations

from fastapi import APIRouter

from app.schemas import SearchRequest, SearchResponse
from app.stubs import build_search_response

router = APIRouter(prefix="/api/v1/search", tags=["Search"])


@router.post("", response_model=SearchResponse, summary="Search documents or chunks without synthesis")
async def search_documents(request: SearchRequest) -> SearchResponse:
    return build_search_response(request.query, request.page, request.limit)
