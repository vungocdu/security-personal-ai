from __future__ import annotations

import json
from dataclasses import dataclass
from functools import lru_cache

import firebase_admin
from firebase_admin import auth as firebase_auth
from firebase_admin import credentials
from fastapi import Header, HTTPException, status

from app.config import AppConfig, load_config


@dataclass(frozen=True, slots=True)
class AuthenticatedUser:
    uid: str
    email: str | None
    name: str | None


def _build_firebase_credential(config: AppConfig):
    if config.firebase_service_account_json:
        service_account_info = json.loads(config.firebase_service_account_json)
        return credentials.Certificate(service_account_info)
    if config.firebase_service_account_path:
        return credentials.Certificate(config.firebase_service_account_path)
    return credentials.ApplicationDefault()


@lru_cache(maxsize=1)
def _firebase_app() -> firebase_admin.App:
    config = load_config()
    options = {"projectId": config.firebase_project_id} if config.firebase_project_id else None
    credential = _build_firebase_credential(config)
    try:
        return firebase_admin.get_app()
    except ValueError:
        return firebase_admin.initialize_app(credential=credential, options=options)


def verify_firebase_token(token: str, config: AppConfig | None = None) -> AuthenticatedUser | None:
    settings = config or load_config()
    if not settings.auth_enforce:
        return AuthenticatedUser(uid="anonymous", email=None, name="Anonymous")
    if not token:
        return None
    try:
        decoded = firebase_auth.verify_id_token(token, app=_firebase_app())
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
