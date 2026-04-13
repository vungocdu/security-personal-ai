from __future__ import annotations

from fastapi import APIRouter, Depends

from app.auth import require_authenticated_user
from app.schemas import QueryRequest, QueryResponse
from app.services import QueryService

router = APIRouter(prefix="/api/v1/query", tags=["Query"], dependencies=[Depends(require_authenticated_user)])
service = QueryService()


@router.post("", response_model=QueryResponse, summary="Execute grounded query with synthesis and citations")
async def execute_query(request: QueryRequest) -> QueryResponse:
    return service.execute(request)
