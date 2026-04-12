from __future__ import annotations

from fastapi import APIRouter

from app.schemas import QueryRequest, QueryResponse
from app.services import QueryService

router = APIRouter(prefix="/api/v1/query", tags=["Query"])
service = QueryService()


@router.post("", response_model=QueryResponse, summary="Execute grounded query with synthesis and citations")
async def execute_query(request: QueryRequest) -> QueryResponse:
    return service.execute(request)
