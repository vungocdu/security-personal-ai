from __future__ import annotations

from dataclasses import dataclass
from datetime import date

from fastapi import HTTPException, status

from app.repositories import fixture_repository
from app.schemas import (
    CitationResource,
    DocumentAcceptedResponse,
    DocumentCollection,
    DocumentResource,
    DocumentVersionCollection,
    FilterObject,
    PreviewResource,
    QueryRequest,
    QueryResponse,
    SearchRequest,
    SearchResponse,
)


@dataclass(slots=True)
class QueryService:
    def execute(self, request: QueryRequest) -> QueryResponse:
        include_debug = bool(request.options and request.options.include_debug)
        max_citations = request.options.max_citations if request.options else 8
        return fixture_repository.execute_query(request.query, request.filters, include_debug, max_citations)


@dataclass(slots=True)
class SearchService:
    def execute(self, request: SearchRequest) -> SearchResponse:
        return fixture_repository.search(request.query, request.page, request.limit, request.filters)


@dataclass(slots=True)
class DocumentService:
    def list_documents(
        self,
        *,
        ticker: str | None,
        document_type: str | None,
        source: str | None,
        language: str | None,
        date_from: date | None,
        date_to: date | None,
        page: int,
        limit: int,
    ) -> DocumentCollection:
        return fixture_repository.list_documents(
            ticker=ticker,
            document_type=document_type,
            source=source,
            language=language,
            date_from=date_from,
            date_to=date_to,
            page=page,
            limit=limit,
        )

    def upload_document(
        self,
        *,
        filename: str,
        document_type: str | None,
        ticker: str | None,
        company_name: str | None,
        publication_date: date | None,
        source: str | None,
    ) -> DocumentAcceptedResponse:
        return fixture_repository.upload_document(
            filename=filename,
            document_type=document_type,
            ticker=ticker,
            company_name=company_name,
            publication_date=publication_date,
            source=source,
        )

    def get_document(self, document_id: str) -> DocumentResource:
        document = fixture_repository.get_document(document_id)
        if document is None:
            raise not_found("document_not_found", f"Document '{document_id}' was not found.")
        return document

    def list_versions(self, document_id: str) -> DocumentVersionCollection:
        versions = fixture_repository.list_versions(document_id)
        if versions is None:
            raise not_found("document_not_found", f"Document '{document_id}' was not found.")
        return versions

    def get_preview(self, document_id: str, version_id: str, page_number: int) -> PreviewResource:
        preview = fixture_repository.get_preview(document_id, version_id, page_number)
        if preview is None:
            raise not_found("preview_not_found", f"Preview for document '{document_id}' was not found.")
        return preview


@dataclass(slots=True)
class CitationService:
    def get_citation(self, citation_id: str) -> CitationResource:
        citation = fixture_repository.get_citation(citation_id)
        if citation is None:
            raise not_found("citation_not_found", f"Citation '{citation_id}' was not found.")
        return citation


def not_found(code: str, message: str) -> HTTPException:
    return HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail={"code": code, "message": message},
    )
