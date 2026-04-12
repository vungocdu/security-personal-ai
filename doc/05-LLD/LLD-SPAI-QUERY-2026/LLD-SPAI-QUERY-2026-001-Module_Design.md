# Module Design Specification

**MERCURY SOLUTIONS**
**Software Engineering Excellence**

---

## DOCUMENT CONTROL

| Field | Value |
| --- | --- |
| **Document ID** | LLD-SPAI-QUERY-2026-001 |
| **Template Version** | 1.0 |
| **Document Version** | 1.0 |
| **Project / Product** | Security Personal AI |
| **Module / Component** | Query Orchestration |
| **Author** | OpenAI Codex, AI Implementation Draft |
| **Reviewer(s)** | Tech Lead, QA Lead, Security Lead |
| **Document Status** | Draft |
| **Classification** | Confidential |
| **Creation Date** | 2026-04-12 |
| **Last Updated** | 2026-04-12 |
| **Approved By** | Pending |
| **Approval Date** | Pending |
| **Next Review Date** | 2026-04-26 |
| **AI-Assisted** | [x] Yes - Tool: **Codex** |

---

## 1. PURPOSE & SCOPE

- **Objective:** Chuẩn hoa request query va dieu phoi grounded answer flow cho MVP query-first RAG, dam bao answer chi duoc tong hop tren context da retrieve va co citation.
- **In Scope:** `POST /api/v1/query`, request validation, filter normalization, orchestration service, answer envelope, debug payload, trace id propagation.
- **Out of Scope:** query history, session memory, compare workflow da buoc, personalized ranking, recommendation logic.

## 2. CONTEXT & ASSUMPTIONS

- **System Context Diagram:** Tham chieu [AD-SPAI-2026-001-Architecture_Design.md](/Users/steve/development/mercury/security-personal-ai/doc/02-Architecture/AD/AD-SPAI-2026-001-Architecture_Design.md) section container/runtime view.
- **Dependencies:** FastAPI router, Pydantic schemas, QueryService, SearchService, CitationService, LangGraph orchestrator stub/provider, auth context.
- **Assumptions & Constraints:** Phase 1 chi ho tro text query; orchestration co the duoc stub hoa bang fixture data mien response giong OpenAPI; access control duoc ap truoc retrieval.

## 3. FUNCTIONAL DECOMPOSITION

| Capability | Description | Trigger | Output | Related Requirements |
| --- | --- | --- | --- | --- |
| Query intake | Validate payload va tao request id | User POST query | QueryCommand | BR-FN-003 |
| Filter normalization | Chuyen filter tu API payload sang retrieval constraint | Query request co filters | NormalizedQueryContext | BR-FN-003, BR-FN-007 |
| Retrieval orchestration | Goi hybrid retrieval + rerank | QueryCommand hop le | Candidate chunk set | BR-FN-003 |
| Answer synthesis | Tong hop answer grounded tren chunk duoc chon | Retrieved context | AnswerObject | BR-FN-004 |
| Citation packaging | Dinh kem citation cho tung luan diem | Synthesized answer | CitationResource[] | BR-FN-007 |
| Response validation | Dam bao answer co nguon va disclaimer | Truoc response 200 | QueryResponse | BR-NF-002 |

- **Business Rules:**
  - `include_debug=false` la mac dinh va khong tra retrieval internals neu user khong yeu cau.
  - Neu context khong du, `insufficient_evidence=true` va answer phai noi ro thieu can cu.
  - So citation tra ve bi gioi han boi `max_citations` va phai giu duoc preview fields.
- **State Management:** Query la stateless request/response. Runtime state chi ton tai trong vong doi `QueryCommand -> QueryResult`.

## 4. SEQUENCE OF OPERATIONS

- **Primary Flow:** Frontend gui `QueryRequest` -> router validate -> QueryService tao normalized context -> SearchService lay candidate chunks va rerank -> AnswerAssembler tong hop answer + citations -> response formatter tra `QueryResponse`.
- **Alternate / Exception Flows:**
  - Validation fail -> 422 voi `ErrorEnvelope`.
  - Khong tim thay context du -> 200 voi `insufficient_evidence=true`.
  - Search/model timeout -> 504 voi `ErrorEnvelope`.
- **Diagram:** [LLD-SPAI-QUERY-2026-003-Sequence_Diagram.md](./LLD-SPAI-QUERY-2026-003-Sequence_Diagram.md)

## 5. COMPONENT & CLASS DESIGN

- **Component Overview:**
  - `QueryRouter`: public REST entrypoint.
  - `QueryService`: orchestration facade.
  - `FilterNormalizer`: chuyen API filter sang retrieval filter.
  - `AnswerAssembler`: build `AnswerObject` va citation list.
  - `ErrorFactory`: build `ErrorEnvelope`.
- **Design Patterns:** Service layer, adapter cho retrieval provider, presenter/assembler cho API response.
- **Class Diagram:** [LLD-SPAI-QUERY-2026-002-Class_Diagram.md](./LLD-SPAI-QUERY-2026-002-Class_Diagram.md)
- **Interfaces:**
  - `execute_query(request: QueryRequest) -> QueryResponse`
  - `normalize(filters: FilterObject | None) -> NormalizedFilters`
  - `assemble(result: RetrievalBundle, max_citations: int) -> QueryResponse`

## 6. INTERFACES & CONTRACTS

| Interface | Consumer | Provider | Protocol | DTO / Payload | Notes |
| --- | --- | --- | --- | --- | --- |
| `POST /api/v1/query` | Frontend workspace | FastAPI QueryRouter | REST | `QueryRequest`, `QueryResponse` | Source of truth: OpenAPI |
| `SearchService.search_for_query` | QueryService | Search module | In-process | `SearchRequestLike`, `SearchBundle` | No network boundary in MVP |
| `CitationHydration` | QueryService | Citation module | In-process | `CitationResource[]` | Preview contract bat buoc |

- **Backward Compatibility:** Them field moi vao response phai optional neu chua co frontend consumption; khong doi ten field da co trong OpenAPI.
- **Error Models:** `validation_error`, `auth_forbidden`, `upstream_timeout`, `internal_error`.

## 7. DATA DESIGN

- **Data Sources:** Qdrant payload chunks, PostgreSQL metadata, object storage preview artifacts.
- **Schemas:** Query module khong luu state nghiep vu; chi dung `QueryRequest`, `NormalizedFilters`, `QueryResponse`.
- **Data Flow:** User query -> normalized filters -> retrieval bundle -> synthesized answer -> API response.
- **Retention & Archiving:** Khong luu query history trong MVP. Chi log ky thuat voi request id.

## 8. ERROR HANDLING & RESILIENCE

- **Failure Modes:** malformed filters, upstream timeout, citation preview missing, unauthorized document access.
- **Fallbacks / Retries:** Khong retry model/search nhieu lan trong request path MVP; tra timeout ro rang thay vi silent retry.
- **Idempotency:** Query la read-only va idempotent o muc request semantics.
- **Monitoring Hooks:** log `request_id`, `query_length`, `citation_count`, `insufficient_evidence`, `latency_ms`.

## 9. SECURITY & PRIVACY CONTROLS

- **Authentication & Authorization:** bearer auth o gateway; user scope duoc truyen vao search filter.
- **Data Protection:** khong dua chunk khong duoc phep vao synthesis context.
- **Input Validation / Sanitisation:** Pydantic enforce schema; bo qua unknown fields.
- **Audit Logging:** log ky thuat gom request id, user id, endpoint, status code.
- **Threat Considerations:** prompt injection trong tai lieu duoc giam thieu bang retrieval-grounded answer only.

## 10. PERFORMANCE & SCALABILITY

- **Key Metrics:** p95 query latency < 5s o pilot, context_top_n <= 8, max_citations <= 20.
- **Capacity Planning:** QueryService stateless, co the horizontal scale doc lap voi ingestion.
- **Caching Strategy:** chua bat buoc trong MVP; co the them short-lived cache cho repeated query sau.
- **Load / Stress Considerations:** retrieval/rerank la bottleneck chinh; answer synthesis phai gioi han context size.

## 11. OBSERVABILITY & OPERATIONS

- **Logs:** structured JSON log voi `request_id`, `endpoint`, `latency_ms`, `result_count`.
- **Metrics:** query_count, query_latency_ms, insufficient_evidence_rate.
- **Tracing:** span `query.execute`, `query.search`, `query.answer`.
- **Feature Flags / Configuration:** `ENABLE_QUERY_DEBUG`, `DEFAULT_MAX_CITATIONS`.
- **Runbooks:** su dung AD va backend README cho local runbook MVP.

## 12. VERIFICATION & TESTABILITY

- **Unit Tests:** valid query, query with debug, query with filters, insufficient evidence response, validation error.
- **Integration Tests:** router -> service -> stub provider alignment voi OpenAPI.
- **Performance Tests:** smoke benchmark cho response builder va serialization.
- **Security Tests:** forbidden auth path, filter sanitization.
- **Traceability:** Query module cover BR-FN-003, BR-FN-004, BR-FN-007, BR-NF-002.

## 13. RISKS & OPEN ISSUES

| ID | Description | Impact | Mitigation / Action | Owner | Status |
| --- | --- | --- | --- | --- | --- |
| R-LLD-QUERY-001 | Query response de tro nen generic neu answer assembler khong ton trong evidence-first format | Medium | Dong bo formatter voi UI answer card | Backend | Open |
| R-LLD-QUERY-002 | Debug payload lo retrieval internals khong can thiet | Low | Chi bat khi `include_debug=true` | Backend | Open |

## 14. APPROVALS & CHANGE HISTORY

| Version | Date | Description | Author | Reviewer | Approved By |
| --- | --- | --- | --- | --- | --- |
| 1.0 | 2026-04-12 | Initial release | OpenAI Codex | Pending | Pending |
