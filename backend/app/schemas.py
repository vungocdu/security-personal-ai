from __future__ import annotations

from datetime import date, datetime
from enum import Enum
from typing import Literal
from uuid import uuid4

from pydantic import BaseModel, ConfigDict, Field


class StrictModel(BaseModel):
    model_config = ConfigDict(extra="forbid")


class DocumentType(str, Enum):
    annual_report = "annual_report"
    financial_statement = "financial_statement"
    research_report = "research_report"
    legal_document = "legal_document"
    disclosure = "disclosure"
    internal_note = "internal_note"


class AnswerConfidence(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"


class ParseStatus(str, Enum):
    accepted = "accepted"
    indexing = "indexing"
    indexed = "indexed"
    failed = "failed"
    withdrawn = "withdrawn"
    invalidated = "invalidated"
    superseded = "superseded"


class FilterObject(StrictModel):
    ticker: list[str] | None = None
    document_type: list[DocumentType] | None = None
    source: list[str] | None = None
    language: list[str] | None = None
    date_from: date | None = None
    date_to: date | None = None
    reporting_period: list[str] | None = None
    sector: list[str] | None = None
    market: list[str] | None = None


class QueryOptions(StrictModel):
    include_debug: bool = False
    max_citations: int = Field(default=8, ge=1, le=20)


class QueryRequest(StrictModel):
    query: str = Field(min_length=1, max_length=4000)
    filters: FilterObject | None = None
    options: QueryOptions | None = None


class SearchRequest(StrictModel):
    query: str = Field(min_length=1, max_length=4000)
    filters: FilterObject | None = None
    page: int = Field(default=1, ge=1)
    limit: int = Field(default=20, ge=1, le=100)


class AuthMeResponse(StrictModel):
    uid: str
    email: str | None = None
    name: str | None = None


class ScoreBreakdown(StrictModel):
    dense: float | None = None
    sparse: float | None = None
    rerank: float | None = None


class AnswerObject(StrictModel):
    summary: str
    confidence: AnswerConfidence
    insufficient_evidence: bool
    disclaimer: str | None = None


class DebugInfo(StrictModel):
    retrieval_strategy: str | None = None
    dense_top_k: int | None = None
    sparse_top_k: int | None = None
    fused_top_k: int | None = None
    context_top_n: int | None = None


class CitationResource(StrictModel):
    citation_id: str
    document_id: str
    document_version_id: str
    title: str
    source: str
    document_type: DocumentType
    page_number: int | None = Field(default=None, ge=1)
    section_heading: str | None = None
    chunk_id: str
    snippet: str
    text_offset_start: int | None = Field(default=None, ge=0)
    text_offset_end: int | None = Field(default=None, ge=0)
    preview_url: str | None = None
    viewer_anchor: str | None = None
    version_label: str
    confidence: float | None = Field(default=None, ge=0, le=1)


class QueryResponse(StrictModel):
    request_id: str
    query: str
    filters: FilterObject | None = None
    answer: AnswerObject
    citations: list[CitationResource]
    debug: DebugInfo | None = None


class SearchChunkResult(StrictModel):
    result_type: Literal["chunk"] = "chunk"
    document_id: str
    document_version_id: str
    title: str
    document_type: DocumentType
    ticker: str | None = None
    publication_date: date | None = None
    page_number: int | None = Field(default=None, ge=1)
    section_heading: str | None = None
    chunk_id: str
    snippet: str
    preview_url: str | None = None
    viewer_anchor: str | None = None
    scores: ScoreBreakdown | None = None


class SearchDocumentResult(StrictModel):
    result_type: Literal["document"] = "document"
    document_id: str
    document_version_id: str
    title: str
    document_type: DocumentType
    ticker: str | None = None
    publication_date: date | None = None
    source: str | None = None
    language: str | None = None
    preview_url: str | None = None
    scores: ScoreBreakdown | None = None


class SearchResponse(StrictModel):
    request_id: str
    query: str
    page: int
    limit: int
    total: int
    results: list[SearchChunkResult | SearchDocumentResult]


class DocumentResource(StrictModel):
    document_id: str
    title: str
    document_type: DocumentType
    ticker: str | None = None
    source: str
    language: str
    publication_date: date
    current_version_id: str
    access_level: str
    index_status: ParseStatus | Literal["accepted", "indexing", "indexed", "failed", "superseded"]


class DocumentAcceptedResponse(StrictModel):
    document_id: str
    document_version_id: str
    index_job_id: str
    status: Literal["accepted"] = "accepted"


class DocumentVersionResource(StrictModel):
    document_id: str
    document_version_id: str
    version_label: str
    is_current_version: bool
    supersedes_version_id: str | None = None
    publication_date: date
    parse_status: ParseStatus


class DocumentCollection(StrictModel):
    page: int
    limit: int
    total: int
    data: list[DocumentResource]


class DocumentVersionCollection(StrictModel):
    document_id: str
    data: list[DocumentVersionResource]


class PreviewResource(StrictModel):
    document_id: str
    document_version_id: str
    page_number: int
    mime_type: str
    preview_url: str
    viewer_anchor: str | None = None
    expires_at: datetime


class ErrorDetail(StrictModel):
    field: str | None = None
    issue: str


class ErrorBody(StrictModel):
    code: str
    message: str
    details: list[ErrorDetail] | None = None
    request_id: str


class ErrorEnvelope(StrictModel):
    error: ErrorBody


class RepositoryFolderResource(StrictModel):
    name: str
    path: str


class RepositoryFileResource(StrictModel):
    name: str
    path: str
    size_bytes: int | None = None
    content_type: str | None = None
    updated_at: datetime | None = None


class RepositoryListingResponse(StrictModel):
    path: str
    folders: list[RepositoryFolderResource]
    files: list[RepositoryFileResource]


class CreateFolderRequest(StrictModel):
    path: str = Field(min_length=1, max_length=500)


class CreateFolderResponse(StrictModel):
    folder: RepositoryFolderResource


class UploadRepositoryFileResponse(StrictModel):
    file: RepositoryFileResource


def new_request_id() -> str:
    return str(uuid4())
