from __future__ import annotations

from copy import deepcopy
from datetime import date, datetime, timedelta, timezone

from app.schemas import (
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
    SearchDocumentResult,
    SearchResponse,
    new_request_id,
)


class FixtureRepository:
    """In-memory fixture repository backing the MVP API contracts."""

    def __init__(self) -> None:
        self._documents = [
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
            ),
            DocumentResource(
                document_id="doc_ssi_research_2024q4",
                title="SSI Research Report Q4 2024",
                document_type=DocumentType.research_report,
                ticker="SSI",
                source="broker_feed",
                language="en",
                publication_date=date(2024, 12, 18),
                current_version_id="docver_ssi_research_2024q4_v2",
                access_level="licensed",
                index_status=ParseStatus.indexed,
            ),
            DocumentResource(
                document_id="doc_fpt_fin_2024q4",
                title="FPT Financial Statement Q4 2024",
                document_type=DocumentType.financial_statement,
                ticker="FPT",
                source="issuer_upload",
                language="vi",
                publication_date=date(2025, 1, 22),
                current_version_id="docver_fpt_fin_2024q4_v1",
                access_level="internal",
                index_status=ParseStatus.indexing,
            ),
        ]
        self._versions = {
            "doc_hpg_ar_2024": [
                DocumentVersionResource(
                    document_id="doc_hpg_ar_2024",
                    document_version_id="docver_hpg_ar_2024_v1",
                    version_label="v1",
                    is_current_version=True,
                    supersedes_version_id=None,
                    publication_date=date(2025, 3, 29),
                    parse_status=ParseStatus.indexed,
                )
            ],
            "doc_ssi_research_2024q4": [
                DocumentVersionResource(
                    document_id="doc_ssi_research_2024q4",
                    document_version_id="docver_ssi_research_2024q4_v1",
                    version_label="v1",
                    is_current_version=False,
                    supersedes_version_id=None,
                    publication_date=date(2024, 12, 10),
                    parse_status=ParseStatus.superseded,
                ),
                DocumentVersionResource(
                    document_id="doc_ssi_research_2024q4",
                    document_version_id="docver_ssi_research_2024q4_v2",
                    version_label="v2",
                    is_current_version=True,
                    supersedes_version_id="docver_ssi_research_2024q4_v1",
                    publication_date=date(2024, 12, 18),
                    parse_status=ParseStatus.indexed,
                ),
            ],
            "doc_fpt_fin_2024q4": [
                DocumentVersionResource(
                    document_id="doc_fpt_fin_2024q4",
                    document_version_id="docver_fpt_fin_2024q4_v1",
                    version_label="v1",
                    is_current_version=True,
                    supersedes_version_id=None,
                    publication_date=date(2025, 1, 22),
                    parse_status=ParseStatus.indexing,
                )
            ],
        }
        self._citations = {
            "cit_hpg_risk_001": CitationResource(
                citation_id="cit_hpg_risk_001",
                document_id="doc_hpg_ar_2024",
                document_version_id="docver_hpg_ar_2024_v1",
                title="HPG Annual Report 2024",
                source="internal_repository",
                document_type=DocumentType.annual_report,
                page_number=87,
                section_heading="Risk Factors",
                chunk_id="chk_hpg_009182",
                snippet="Bien dong gia quang sat va than coc co the anh huong den bien loi nhuan gop...",
                text_offset_start=18240,
                text_offset_end=18410,
                preview_url="/api/v1/documents/doc_hpg_ar_2024/versions/docver_hpg_ar_2024_v1/preview/87",
                viewer_anchor="page=87&chunk=chk_hpg_009182",
                version_label="v1",
                confidence=0.91,
            ),
            "cit_hpg_cashflow_002": CitationResource(
                citation_id="cit_hpg_cashflow_002",
                document_id="doc_hpg_ar_2024",
                document_version_id="docver_hpg_ar_2024_v1",
                title="HPG Annual Report 2024",
                source="internal_repository",
                document_type=DocumentType.annual_report,
                page_number=104,
                section_heading="Capital Expenditure",
                chunk_id="chk_hpg_009399",
                snippet="Ap luc dong tien den tu chu ky dau tu lon va nhu cau von luu dong tang...",
                text_offset_start=23310,
                text_offset_end=23590,
                preview_url="/api/v1/documents/doc_hpg_ar_2024/versions/docver_hpg_ar_2024_v1/preview/104",
                viewer_anchor="page=104&chunk=chk_hpg_009399",
                version_label="v1",
                confidence=0.88,
            ),
            "cit_ssi_covenant_003": CitationResource(
                citation_id="cit_ssi_covenant_003",
                document_id="doc_ssi_research_2024q4",
                document_version_id="docver_ssi_research_2024q4_v2",
                title="SSI Research Report Q4 2024",
                source="broker_feed",
                document_type=DocumentType.research_report,
                page_number=12,
                section_heading="Balance Sheet Pressure",
                chunk_id="chk_ssi_1102",
                snippet="Covenant pressure remains manageable but margin lending exposure is rising...",
                text_offset_start=820,
                text_offset_end=1030,
                preview_url="/api/v1/documents/doc_ssi_research_2024q4/versions/docver_ssi_research_2024q4_v2/preview/12",
                viewer_anchor="page=12&chunk=chk_ssi_1102",
                version_label="v2",
                confidence=0.86,
            ),
        }
        self._search_results = [
            SearchChunkResult(
                document_id="doc_ssi_research_2024q4",
                document_version_id="docver_ssi_research_2024q4_v2",
                title="SSI Research Report Q4 2024",
                document_type=DocumentType.research_report,
                ticker="SSI",
                publication_date=date(2024, 12, 18),
                page_number=12,
                section_heading="Balance Sheet Pressure",
                chunk_id="chk_ssi_1102",
                snippet="Covenant pressure remains manageable but margin lending exposure is rising...",
                preview_url="/api/v1/documents/doc_ssi_research_2024q4/versions/docver_ssi_research_2024q4_v2/preview/12",
                viewer_anchor="page=12&chunk=chk_ssi_1102",
                scores=ScoreBreakdown(dense=0.82, sparse=13.4, rerank=0.91),
            ),
            SearchDocumentResult(
                document_id="doc_hpg_ar_2024",
                document_version_id="docver_hpg_ar_2024_v1",
                title="HPG Annual Report 2024",
                document_type=DocumentType.annual_report,
                ticker="HPG",
                publication_date=date(2025, 3, 29),
                source="internal_repository",
                language="vi",
                preview_url="/api/v1/documents/doc_hpg_ar_2024/versions/docver_hpg_ar_2024_v1/preview/1",
                scores=ScoreBreakdown(dense=0.79, sparse=8.6, rerank=0.84),
            ),
        ]

    def list_documents(
        self,
        *,
        ticker: str | None = None,
        document_type: str | None = None,
        source: str | None = None,
        language: str | None = None,
        date_from: date | None = None,
        date_to: date | None = None,
        page: int,
        limit: int,
    ) -> DocumentCollection:
        data = []
        for document in self._documents:
            if ticker and document.ticker != ticker:
                continue
            if document_type and document.document_type.value != document_type:
                continue
            if source and document.source != source:
                continue
            if language and document.language != language:
                continue
            if date_from and document.publication_date < date_from:
                continue
            if date_to and document.publication_date > date_to:
                continue
            data.append(deepcopy(document))

        start = (page - 1) * limit
        end = start + limit
        return DocumentCollection(page=page, limit=limit, total=len(data), data=data[start:end])

    def get_document(self, document_id: str) -> DocumentResource | None:
        for document in self._documents:
            if document.document_id == document_id:
                return deepcopy(document)
        return None

    def list_versions(self, document_id: str) -> DocumentVersionCollection | None:
        versions = self._versions.get(document_id)
        if versions is None:
            return None
        return DocumentVersionCollection(document_id=document_id, data=deepcopy(versions))

    def upload_document(
        self,
        *,
        filename: str,
        document_id: str | None = None,
        document_type: str | None = None,
        ticker: str | None = None,
        company_name: str | None = None,
        publication_date: date | None = None,
        source: str | None = None,
    ) -> DocumentAcceptedResponse:
        if document_id:
            document_index = self._find_document_index(document_id)
            if document_index is None:
                raise ValueError(f"Unknown document_id '{document_id}'")
            return self._append_document_version(
                document_index=document_index,
                document_type=document_type,
                ticker=ticker,
                publication_date=publication_date,
                source=source,
            )

        base = ticker.lower() if ticker else "uploaded"
        doc_id = f"doc_{base}_{len(self._documents) + 1:03d}"
        version_id = f"docver_{base}_{len(self._documents) + 1:03d}_v1"
        created_document = DocumentResource(
            document_id=doc_id,
            title=company_name or filename,
            document_type=DocumentType(document_type) if document_type else DocumentType.internal_note,
            ticker=ticker,
            source=source or "manual_upload",
            language="vi",
            publication_date=publication_date or date.today(),
            current_version_id=version_id,
            access_level="internal",
            index_status=ParseStatus.accepted,
        )
        self._documents.append(created_document)
        self._versions[doc_id] = [
            DocumentVersionResource(
                document_id=doc_id,
                document_version_id=version_id,
                version_label="v1",
                is_current_version=True,
                supersedes_version_id=None,
                publication_date=created_document.publication_date,
                parse_status=ParseStatus.accepted,
            )
        ]
        return DocumentAcceptedResponse(
            document_id=doc_id,
            document_version_id=version_id,
            index_job_id=f"job_{len(self._documents) + 7700}",
        )

    def _find_document_index(self, document_id: str) -> int | None:
        for index, document in enumerate(self._documents):
            if document.document_id == document_id:
                return index
        return None

    def _append_document_version(
        self,
        *,
        document_index: int,
        document_type: str | None,
        ticker: str | None,
        publication_date: date | None,
        source: str | None,
    ) -> DocumentAcceptedResponse:
        document = self._documents[document_index]
        versions = self._versions[document.document_id]
        current_version = next((version for version in versions if version.is_current_version), None)
        if current_version is None:
            raise ValueError(f"Document '{document.document_id}' has no current version.")

        current_version.is_current_version = False
        current_version.parse_status = ParseStatus.superseded

        next_version_number = len(versions) + 1
        base_version_id = current_version.document_version_id
        if "_v" in base_version_id:
            base_version_id = base_version_id.rsplit("_v", maxsplit=1)[0]
        new_version_id = f"{base_version_id}_v{next_version_number}"
        published_on = publication_date or date.today()

        versions.append(
            DocumentVersionResource(
                document_id=document.document_id,
                document_version_id=new_version_id,
                version_label=f"v{next_version_number}",
                is_current_version=True,
                supersedes_version_id=current_version.document_version_id,
                publication_date=published_on,
                parse_status=ParseStatus.accepted,
            )
        )

        document.current_version_id = new_version_id
        document.publication_date = published_on
        document.index_status = ParseStatus.accepted
        if ticker:
            document.ticker = ticker
        if document_type:
            document.document_type = DocumentType(document_type)
        if source:
            document.source = source

        return DocumentAcceptedResponse(
            document_id=document.document_id,
            document_version_id=new_version_id,
            index_job_id=f"job_{len(self._documents) + 7700 + len(versions)}",
        )

    def get_citation(self, citation_id: str) -> CitationResource | None:
        citation = self._citations.get(citation_id)
        return deepcopy(citation) if citation else None

    def get_preview(self, document_id: str, version_id: str, page_number: int) -> PreviewResource | None:
        document = self.get_document(document_id)
        if document is None:
            return None
        versions = self._versions.get(document_id)
        if versions is None or not any(item.document_version_id == version_id for item in versions):
            return None
        mime_type = "application/pdf"
        if document.document_type == DocumentType.research_report:
            mime_type = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        if document.document_type == DocumentType.financial_statement:
            mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        return PreviewResource(
            document_id=document_id,
            document_version_id=version_id,
            page_number=page_number,
            mime_type=mime_type,
            preview_url=f"https://signed.example.com/preview/{document_id}/{version_id}/page/{page_number}",
            viewer_anchor=f"page={page_number}",
            expires_at=datetime.now(timezone.utc) + timedelta(minutes=30),
        )

    def search(self, query: str, page: int, limit: int, filters: FilterObject | None) -> SearchResponse:
        lowered = query.lower()
        results = []
        for result in self._search_results:
            result_ticker = getattr(result, "ticker", None)
            if filters and filters.ticker and result_ticker not in filters.ticker:
                continue
            if filters and filters.document_type and result.document_type not in filters.document_type:
                continue
            haystack = f"{result.title} {getattr(result, 'snippet', '')} {getattr(result, 'source', '')}".lower()
            if lowered not in haystack and not any(token in haystack for token in lowered.split()):
                continue
            results.append(deepcopy(result))

        if not results:
            results = deepcopy(self._search_results)

        start = (page - 1) * limit
        end = start + limit
        return SearchResponse(
            request_id=new_request_id(),
            query=query,
            page=page,
            limit=limit,
            total=len(results),
            results=results[start:end],
        )

    def execute_query(self, query: str, filters: FilterObject | None, include_debug: bool, max_citations: int) -> QueryResponse:
        citations = [
            deepcopy(self._citations["cit_hpg_risk_001"]),
            deepcopy(self._citations["cit_hpg_cashflow_002"]),
        ]
        if filters and filters.ticker == ["SSI"]:
            citations = [deepcopy(self._citations["cit_ssi_covenant_003"])]

        insufficient = "khong du du lieu" in query.lower()
        answer = AnswerObject(
            summary=(
                "Khong du can cu de ket luan tu bo tai lieu hien tai."
                if insufficient
                else "Ba nhom rui ro noi bat la nhu cau phuc hoi cham, bien dong gia nguyen lieu va ap luc dong tien tu chu ky dau tu lon."
            ),
            confidence=AnswerConfidence.low if insufficient else AnswerConfidence.medium,
            insufficient_evidence=insufficient,
            disclaimer="Khong coi day la khuyen nghi dau tu.",
        )
        return QueryResponse(
            request_id=new_request_id(),
            query=query,
            filters=filters,
            answer=answer,
            citations=citations[:max_citations],
            debug=DebugInfo(
                retrieval_strategy="dense+sparse+metadata+rerank",
                dense_top_k=30,
                sparse_top_k=30,
                fused_top_k=20,
                context_top_n=min(max_citations, 8),
            )
            if include_debug
            else None,
        )


fixture_repository = FixtureRepository()
