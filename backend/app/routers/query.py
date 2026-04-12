from __future__ import annotations

from fastapi import APIRouter

from app.schemas import QueryRequest, QueryResponse
from app.stubs import build_query_response

router = APIRouter(prefix="/api/v1/query", tags=["Query"])


@router.post("", response_model=QueryResponse, summary="Execute grounded query with synthesis and citations")
async def execute_query(request: QueryRequest) -> QueryResponse:
    include_debug = bool(request.options and request.options.include_debug)
    return build_query_response(request.query, request.filters, include_debug)
