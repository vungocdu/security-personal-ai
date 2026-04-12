from __future__ import annotations

from datetime import date, datetime, timedelta, timezone

from .schemas import (
    AnswerConfidence,
    AnswerObject,
    CitationResource,
    DebugInfo,
    DocumentAcceptedResponse,
    DocumentCollection,
    DocumentResource,
    DocumentType,
    DocumentVersionCollection,
    DocumentVersionResource,
    FilterObject,
    ParseStatus,
    PreviewResource,
    QueryResponse,
    ScoreBreakdown,
    SearchChunkResult,
    SearchResponse,
    new_request_id,
)


def build_query_response(query: str, filters: FilterObject | None, include_debug: bool) -> QueryResponse:
    citation = CitationResource(
        citation_id="cit_001",
        document_id="doc_hpg_ar_2024",
        document_version_id="docver_hpg_ar_2024_v1",
        title="HPG Annual Report 2024",
        source="internal_repository",
        document_type=DocumentType.annual_report,
        page_number=87,
        section_heading="Risk Factors",
        chunk_id="chk_009182",
        snippet="Bien dong gia quang sat va than coc co the anh huong den bien loi nhuan gop...",
        text_offset_start=18240,
        text_offset_end=18410,
        preview_url="/api/v1/documents/doc_hpg_ar_2024/versions/docver_hpg_ar_2024_v1/preview/87",
        viewer_anchor="page=87&chunk=chk_009182",
        version_label="v1",
        confidence=0.91,
    )
    return QueryResponse(
        request_id=new_request_id(),
        query=query,
        filters=filters,
        answer=AnswerObject(
            summary="Ba nhóm rủi ro nổi bật là nhu cầu thép phục hồi chậm, biến động giá nguyên liệu và áp lực dòng tiền từ đầu tư lớn.",
            confidence=AnswerConfidence.medium,
            insufficient_evidence=False,
            disclaimer="Không coi đây là khuyến nghị đầu tư.",
        ),
        citations=[citation],
        debug=DebugInfo(
            retrieval_strategy="dense+sparse+metadata+rerank",
            dense_top_k=30,
            sparse_top_k=30,
            fused_top_k=20,
            context_top_n=8,
        )
        if include_debug
        else None,
    )


def build_search_response(query: str, page: int, limit: int) -> SearchResponse:
    result = SearchChunkResult(
        document_id="doc_ssi_ar_2023",
        document_version_id="docver_ssi_ar_2023_v1",
        title="SSI Annual Report 2023",
        document_type=DocumentType.annual_report,
        ticker="SSI",
        publication_date=date(2024, 3, 28),
        page_number=134,
        section_heading="Borrowings and Bonds",
        chunk_id="chk_1102",
        snippet="Tap doan co cac dieu khoan rang buoc lien quan den cac khoan vay...",
        preview_url="/api/v1/documents/doc_ssi_ar_2023/versions/docver_ssi_ar_2023_v1/preview/134",
        viewer_anchor="page=134&chunk=chk_1102",
        scores=ScoreBreakdown(dense=0.82, sparse=13.4, rerank=0.91),
    )
    return SearchResponse(
        request_id=new_request_id(),
        query=query,
        page=page,
        limit=limit,
        total=1,
        results=[result],
    )


def build_document_collection(page: int, limit: int) -> DocumentCollection:
    return DocumentCollection(
        page=page,
        limit=limit,
        total=1,
        data=[
            DocumentResource(
                document_id="doc_hpg_ar_2024",
                title="HPG Annual Report 2024",
                document_type=DocumentType.annual_report,
                ticker="HPG",
                source="internal_repository",
                language="vi",
                publication_date=date(2025, 3, 29),
                current_version_id="docver_hpg_ar_2024_v1",
                access_level="internal",
                index_status=ParseStatus.indexed,
            )
        ],
    )


def build_document(document_id: str) -> DocumentResource:
    return DocumentResource(
        document_id=document_id,
        title="HPG Annual Report 2024",
        document_type=DocumentType.annual_report,
        ticker="HPG",
        source="internal_repository",
        language="vi",
        publication_date=date(2025, 3, 29),
        current_version_id="docver_hpg_ar_2024_v1",
        access_level="internal",
        index_status=ParseStatus.indexed,
    )


def build_document_versions(document_id: str) -> DocumentVersionCollection:
    return DocumentVersionCollection(
        document_id=document_id,
        data=[
            DocumentVersionResource(
                document_id=document_id,
                document_version_id="docver_hpg_ar_2024_v1",
                version_label="v1",
                is_current_version=True,
                supersedes_version_id=None,
                publication_date=date(2025, 3, 29),
                parse_status=ParseStatus.indexed,
            )
        ],
    )


def build_upload_response() -> DocumentAcceptedResponse:
    return DocumentAcceptedResponse(
        document_id="doc_new_001",
        document_version_id="docver_new_001_v1",
        index_job_id="job_7751",
    )


def build_preview(document_id: str, version_id: str, page_number: int) -> PreviewResource:
    return PreviewResource(
        document_id=document_id,
        document_version_id=version_id,
        page_number=page_number,
        mime_type="application/pdf",
        preview_url=f"https://signed.example.com/preview/{document_id}/{version_id}/page/{page_number}",
        viewer_anchor=f"page={page_number}",
        expires_at=datetime.now(timezone.utc) + timedelta(minutes=30),
    )


def build_citation(citation_id: str) -> CitationResource:
    return CitationResource(
        citation_id=citation_id,
        document_id="doc_hpg_ar_2024",
        document_version_id="docver_hpg_ar_2024_v1",
        title="HPG Annual Report 2024",
        source="internal_repository",
        document_type=DocumentType.annual_report,
        page_number=87,
        section_heading="Risk Factors",
        chunk_id="chk_009182",
        snippet="Bien dong gia quang sat va than coc co the anh huong den bien loi nhuan gop...",
        text_offset_start=18240,
        text_offset_end=18410,
        preview_url="/api/v1/documents/doc_hpg_ar_2024/versions/docver_hpg_ar_2024_v1/preview/87",
        viewer_anchor="page=87&chunk=chk_009182",
        version_label="v1",
        confidence=0.91,
    )
