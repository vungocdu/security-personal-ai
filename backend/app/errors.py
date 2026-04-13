from __future__ import annotations

from uuid import uuid4

from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.schemas import ErrorBody, ErrorDetail, ErrorEnvelope


def _request_id(request: Request) -> str:
    return request.headers.get("x-request-id", str(uuid4()))


def error_response(*, request: Request, status_code: int, code: str, message: str, details: list[ErrorDetail] | None = None) -> JSONResponse:
    envelope = ErrorEnvelope(
        error=ErrorBody(
            code=code,
            message=message,
            details=details,
            request_id=_request_id(request),
        )
    )
    return JSONResponse(status_code=status_code, content=envelope.model_dump(mode="json"))


def install_error_handlers(app: FastAPI) -> None:
    @app.exception_handler(HTTPException)
    async def handle_http_exception(request: Request, exc: HTTPException) -> JSONResponse:
        if isinstance(exc.detail, dict):
            code = exc.detail.get("code", "http_error")
            message = exc.detail.get("message", "Request failed.")
        else:
            code = "http_error"
            message = str(exc.detail)
        return error_response(request=request, status_code=exc.status_code, code=code, message=message)

    @app.exception_handler(RequestValidationError)
    async def handle_validation_error(request: Request, exc: RequestValidationError) -> JSONResponse:
        details = [
            ErrorDetail(field=".".join(str(part) for part in err["loc"] if part != "body"), issue=err["msg"])
            for err in exc.errors()
        ]
        return error_response(
            request=request,
            status_code=422,
            code="validation_error",
            message="Request validation failed.",
            details=details,
        )

    @app.exception_handler(Exception)
    async def handle_unexpected_error(request: Request, exc: Exception) -> JSONResponse:
        return error_response(
            request=request,
            status_code=500,
            code="internal_error",
            message="An unexpected error occurred.",
        )
