# API Design

**Document ID:** API-SPAI-QSDC-2026-001  
**Template Version:** 1.0.0  
**Related Standards:** ISO/IEC/IEEE 42010, ISO/IEC 12207:2017 §6.4.4, ISO/IEC/IEEE 29148:2018, ISO/IEC 27001:2022, ISO/IEC 25010, PDPA (Singapore)

---

## Document Control

| Field | Value |
| --- | --- |
| **Service / Module** | Security Personal AI Query/Search/Document/Citation API |
| **API Type** | REST |
| **Document Version** | 0.1 Draft |
| **Status** | Draft |
| **Classification** | Confidential |
| **Author** | OpenAI Codex, AI API Draft |
| **Reviewers** | Architect, Backend Lead, Frontend Lead, QA, Security |
| **Creation Date** | 2026-04-12 |
| **Last Updated** | 2026-04-12 |
| **Approved By** | Pending |
| **Approval Date** | Pending |
| **Next Review Date** | 2026-04-26 |
| **AI-Assisted** | [x] Yes — Tool: **Codex** |

---

## ISO Traceability Matrix

| Clause / Control | Addressed In | Evidence |
| --- | --- | --- |
| ISO/IEC/IEEE 42010 §5 (Viewpoints/Concerns) | §4–§8 | Context, endpoint design, resource model |
| ISO/IEC 12207:2017 §6.4.4 (Architecture Definition) | Entire document | API contracts and lifecycle controls |
| ISO/IEC/IEEE 29148 §9 (Requirements) | §1, §6, §7, §9 | Requirement to contract mapping |
| ISO/IEC 27001:2022 Annex A (Security) | §8, §10, §12 | Auth, RBAC, logging, rate limits |
| ISO/IEC 25010 (Quality) | §9, §12, §14 | Performance, maintainability, verification |

---

## 1. Purpose & Scope

### 1.1 Purpose

Tài liệu này mô tả API contract cho các nhóm nghiệp vụ cốt lõi của Phase 1:

- nhận query và trả lời có citation,
- tìm kiếm tài liệu/chunk có filter,
- quản lý document registry và version,
- resolve citation và preview nguồn.

Mục tiêu là để frontend, backend, QA và security cùng build trên một contract thống nhất. Theo `OpenAPI_Guide.md`, OpenAPI spec là source of truth. Tài liệu này là API design baseline, còn schema cuối cùng phải được materialize thành OpenAPI spec từ đúng contract bên dưới.

### 1.2 Scope

- **In Scope:** `Query API`, `Search API`, `Document API`, `Citation API`, auth model ở mức endpoint, validation rules, error envelope, rate limits, observability fields.
- **Out of Scope:** authentication provider internals, query history API, analytics API, workspace API, watchlist API, feedback analytics API, compare/timeline workflows mức Phase 2.
- **Assumptions:** path versioning dùng `/api/v1`, bearer auth đã có từ identity provider, backend implementation dùng FastAPI, orchestration dùng LangGraph, retrieval dùng Qdrant + PostgreSQL + sparse retrieval adapter.

### 1.3 MVP Boundary

#### Required for MVP

- `POST /api/v1/query`
- `POST /api/v1/search`
- `GET /api/v1/documents`
- `POST /api/v1/documents`
- `GET /api/v1/documents/{documentId}`
- `GET /api/v1/documents/{documentId}/versions`
- `GET /api/v1/documents/{documentId}/versions/{versionId}/preview/{pageNumber}`
- `GET /api/v1/citations/{citationId}`
- Bearer auth
- Access control at document/version/citation/preview level
- Citation payload đủ để frontend mở đúng nguồn
- Structured logs + `request_id`

#### Nice to Have Later

- `GET /api/v1/documents/{documentId}/versions/{versionId}` như endpoint riêng nếu UI chưa cần màn hình detail version
- `options.include_debug` trong query response
- score breakdown (`dense`, `sparse`, `rerank`) trong search results cho production UI
- `Idempotency-Key` cho upload
- signed preview URLs nếu MVP đang dùng protected API redirect nội bộ
- advanced filter dimensions như `sector`, `market`, `reporting_period` nếu dataset MVP chưa cần
- rich observability fields vượt ngoài Langfuse + app logs
### 1.4 Objectives & Success Metrics

- Frontend gọi được query/search/document/citation APIs mà không cần contract phụ ngoài OpenAPI spec.
- Query API trả grounded answer với citation object đầy đủ cho preview.
- Search API hỗ trợ filter theo `ticker`, `document_type`, `date range`, `source`, `language`, `access scope`.
- Document API support version-aware retrieval và preview.
- P95 latency cho `POST /api/v1/query` với truy vấn phổ biến trong pilot dataset phải dưới 5 giây.

---

## 2. Definitions & References

| Term | Definition |
| --- | --- |
| Query | Một request hỏi đáp ngôn ngữ tự nhiên trên document corpus |
| Search | Một request tìm document/chunk mà chưa bắt buộc synthesis answer |
| Citation | Liên kết có cấu trúc từ answer tới document version, page, chunk và snippet |
| Logical Document | Thực thể tài liệu ổn định theo business identity |
| Document Version | Một bản cụ thể của logical document tại thời điểm ingest |
| Preview Artifact | Rendered view để UI mở đúng page/chunk |

| Reference | Location | Notes |
| --- | --- | --- |
| OpenAPI Guide | `/Users/steve/development/mercury/security-personal-ai/doc/02-Architecture/API/OpenAPI_Guide.md` | OpenAPI is source of truth |
| Architecture Design | `/Users/steve/development/mercury/security-personal-ai/doc/02-Architecture/AD/AD-SPAI-2026-001-Architecture_Design.md` | Phase 1 architecture baseline |
| BRD | `/Users/steve/development/mercury/security-personal-ai/doc/01-Requirements/BRD/BRD-SPAI-2026-001-Personal_AI_Agent_For_Stock_Expert.md` | Business drivers and scope |
| API Template | `/Users/steve/development/mercury/security-personal-ai/doc/02-Architecture/API/TEMPLATE-ARCH-102-API_Design.md` | Document template |
| Security Plan | `/Users/steve/development/mercury/security-personal-ai/doc/02-Architecture/Security_Privacy/` | Pending detailed controls |

---

## 3. Stakeholders, Roles & RACI

| Stakeholder | Role | Responsibilities | RACI (R/A/C/I) | Review Status |
| --- | --- | --- | --- | --- |
| Product Owner | Business owner | Approves scope and response semantics | A | Pending |
| Solution Architect | Architecture owner | Approves API boundaries and resource model | A | Pending |
| Backend Engineer | Service implementer | Implements endpoints, validation, authz, logging | R | Pending |
| Frontend Engineer | Consumer | Implements UI contract, pagination, preview integration | C | Pending |
| QA Lead | Verification | Contract tests, click-through preview validation | R | Pending |
| Security Officer | Security review | Reviews auth, RBAC, logging, retention | C | Pending |
| DevOps | Runtime owner | Deploys, monitors, rate limits, logs | C | Pending |
| AI Agent (Codex) | Drafting support | Initial contract authoring | I | Complete |

---

## 4. System Context & Dependencies

### 4.1 Context

Web UI gọi FastAPI. FastAPI xác thực user, áp access scope, gọi orchestrator và data services. Query/search response phụ thuộc vào:

- PostgreSQL cho document registry, version metadata, access control.
- Qdrant cho dense vector retrieval.
- Sparse retrieval adapter cho keyword/BM25 or sparse-vector retrieval.
- Object storage cho file gốc và preview artifacts.

### 4.2 Integrations & Upstream/Downstream Services

| System | Interaction Type | Direction | Protocol | Notes |
| --- | --- | --- | --- | --- |
| Identity Provider | Authentication / claims | Inbound | OIDC/OAuth2 | Bearer token validation |
| Orchestrator Service | Query execution | Outbound | Internal HTTP / RPC | LangGraph flow |
| PostgreSQL | Metadata lookup | Outbound | SQL | Registry, version, permissions |
| Qdrant | Dense retrieval | Outbound | HTTP/gRPC | Chunk embeddings and payload |
| Sparse Retrieval Service | Keyword retrieval | Outbound | Internal HTTP / library call | BM25 or sparse vector |
| Object Storage | Preview/file access | Outbound | HTTPS/S3 API | Original files, preview artifacts |

### 4.3 Constraints

- API phải versioned bằng path `/api/v1`.
- OpenAPI spec là source of truth, examples trong tài liệu này phải được reflected trong spec.
- Query runtime không được trả citation thiếu `document_version_id`.
- Query history không được persist thành user-facing API trong Phase 1.

---

## 5. Resource Model & Domain Overview

### 5.1 Domain Summary

Tài liệu này định nghĩa 4 resource group:

- `QueryExecution`, trả synthesized answer + citations.
- `SearchResult`, trả tài liệu/chunk phù hợp cho người dùng duyệt nguồn.
- `Document` và `DocumentVersion`, quản lý registry, listing, status, preview.
- `Citation`, resolve metadata và preview anchor từ một citation cụ thể.

### 5.2 Resource Relationships

- Một `Document` có nhiều `DocumentVersion`.
- Một `DocumentVersion` có nhiều `Chunk`.
- Một `QueryExecution` có nhiều `Citation`.
- Một `Citation` luôn tham chiếu đúng một `DocumentVersion` và một `Chunk`.

### 5.3 Field Dictionary (High-level)

| Resource | Field | Description | Type | Sensitive? | Notes |
| --- | --- | --- | --- | --- | --- |
| Document | `document_id` | Logical document ID | string | No | Stable across versions |
| DocumentVersion | `document_version_id` | Exact indexed version | string | No | Mandatory in citations |
| SearchResult | `snippet` | Matching excerpt | string | Potentially yes | Must honor access control |
| Citation | `preview_url` | URL for preview artifact | string | No | Must be scoped by auth |
| QueryExecution | `answer.summary` | Short grounded answer | string | Potentially yes | Generated from retrieved context |

---

## 6. Endpoint Catalogue & Contracts

### 6.1 Endpoint Summary

| Endpoint | Method | Purpose | Auth | RBAC | Request Schema | Response Schema |
| --- | --- | --- | --- | --- | --- | --- |
| `/api/v1/query` | POST | Execute grounded query with synthesis and citations | Bearer | Any authenticated user with corpus access | `QueryRequest` | `QueryResponse` |
| `/api/v1/search` | POST | Search documents/chunks without synthesis | Bearer | Any authenticated user with corpus access | `SearchRequest` | `SearchResponse` |
| `/api/v1/documents` | GET | List documents visible to caller | Bearer | Scoped by access policy | `ListDocumentsRequest` | `DocumentCollection` |
| `/api/v1/documents` | POST | Upload document for ingestion | Bearer | Authorized uploader/admin | `multipart/form-data` | `DocumentAcceptedResponse` |
| `/api/v1/documents/{documentId}` | GET | Get logical document details | Bearer | Scoped by access policy | Path | `DocumentResource` |
| `/api/v1/documents/{documentId}/versions` | GET | List versions of a document | Bearer | Scoped by access policy | Path | `DocumentVersionCollection` |
| `/api/v1/documents/{documentId}/versions/{versionId}` | GET | Get exact version details | Bearer | Scoped by access policy | Path | `DocumentVersionResource` |
| `/api/v1/documents/{documentId}/versions/{versionId}/preview/{pageNumber}` | GET | Open preview artifact for a page | Bearer | Scoped by access policy | Path | `PreviewResource` |
| `/api/v1/citations/{citationId}` | GET | Resolve a citation for UI preview | Bearer | Scoped by originating access policy | Path | `CitationResource` |

#### MVP endpoint classification

| Endpoint | Phase |
| --- | --- |
| `POST /api/v1/query` | Required for MVP |
| `POST /api/v1/search` | Required for MVP |
| `GET /api/v1/documents` | Required for MVP |
| `POST /api/v1/documents` | Required for MVP |
| `GET /api/v1/documents/{documentId}` | Required for MVP |
| `GET /api/v1/documents/{documentId}/versions` | Required for MVP |
| `GET /api/v1/documents/{documentId}/versions/{versionId}/preview/{pageNumber}` | Required for MVP |
| `GET /api/v1/citations/{citationId}` | Required for MVP |
| `GET /api/v1/documents/{documentId}/versions/{versionId}` | Nice to have later |

### 6.2 Detailed Endpoint Specification

#### 6.2.1 `POST /api/v1/query`

- **Description:** Execute a Phase 1 query-first RAG request. Backend shall apply access filtering, hybrid retrieval, rerank, synthesis, and citation packaging.
- **Request Headers:**
  - `Authorization: Bearer <token>`
  - `X-Request-Id: <uuid>` optional, server generates one if absent
- **Request Body Schema:** `QueryRequest`
- **Request Example:**

```json
{
  "query": "Rủi ro lớn nhất của HPG trong 2024 là gì?",
  "filters": {
    "ticker": ["HPG"],
    "document_type": ["annual_report", "research_report"],
    "date_from": "2024-01-01",
    "date_to": "2024-12-31"
  },
  "options": {
    "include_debug": false,
    "max_citations": 8
  }
}
```

- **Response Body Schema:** `QueryResponse`
- **Response Example:**

```json
{
  "request_id": "0f3e41b0-78d3-4ff2-8d2f-5b2f1c8279ab",
  "query": "Rủi ro lớn nhất của HPG trong 2024 là gì?",
  "filters": {
    "ticker": ["HPG"],
    "document_type": ["annual_report", "research_report"],
    "date_from": "2024-01-01",
    "date_to": "2024-12-31"
  },
  "answer": {
    "summary": "Ba nhóm rủi ro nổi bật là nhu cầu thép phục hồi chậm, biến động giá nguyên liệu và áp lực dòng tiền từ đầu tư lớn.",
    "confidence": "medium",
    "insufficient_evidence": false,
    "disclaimer": "Không coi đây là khuyến nghị đầu tư."
  },
  "citations": [
    {
      "citation_id": "cit_001",
      "document_id": "doc_hpg_ar_2024",
      "document_version_id": "docver_hpg_ar_2024_v1",
      "title": "HPG Annual Report 2024",
      "source": "internal_repository",
      "document_type": "annual_report",
      "page_number": 87,
      "section_heading": "Risk Factors",
      "chunk_id": "chk_009182",
      "snippet": "Bien dong gia quang sat va than coc co the anh huong den bien loi nhuan gop...",
      "text_offset_start": 18240,
      "text_offset_end": 18410,
      "preview_url": "/api/v1/documents/doc_hpg_ar_2024/versions/docver_hpg_ar_2024_v1/preview/87",
      "viewer_anchor": "page=87&chunk=chk_009182",
      "version_label": "v1",
      "confidence": 0.91
    }
  ],
  "debug": null
}
```

- **Behaviour / Rules:**
  - Must reject empty query after trim.
  - Must enforce access filter before retrieval.
  - Must include `document_version_id` in every citation.
  - Must return `insufficient_evidence=true` when evidence is not enough.
  - Must not persist query history as user-facing resource in Phase 1.

#### 6.2.2 `POST /api/v1/search`

- **Description:** Retrieve matching documents/chunks without answer synthesis.
- **Request Body Schema:** `SearchRequest`
- **Request Example:**

```json
{
  "query": "trai phieu covenant impairment",
  "filters": {
    "ticker": ["SSI"],
    "document_type": ["annual_report", "research_report"],
    "language": ["vi", "en"]
  },
  "page": 1,
  "limit": 20
}
```

- **Response Example:**

```json
{
  "request_id": "eb1df090-df59-4a54-8500-cf94dd2ddab7",
  "query": "trai phieu covenant impairment",
  "page": 1,
  "limit": 20,
  "total": 52,
  "results": [
    {
      "result_type": "chunk",
      "document_id": "doc_ssi_ar_2023",
      "document_version_id": "docver_ssi_ar_2023_v1",
      "title": "SSI Annual Report 2023",
      "document_type": "annual_report",
      "ticker": "SSI",
      "publication_date": "2024-03-28",
      "page_number": 134,
      "section_heading": "Borrowings and Bonds",
      "chunk_id": "chk_1102",
      "snippet": "Tap doan co cac dieu khoan rang buoc lien quan den cac khoan vay...",
      "preview_url": "/api/v1/documents/doc_ssi_ar_2023/versions/docver_ssi_ar_2023_v1/preview/134",
      "viewer_anchor": "page=134&chunk=chk_1102",
      "scores": {
        "dense": 0.82,
        "sparse": 13.4,
        "rerank": 0.91
      }
    }
  ]
}
```

- **Behaviour / Rules:**
  - Search results may include document-level and chunk-level hits, but response must label `result_type`.
  - Search endpoint shall support pagination.
  - Search endpoint shall not synthesize an answer field.

#### 6.2.3 `GET /api/v1/documents`

- **Description:** List documents visible to the caller with filtering and pagination.
- **Query Parameters:**
  - `ticker`
  - `document_type`
  - `source`
  - `language`
  - `date_from`
  - `date_to`
  - `page`
  - `limit`
- **Response Example:**

```json
{
  "page": 1,
  "limit": 20,
  "total": 2,
  "data": [
    {
      "document_id": "doc_hpg_ar_2024",
      "title": "HPG Annual Report 2024",
      "document_type": "annual_report",
      "ticker": "HPG",
      "source": "internal_repository",
      "language": "vi",
      "publication_date": "2025-03-29",
      "current_version_id": "docver_hpg_ar_2024_v1",
      "access_level": "internal",
      "index_status": "indexed"
    }
  ]
}
```

#### 6.2.4 `POST /api/v1/documents`

- **Description:** Upload a document and create an ingestion job.
- **Content Type:** `multipart/form-data`
- **Form Fields:**
  - `file` required
  - `document_type` optional but recommended
  - `ticker` optional
  - `company_name` optional
  - `publication_date` optional
  - `source` optional
- **Response Example:**

```json
{
  "document_id": "doc_new_001",
  "document_version_id": "docver_new_001_v1",
  "index_job_id": "job_7751",
  "status": "accepted"
}
```

- **Behaviour / Rules:**
  - Upload does not mean searchable immediately.
  - Response shall return `202 Accepted` when async ingestion is started.

#### 6.2.5 `GET /api/v1/documents/{documentId}`

- **Description:** Return logical document details, current version pointer, and indexing state.

#### 6.2.6 `GET /api/v1/documents/{documentId}/versions`

- **Description:** Return all visible versions for a logical document.
- **Behaviour / Rules:**
  - Must include `is_current_version`.
  - Must include supersede relationship where available.

#### 6.2.7 `GET /api/v1/documents/{documentId}/versions/{versionId}`

- **Description:** Return exact version metadata and ingestion/index status.
- **Behaviour / Rules:**
  - Must 404 when the version does not belong to the provided document.

#### 6.2.8 `GET /api/v1/documents/{documentId}/versions/{versionId}/preview/{pageNumber}`

- **Description:** Resolve a preview resource for a page in a specific document version.
- **Response Example:**

```json
{
  "document_id": "doc_hpg_ar_2024",
  "document_version_id": "docver_hpg_ar_2024_v1",
  "page_number": 87,
  "mime_type": "application/pdf",
  "preview_url": "https://signed.example.com/preview/doc_hpg_ar_2024/v1/page/87",
  "viewer_anchor": "page=87",
  "expires_at": "2026-04-12T10:30:00Z"
}
```

#### 6.2.9 `GET /api/v1/citations/{citationId}`

- **Description:** Resolve a citation object for UI click-through or rehydration.
- **Behaviour / Rules:**
  - Citation lookup shall validate that the caller still has access to the underlying document version.
  - If the source version is superseded, response must still include `version_label` and current-version hint.

### 6.3 Payload Schemas

#### `QueryRequest`

| Field | Type | Required | Notes |
| --- | --- | --- | --- |
| `query` | string | Yes | 1..4000 chars after trim |
| `filters` | object | No | Metadata filters |
| `options.include_debug` | boolean | No | Default `false` |
| `options.max_citations` | integer | No | Default 8, max 20 |

**MVP required fields:** `query`  
**Nice to have later:** `options.include_debug`

#### `SearchRequest`

| Field | Type | Required | Notes |
| --- | --- | --- | --- |
| `query` | string | Yes | 1..4000 chars |
| `filters` | object | No | Same filter model as query |
| `page` | integer | No | Default 1 |
| `limit` | integer | No | Default 20, max 100 |

**MVP required fields:** `query`  
**MVP recommended:** `filters.ticker`, `filters.document_type`, `date_from`, `date_to`, `page`, `limit`

#### `FilterObject`

| Field | Type | Required | Notes |
| --- | --- | --- | --- |
| `ticker` | string[] | No | Example `["HPG"]` |
| `document_type` | string[] | No | Enum values controlled in OpenAPI |
| `source` | string[] | No | Source registry values |
| `language` | string[] | No | ISO-like codes, e.g. `vi`, `en` |
| `date_from` | date | No | Inclusive lower bound |
| `date_to` | date | No | Inclusive upper bound |
| `reporting_period` | string[] | No | Example `["FY2024"]` |
| `sector` | string[] | No | Example `["steel"]` |
| `market` | string[] | No | Example `["HOSE"]` |

**Required for MVP filter set:**

- `ticker`
- `document_type`
- `date_from`
- `date_to`
- `source`
- `language`

**Nice to have later filter set:**

- `reporting_period`
- `sector`
- `market`

#### `CitationResource`

| Field | Type | Required | Notes |
| --- | --- | --- | --- |
| `citation_id` | string | Yes | Stable within response scope |
| `document_id` | string | Yes | Logical document ID |
| `document_version_id` | string | Yes | Exact version |
| `title` | string | Yes | Display title |
| `source` | string | Yes | Source registry key |
| `document_type` | string | Yes | Business doc type |
| `page_number` | integer | Conditional | Required if page-mapped |
| `section_heading` | string | No | For preview context |
| `chunk_id` | string | Yes | Chunk reference |
| `snippet` | string | Yes | Safe preview snippet |
| `text_offset_start` | integer | No | Present when canonical offsets exist |
| `text_offset_end` | integer | No | Present when canonical offsets exist |
| `preview_url` | string | No | Signed URL or API URL |
| `viewer_anchor` | string | No | UI anchor/hint |
| `version_label` | string | Yes | Example `v1`, `amended-2` |
| `confidence` | number | No | 0..1 |

**MVP required citation fields:** `citation_id`, `document_id`, `document_version_id`, `title`, `source`, `document_type`, `chunk_id`, `snippet`, `version_label`  
**MVP strongly recommended:** `page_number`, `preview_url`, `viewer_anchor`  
**Nice to have later:** `text_offset_start`, `text_offset_end`, `confidence`

---

## 7. Business Rules & Validation

| Rule ID | Statement | Applies To | Enforcement | Source |
| --- | --- | --- | --- | --- |
| BR-QRY-001 | Query request shall reject empty or whitespace-only `query` | `POST /query`, `POST /search` | JSON validation + service layer | AD v0.3 |
| BR-QRY-002 | Query synthesis shall only use candidates after access-filtered hybrid retrieval and rerank | `POST /query` | Orchestrator contract | AD v0.3 |
| BR-CIT-001 | Every citation shall include `document_version_id` | `POST /query`, `GET /citations/{citationId}` | Response validator | AD v0.3 |
| BR-DOC-001 | Upload creates a new document version, never destructive overwrite | `POST /documents` | Ingestion service | AD v0.3 |
| BR-DOC-002 | Version preview request shall fail if `versionId` does not belong to `documentId` | `GET /documents/{documentId}/versions/{versionId}` | Service layer check | Data integrity |
| BR-SEC-001 | Caller shall only see documents, versions, chunks and citations within current access scope | All endpoints | Authz middleware + SQL filters + retrieval payload filter | Security baseline |
| BR-SCH-001 | Search endpoint shall not return synthesized answer field | `POST /search` | Schema contract | API design decision |

#### MVP rules that must ship now

- `BR-QRY-001`
- `BR-QRY-002`
- `BR-CIT-001`
- `BR-DOC-001`
- `BR-SEC-001`
- `BR-SCH-001`

#### Nice to have later

- `BR-DOC-002` as explicit standalone version-detail flow if UI MVP does not expose per-version screen yet

---

## 8. Security & Privacy Controls

### 8.1 Authentication

- Method: Bearer token from OIDC/OAuth2 compatible identity provider.
- Every protected endpoint must validate token signature, expiry and required claims.
- Anonymous access is out of scope for Phase 1.

### 8.2 Authorization & RBAC

- Minimum model: role + document access scope + access level.
- Authorization shall be enforced at:
  - document listing,
  - version listing,
  - citation resolve,
  - preview resolve,
  - retrieval candidate generation.

### 8.3 Data Protection

- Preview URLs should be signed, short-lived URLs or protected API redirects.
- Logs shall not store raw bearer tokens.
- Logs should avoid full sensitive chunk content unless explicitly whitelisted for secure debug mode.

### 8.4 Threat Model Summary

- Main threats: unauthorized preview access, citation leakage across users, oversized uploads, prompt leakage from unauthorized chunks, IDOR on document/version endpoints.
- Mitigations: scoped authz checks, signed URLs, schema validation, upload size limits, retrieval-level authorization, request logging with request ID.

### 8.5 Compliance Notes

- Query history is not exposed as API resource in Phase 1.
- Citation and preview access must be traceable for audit.
- Data retention for technical logs must be handled separately from user-facing history.

---

## 9. Non-Functional Requirements

| Attribute | Target | Measurement Method | Architecture Strategy |
| --- | --- | --- | --- |
| Query Performance | P95 < 5s on common pilot queries | Load test + tracing | Candidate budget, rerank cap, async orchestration |
| Search Performance | P95 < 2s on filtered search | Load test | Indexed filters, pagination |
| Availability | ≥ 99.5% monthly | Monitoring dashboard | Managed services + retries |
| Maintainability | Contract-first via OpenAPI | Contract tests | OpenAPI source of truth |
| Security | Zero unauthorized citation/preview access in test suite | Security and authz tests | Central authz checks |
| Observability | 100% requests with `request_id` | Log audit | Structured logging |

---

## 10. Error Handling & Status Codes

### 10.1 Standard Error Envelope

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "query must not be empty",
    "details": [
      {
        "field": "query",
        "issue": "required"
      }
    ],
    "request_id": "0f3e41b0-78d3-4ff2-8d2f-5b2f1c8279ab"
  }
}
```

### 10.2 Error Catalogue

| Code | HTTP Status | Description | Retryable? | Logged As | Notes |
| --- | --- | --- | --- | --- | --- |
| `AUTH_INVALID_TOKEN` | 401 | Missing or invalid token | No | Warn | Re-auth required |
| `AUTH_FORBIDDEN` | 403 | Caller lacks access to resource | No | Warn | Includes document/version/citation denial |
| `VALIDATION_ERROR` | 422 | Request schema invalid | No | Info | Includes field-level details |
| `RESOURCE_NOT_FOUND` | 404 | Document, version, citation not found | No | Info | Avoid leaking hidden resource existence |
| `PREVIEW_NOT_READY` | 409 | Preview artifact not available yet | Yes | Info | User may retry later |
| `RATE_LIMIT_EXCEEDED` | 429 | Quota exceeded | Yes | Info | Retry after backoff |
| `UPSTREAM_TIMEOUT` | 504 | Retrieval/model dependency timeout | Yes | Error | Trace provider |
| `INTERNAL_ERROR` | 500 | Unhandled server error | Possibly | Error | Include request ID |

---

## 11. Rate Limiting, Quotas & Idempotency

| Endpoint | Limit | Dimension | Idempotency | Notes |
| --- | --- | --- | --- | --- |
| `POST /api/v1/query` | 60 req/min | token | Not required | Protect expensive synthesis path |
| `POST /api/v1/search` | 120 req/min | token | Not required | Search is cheaper than query |
| `POST /api/v1/documents` | 20 req/hour | token | Optional `Idempotency-Key` recommended | Large uploads, async ingestion |
| `GET /api/v1/documents/*/preview/*` | 300 req/min | token | N/A | High-frequency viewer interaction |

- MVP does not require `Idempotency-Key`, but backend should support it later to avoid duplicate ingestion on retries.
- Retry policy for `429` and `504`: exponential backoff with jitter.

---

## 12. Observability & Operational Logging

| Aspect | Approach | Tooling / Owner |
| --- | --- | --- |
| Logging | JSON logs with `request_id`, `actor_id`, `document_id`, `document_version_id`, `endpoint`, `status_code` | Backend + centralized logs |
| Metrics | Query latency, search latency, preview latency, upload acceptance rate, citation coverage | Prometheus/Grafana or equivalent |
| Tracing | Trace request through API, retrieval, rerank, synthesis | Langfuse + OpenTelemetry |
| Alerting | 5xx spike, preview failures, upstream timeouts, authz denial anomalies | Ops rotation |

**Required log fields per query/search request:**

- `request_id`
- `user_id`
- `endpoint`
- `filters_applied`
- `retrieval_strategy`
- `status_code`
- `latency_ms`

#### Required for MVP

- structured JSON logs
- `request_id`
- latency logging
- Langfuse traces for query path

#### Nice to have later

- centralized metrics stack
- dedicated alert routing
- richer per-endpoint dashboards

---

## 13. Lifecycle Management & Versioning

- **Versioning Scheme:** path-based `/api/v1`.
- **Backward Compatibility Policy:** additive response fields are allowed in `v1`; breaking contract changes require new API version.
- **Document Version Policy:** logical document and document version are separate resources. Query/search/citation responses must always carry exact `document_version_id`.
- **OpenAPI Policy:** every breaking or additive change must first update the OpenAPI spec, then SDKs/examples generated from that spec.

---

## 14. Testing & Verification Plan

| Test Type | Scope | Tooling | Owner | Status |
| --- | --- | --- | --- | --- |
| Unit Tests | Validation and service rules | pytest | Backend Engineer | Required |
| Contract Tests | Request/response against OpenAPI | Schemathesis / Dredd / Prism | QA | Required |
| Integration Tests | Query/search with retrieval stubs or pilot dataset | pytest + test fixtures | Backend Engineer | Required |
| Security Tests | Authz, IDOR, signed preview URL access | automated tests + review | Security | Required |
| Preview Click-through Tests | Page/chunk accuracy across PDF and non-PDF | QA automation/manual | QA | Required |
| Performance Tests | Query/search/preview budgets | k6 | DevOps | Required before release |

Release readiness minimum:

- 0 open high-severity API contract defects.
- 0 unauthorized access findings.
- Contract tests passing against current OpenAPI spec.

---

## 15. Compliance & Data Protection Checklist

- [ ] OpenAPI spec created and treated as source of truth.
- [ ] Query/search/document/citation schemas reflected in spec and examples.
- [ ] PII and confidential fields classified.
- [ ] Preview URL access control validated.
- [ ] Data retention for technical logs documented.
- [ ] Access controls reviewed with Security.
- [ ] API documentation published to internal developer portal or repo docs.

---

## 16. Change Log

| Version | Date | Author | Summary |
| --- | --- | --- | --- |
| 0.1 | 2026-04-12 | OpenAI Codex | Initial API design for Query/Search/Document/Citation Phase 1 |

---

## 17. Approvals

| Role | Name | Signature | Date |
| --- | --- | --- | --- |
| Architect / Tech Lead (Approve) | Pending | Pending | Pending |
| Product Owner (Approve) | Pending | Pending | Pending |
| Security Officer (Concur) | Pending | Pending | Pending |
| QA Lead (Concur) | Pending | Pending | Pending |
| DevOps Lead (Concur) | Pending | Pending | Pending |

---

**Distribution:** Store in `/02-Architecture/API/`. Next step is to create the matching OpenAPI spec and treat that spec as the source of truth for SDK generation and endpoint examples.
