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
from app.services import DocumentService

router = APIRouter(prefix="/api/v1/documents", tags=["Documents"])
service = DocumentService()


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
    return service.list_documents(
        ticker=ticker,
        document_type=document_type,
        source=source,
        language=language,
        date_from=date_from,
        date_to=date_to,
        page=page,
        limit=limit,
    )


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
    return service.upload_document(
        filename=file.filename or "uploaded-document",
        document_type=document_type,
        ticker=ticker,
        company_name=company_name,
        publication_date=publication_date,
        source=source,
    )


@router.get("/{documentId}", response_model=DocumentResource, summary="Get logical document details")
async def get_document(documentId: str) -> DocumentResource:
    return service.get_document(documentId)


@router.get("/{documentId}/versions", response_model=DocumentVersionCollection, summary="List visible versions for a logical document")
async def list_document_versions(documentId: str) -> DocumentVersionCollection:
    return service.list_versions(documentId)


@router.get(
    "/{documentId}/versions/{versionId}/preview/{pageNumber}",
    response_model=PreviewResource,
    summary="Resolve preview resource for a page in a specific version",
)
async def get_document_preview(documentId: str, versionId: str, pageNumber: int) -> PreviewResource:
    return service.get_preview(documentId, versionId, pageNumber)
