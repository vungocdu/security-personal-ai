from __future__ import annotations

from fastapi import APIRouter, Depends

from app.auth import AuthenticatedUser, require_authenticated_user
from app.schemas import AuthMeResponse
from app.services import AuthService

router = APIRouter(prefix="/api/v1/auth", tags=["Auth"])
service = AuthService()


@router.get("/me", response_model=AuthMeResponse, summary="Resolve current authenticated user")
async def me(user: AuthenticatedUser = Depends(require_authenticated_user)) -> AuthMeResponse:
    return service.me(user)
