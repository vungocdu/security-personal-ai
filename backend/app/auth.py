from __future__ import annotations

import json
from dataclasses import dataclass
import firebase_admin
from firebase_admin import auth as firebase_auth
from fastapi import Header, HTTPException, status

from app.config import AppConfig, load_config
from app.firebase import firebase_app


@dataclass(frozen=True, slots=True)
class AuthenticatedUser:
    uid: str
    email: str | None
    name: str | None


def verify_firebase_token(token: str, config: AppConfig | None = None) -> AuthenticatedUser | None:
    settings = config or load_config()
    if not settings.auth_enforce:
        return AuthenticatedUser(uid="anonymous", email=None, name="Anonymous")
    if not token:
        return None
    try:
        decoded = firebase_auth.verify_id_token(token, app=firebase_app())
    except (
        firebase_auth.ExpiredIdTokenError,
        firebase_auth.InvalidIdTokenError,
        firebase_auth.RevokedIdTokenError,
        firebase_auth.UserDisabledError,
    ):
        return None
    except Exception as exc:
        raise _service_unavailable("auth_provider_unavailable", f"Firebase token verification failed: {exc.__class__.__name__}") from exc
    uid = decoded.get("uid")
    if not isinstance(uid, str) or not uid:
        return None
    email = decoded.get("email")
    name = decoded.get("name")
    return AuthenticatedUser(
        uid=uid,
        email=email if isinstance(email, str) else None,
        name=name if isinstance(name, str) else None,
    )


def require_authenticated_user(authorization: str | None = Header(default=None, alias="Authorization")) -> AuthenticatedUser:
    settings = load_config()
    if not settings.auth_enforce:
        return AuthenticatedUser(uid="anonymous", email=None, name="Anonymous")
    if not authorization:
        raise _unauthorized("auth_missing_token", "Missing bearer token.")
    scheme, _, token = authorization.partition(" ")
    if scheme.lower() != "bearer" or not token:
        raise _unauthorized("auth_invalid_token", "Authorization header must use Bearer token.")

    resolved = verify_firebase_token(token, settings)
    if resolved is None:
        raise _unauthorized("auth_invalid_token", "Invalid or expired access token.")
    return resolved


def _unauthorized(code: str, message: str) -> HTTPException:
    return HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail={"code": code, "message": message},
    )


def _service_unavailable(code: str, message: str) -> HTTPException:
    return HTTPException(
        status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
        detail={"code": code, "message": message},
    )
