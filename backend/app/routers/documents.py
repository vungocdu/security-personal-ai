from __future__ import annotations

from datetime import date

from fastapi import APIRouter, File, Form, Query, UploadFile, status

from app.schemas import (
    DocumentAcceptedResponse,
    DocumentCollection,
    DocumentResource,
    DocumentVersionCollection,
    PreviewResource,
)
from app.stubs import (
    build_document,
    build_document_collection,
    build_document_versions,
    build_preview,
    build_upload_response,
)

router = APIRouter(prefix="/api/v1/documents", tags=["Documents"])


@router.get("", response_model=DocumentCollection, summary="List documents visible to caller")
async def list_documents(
    ticker: str | None = Query(default=None),
    document_type: str | None = Query(default=None),
    source: str | None = Query(default=None),
    language: str | None = Query(default=None),
    date_from: date | None = Query(default=None),
    date_to: date | None = Query(default=None),
    page: int = Query(default=1, ge=1),
    limit: int = Query(default=20, ge=1, le=100),
) -> DocumentCollection:
    _ = (ticker, document_type, source, language, date_from, date_to)
    return build_document_collection(page, limit)


@router.post(
    "",
    response_model=DocumentAcceptedResponse,
    status_code=status.HTTP_202_ACCEPTED,
    summary="Upload document and create ingestion job",
)
async def upload_document(
    file: UploadFile = File(...),
    document_type: str | None = Form(default=None),
    ticker: str | None = Form(default=None),
    company_name: str | None = Form(default=None),
    publication_date: date | None = Form(default=None),
    source: str | None = Form(default=None),
) -> DocumentAcceptedResponse:
    _ = (file, document_type, ticker, company_name, publication_date, source)
    return build_upload_response()


@router.get("/{document_id}", response_model=DocumentResource, summary="Get logical document details")
async def get_document(document_id: str) -> DocumentResource:
    return build_document(document_id)


@router.get("/{document_id}/versions", response_model=DocumentVersionCollection, summary="List visible versions for a logical document")
async def list_document_versions(document_id: str) -> DocumentVersionCollection:
    return build_document_versions(document_id)


@router.get(
    "/{document_id}/versions/{version_id}/preview/{page_number}",
    response_model=PreviewResource,
    summary="Resolve preview resource for a page in a specific version",
)
async def get_document_preview(document_id: str, version_id: str, page_number: int) -> PreviewResource:
    return build_preview(document_id, version_id, page_number)
