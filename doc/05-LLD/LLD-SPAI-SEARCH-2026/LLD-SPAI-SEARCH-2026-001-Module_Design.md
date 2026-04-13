# Module Design Specification

## DOCUMENT CONTROL

| Field | Value |
| --- | --- |
| **Document ID** | LLD-SPAI-SEARCH-2026-001 |
| **Template Version** | 1.0 |
| **Document Version** | 1.0 |
| **Project / Product** | Security Personal AI |
| **Module / Component** | Search and Retrieval |
| **Author** | OpenAI Codex, AI Implementation Draft |
| **Reviewer(s)** | Tech Lead, QA Lead, Security Lead |
| **Document Status** | Draft |
| **Classification** | Confidential |
| **Creation Date** | 2026-04-12 |
| **Last Updated** | 2026-04-12 |
| **AI-Assisted** | [x] Yes - Tool: **Codex** |

## 1. PURPOSE & SCOPE

- **Objective:** Dinh nghia contract hybrid retrieval + rerank cho Query/Search APIs, bao gom metadata filtering, chunk/document result shaping va fallback logic MVP.
- **In Scope:** `POST /api/v1/search`, retrieval service, rerank contract, score breakdown, chunk/document result DTOs, minimal metadata schema cap document/chunk.
- **Out of Scope:** personalization, feedback learning loop, reciprocal rank fusion tuning nang cao, vector provider switching automation.

## 2. CONTEXT & ASSUMPTIONS

- **System Context Diagram:** Tham chieu AD section retrieval architecture va runtime view.
- **Dependencies:** Qdrant, PostgreSQL metadata, object storage preview references, FilterObject, search router, query module.
- **Assumptions & Constraints:** MVP co the stub retrieval data nhung phai giu dung `dense + sparse + metadata + rerank` contract trong docs va API.

## 3. FUNCTIONAL DECOMPOSITION

| Capability | Description | Trigger | Output | Related Requirements |
| --- | --- | --- | --- | --- |
| Hybrid retrieval | Hop nhat dense, sparse va metadata filters | Query/Search request | Candidate set | BR-FN-003 |
| Rerank | Sap lai candidate theo muc lien quan cuoi cung | Candidate set > 0 | Ranked candidates | BR-NF-002 |
| Search response shaping | Tra chunk hoac document results dung schema | Search API | SearchResponse | BR-FN-003 |
| Access filtering | Loai tai lieu user khong duoc xem | Moi retrieval request | Visible candidate set | BR-NF-003 |

- **Business Rules:**
  - Dense retrieval, sparse retrieval va metadata filter la 3 thanh phan bat buoc cua contract, du implementation co the stub o MVP.
  - Rerank la bat buoc cho top candidate truoc khi chon context cho query answer.
  - `scores.rerank` co the nullable neu result_type=document va rerank chua ap dung, nhung field phai ton tai trong schema object neu co scores.
- **State Management:** Search la stateless. Candidate state chi ton tai trong request lifecycle.

## 4. SEQUENCE OF OPERATIONS

- **Primary Flow:** Router nhan `SearchRequest` -> SearchService normalize filters -> DenseRetriever + SparseRetriever -> MetadataFilter -> ResultFusion -> Reranker -> Presenter build `SearchResponse`.
- **Alternate / Exception Flows:** neu sparse hoac dense provider unavailable trong MVP stub, service van phai tra score breakdown hop le cho fixture test; unauthorized document bi loai truoc fusion.
- **Diagram:** [LLD-SPAI-SEARCH-2026-003-Sequence_Diagram.md](./LLD-SPAI-SEARCH-2026-003-Sequence_Diagram.md)

## 5. COMPONENT & CLASS DESIGN

- **Component Overview:** `SearchRouter`, `SearchService`, `DenseRetriever`, `SparseRetriever`, `MetadataFilterBuilder`, `ResultFusion`, `Reranker`, `SearchResultPresenter`.
- **Design Patterns:** strategy pattern cho retrievers/reranker, repository adapter cho metadata lookup, presenter cho result union types.
- **Class Diagram:** [LLD-SPAI-SEARCH-2026-002-Class_Diagram.md](./LLD-SPAI-SEARCH-2026-002-Class_Diagram.md)
- **Interfaces:**
  - `search(request: SearchRequest) -> SearchResponse`
  - `retrieve(query: str, filters: NormalizedFilters) -> Candidate[]`
  - `rerank(query: str, candidates: Candidate[]) -> Candidate[]`

## 6. INTERFACES & CONTRACTS

| Interface | Consumer | Provider | Protocol | DTO / Payload | Notes |
| --- | --- | --- | --- | --- | --- |
| `POST /api/v1/search` | Frontend, QueryService | FastAPI SearchRouter | REST | `SearchRequest`, `SearchResponse` | Source of truth: OpenAPI |
| Dense retrieval | SearchService | DenseRetriever | In-process | `Candidate[]` | semantic retrieval |
| Sparse retrieval | SearchService | SparseRetriever | In-process | `Candidate[]` | keyword/BM25 style retrieval |
| Rerank | SearchService | Reranker | In-process | `Candidate[]` | top-N rerank bat buoc |

- **Backward Compatibility:** Union shape `SearchChunkResult | SearchDocumentResult` khong duoc doi result_type values.
- **Error Models:** `validation_error`, `auth_forbidden`, `upstream_timeout`, `internal_error`.

## 7. DATA DESIGN

- **Data Sources:** `documents`, `document_versions`, `document_chunks`, object storage preview artifacts.
- **Schemas:**
  - Document metadata toi thieu: `document_id`, `current_version_id`, `title`, `document_type`, `ticker`, `source`, `language`, `publication_date`, `access_level`, `index_status`.
  - Chunk metadata toi thieu: `chunk_id`, `document_id`, `document_version_id`, `page_number`, `section_heading`, `preview_url`, `viewer_anchor`, `embedding_ref`, `keyword_terms`, `access_level`.
- **Data Flow:** Search request -> filters -> retriever candidates -> fused/reranked candidates -> result presenter.
- **Retention & Archiving:** Search module khong tu luu ket qua trong MVP.

## 8. ERROR HANDLING & RESILIENCE

- **Failure Modes:** vector store timeout, metadata miss, rerank provider fail, preview url missing.
- **Fallbacks / Retries:** Neu rerank provider fail, co the fallback sang fused order va ghi log canh bao; neu preview url missing van tra result nhung frontend phai hien fallback.
- **Idempotency:** Search read-only.
- **Monitoring Hooks:** log candidate_count_dense/sparse/fused, rerank_applied, fallback_used.

## 9. SECURITY & PRIVACY CONTROLS

- **Authentication & Authorization:** Search nhan user scope tu gateway.
- **Data Protection:** Access filter bat buoc truoc result presenter.
- **Input Validation / Sanitisation:** query length, filter enums, page/limit boundaries.
- **Audit Logging:** request id, endpoint, result count, forbidden filter intersections.
- **Threat Considerations:** Khong tra snippet cua tai lieu ma user khong co quyen.

## 10. PERFORMANCE & SCALABILITY

- **Key Metrics:** retrieval p95 < 2s, rerank p95 < 1.5s, result page <= 100.
- **Capacity Planning:** SearchService stateless; retrievers co the scale doc lap.
- **Caching Strategy:** chua bat buoc; co the them metadata cache sau.
- **Load / Stress Considerations:** chunk-heavy documents co the lam dense payload lon; can gioi han candidate windows.

## 11. OBSERVABILITY & OPERATIONS

- **Logs:** `search_received`, `search_fused`, `search_reranked`, `search_completed`.
- **Metrics:** retrieval_latency_ms, rerank_latency_ms, search_total_results.
- **Tracing:** spans cho dense, sparse, fusion, rerank.
- **Feature Flags / Configuration:** `SEARCH_DEFAULT_LIMIT`, `RERANK_ENABLED`.

## 12. VERIFICATION & TESTABILITY

- **Unit Tests:** search defaults, score breakdown, result_type union, filter pass-through, rerank fallback.
- **Integration Tests:** query module goi search service va nhan duoc ranked chunk results.
- **Performance Tests:** basic latency smoke test voi stub candidate sets.
- **Security Tests:** unauthorized document bi loai khoi results.
- **Traceability:** Cover BR-FN-003, BR-NF-002, BR-NF-003.

## 13. RISKS & OPEN ISSUES

| ID | Description | Impact | Mitigation / Action | Owner | Status |
| --- | --- | --- | --- | --- | --- |
| R-LLD-SEARCH-001 | Hybrid retrieval contract bi rut gon thanh vector-only trong implement sau nay | High | Giu contract ro trong LLD va test names | Backend | Open |
| R-LLD-SEARCH-002 | Preview fields co the bi bo sot trong search results | Medium | Contract test voi frontend fixtures | Backend | Open |

## 14. APPROVALS & CHANGE HISTORY

| Version | Date | Description | Author | Reviewer | Approved By |
| --- | --- | --- | --- | --- | --- |
| 1.0 | 2026-04-12 | Initial release | OpenAI Codex | Pending | Pending |
