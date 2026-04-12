# Module Design Specification

## DOCUMENT CONTROL

| Field | Value |
| --- | --- |
| **Document ID** | LLD-SPAI-DOCUMENT-2026-001 |
| **Template Version** | 1.0 |
| **Document Version** | 1.1 |
| **Project / Product** | Security Personal AI |
| **Module / Component** | Document Ingestion and Versioning |
| **Author** | OpenAI Codex, AI Implementation Draft |
| **Reviewer(s)** | Tech Lead, QA Lead, Security Lead |
| **Document Status** | Draft |
| **Classification** | Confidential |
| **Creation Date** | 2026-04-12 |
| **Last Updated** | 2026-04-12 |
| **AI-Assisted** | [x] Yes - Tool: **Codex** |

## 1. PURPOSE & SCOPE

- **Objective:** Dinh nghia logical document, mandatory versioning model, upload/index status va metadata toi thieu phuc vu repository tree, preview va retrieval; bao gom luong append version vao logical document hien huu.
- **In Scope:** `GET/POST /api/v1/documents`, `GET /api/v1/documents/{documentId}`, `GET /versions`, metadata schema document/chunk, version status lifecycle.
- **Out of Scope:** source connectors phuc tap, OCR pipeline chi tiet, retention automation, document compare workflow.

## 2. CONTEXT & ASSUMPTIONS

- **Dependencies:** object storage, metadata DB, vector store, ingestion worker, document router.
- **Assumptions & Constraints:** Moi logical document phai co it nhat mot version; upload moi tao `document_version_id` moi; logical `document_id` giu on dinh cho folder tree/UI references.

## 3. FUNCTIONAL DECOMPOSITION

| Capability | Description | Trigger | Output | Related Requirements |
| --- | --- | --- | --- | --- |
| Upload acceptance | Nhan file va tao ingestion job | `POST /documents` | `DocumentAcceptedResponse` | BR-FN-001 |
| Upload new version | Append version moi vao logical document hien huu | `POST /documents` + `document_id` | `DocumentAcceptedResponse` | BR-FN-001, BR-FN-007 |
| Document listing | Liet ke logical documents user nhin thay | `GET /documents` | `DocumentCollection` | BR-FN-001 |
| Document detail | Tra metadata logical document | `GET /documents/{id}` | `DocumentResource` | BR-FN-007 |
| Version listing | Tra danh sach version nhin thay | `GET /versions` | `DocumentVersionCollection` | BR-FN-007 |
| Version lifecycle | Quan ly accepted/indexing/indexed/... | ingestion pipeline | status fields | BR-NF-003 |

- **Business Rules:**
  - `document_id` dai dien logical document, khong doi khi co version moi.
  - `document_version_id` bat buoc duy nhat cho tung ingest/version.
  - Neu `POST /documents` co `document_id`, he thong phai append version moi vao logical document do, khong tao logical document moi.
  - Neu `document_id` duoc truyen ma khong ton tai, API phai tra loi `document_not_found`.
  - Chi mot version co `is_current_version=true`.
  - Version bi thay the phai giu lien ket `supersedes_version_id`; version current cu chuyen ve `is_current_version=false` va `parse_status=superseded`.
- **State Management:** Lifecycle version: `accepted -> indexing -> indexed` hoac `failed`; version cu co the thanh `superseded`, `withdrawn`, `invalidated`.

## 4. SEQUENCE OF OPERATIONS

- **Primary Flow:** upload file -> API tao accepted response + ingestion job -> worker parse/chunk/index -> cap nhat `document_versions` va `documents.current_version_id`.
- **Alternate / Exception Flows:** parse fail -> version `failed`; document bi thu hoi -> `withdrawn`; version cu bi thay the -> `superseded`.
- **Diagram:** [LLD-SPAI-DOCUMENT-2026-004-Sequence_Diagram.md](./LLD-SPAI-DOCUMENT-2026-004-Sequence_Diagram.md)

## 5. COMPONENT & CLASS DESIGN

- **Component Overview:** `DocumentRouter`, `DocumentService`, `DocumentRepository`, `VersioningPolicy`, `UploadPresenter`.
- **Design Patterns:** repository, policy object cho versioning, presenter cho API collection/resource.
- **Class Diagram:** [LLD-SPAI-DOCUMENT-2026-002-Class_Diagram.md](./LLD-SPAI-DOCUMENT-2026-002-Class_Diagram.md)
- **Interfaces:**
  - `list_documents(filters, page, limit) -> DocumentCollection`
  - `get_document(document_id) -> DocumentResource`
  - `list_versions(document_id) -> DocumentVersionCollection`
  - `accept_upload(file, metadata, document_id?) -> DocumentAcceptedResponse`

## 6. INTERFACES & CONTRACTS

| Interface | Consumer | Provider | Protocol | DTO / Payload | Notes |
| --- | --- | --- | --- | --- | --- |
| `GET /api/v1/documents` | Frontend left panel | FastAPI | REST | `DocumentCollection` | tree source |
| `POST /api/v1/documents` | Frontend upload | FastAPI | REST multipart | `DocumentAcceptedResponse` | async ingestion; `document_id` optional de append version |
| `GET /api/v1/documents/{documentId}` | Frontend | FastAPI | REST | `DocumentResource` | metadata detail |
| `GET /api/v1/documents/{documentId}/versions` | Frontend | FastAPI | REST | `DocumentVersionCollection` | version drawer/header |

- **Backward Compatibility:** `document_id`, `current_version_id`, `document_version_id` khong duoc doi nghia.
- **Error Models:** `resource_not_found`, `validation_error`, `preview_not_ready`, `auth_forbidden`.

## 7. DATA DESIGN

- **Data Sources:** PostgreSQL metadata tables, object storage, vector payload metadata.
- **Schemas:**
  - `documents`: `document_id`, `title`, `document_type`, `ticker`, `source`, `language`, `publication_date`, `current_version_id`, `access_level`, `index_status`.
  - `document_versions`: `document_version_id`, `document_id`, `version_label`, `publication_date`, `parse_status`, `supersedes_version_id`, `is_current_version`, `preview_manifest`.
  - `document_chunks`: `chunk_id`, `document_id`, `document_version_id`, `page_number`, `section_heading`, `snippet`, `preview_url`, `viewer_anchor`.
- **Data Flow:** upload metadata -> logical document resolution (create new or resolve existing by `document_id`) -> version row -> chunk rows.
- **Retention & Archiving:** Logical document co the giu nhieu version; khong xoa hard-delete trong MVP baseline.

## 8. ERROR HANDLING & RESILIENCE

- **Failure Modes:** duplicate upload, version mismatch, unknown `document_id` when append version, missing current version, parse fail.
- **Fallbacks / Retries:** parse/indexing retry nam ngoai request path; API chi tra accepted.
- **Idempotency:** Upload khong idempotent theo file binary, nhung `document_id` resolution phai xac dinh ro theo metadata.
- **Monitoring Hooks:** log upload accepted, version status transition, indexing failure.

## 9. SECURITY & PRIVACY CONTROLS

- **Authentication & Authorization:** Chi user duoc cap quyen moi xem document/version.
- **Data Protection:** object storage signed URL cho preview/download.
- **Input Validation / Sanitisation:** validate upload form fields va mime types.
- **Audit Logging:** upload actor, document_id, version_id, status transitions.
- **Threat Considerations:** preview URL phai short-lived va chi cho tai lieu duoc phep.

## 10. PERFORMANCE & SCALABILITY

- **Key Metrics:** upload acceptance < 500ms, list documents p95 < 500ms.
- **Capacity Planning:** document listing phai paginate.
- **Caching Strategy:** co the cache document list theo user scope sau nay; MVP khong bat buoc.
- **Load / Stress Considerations:** version list co the lon neu source upload lap lai nhieu lan.

## 11. OBSERVABILITY & OPERATIONS

- **Logs:** `document_upload_accepted`, `document_listed`, `version_listed`, `version_status_changed`.
- **Metrics:** upload_count, indexing_in_progress_count, indexing_failed_count.
- **Tracing:** `document.upload`, `document.list`, `document.versions`.
- **Feature Flags / Configuration:** `UPLOAD_MAX_SIZE_MB`, `PREVIEW_URL_TTL_MINUTES`.

## 12. VERIFICATION & TESTABILITY

- **Unit Tests:** upload response shape, append-version transition, document listing defaults, version list semantics, not found handling.
- **Integration Tests:** upload new doc -> accepted response; upload append version -> current version consistent.
- **Performance Tests:** list pagination smoke test.
- **Security Tests:** forbidden access to documents/versions.
- **Traceability:** Cover BR-FN-001, BR-FN-002, BR-FN-007, BR-NF-003.

## 13. RISKS & OPEN ISSUES

| ID | Description | Impact | Mitigation / Action | Owner | Status |
| --- | --- | --- | --- | --- | --- |
| R-LLD-DOC-001 | Logical document va version bi lon xon neu khong co policy ro | High | Enforce mandatory versioning policy trong service + tests | Backend | Mitigated in 1.1 |
| R-LLD-DOC-002 | Left tree khong du field de hien status/version | Medium | Giu `current_version_id`, `index_status` trong list endpoint | Backend | Open |

## 14. APPROVALS & CHANGE HISTORY

| Version | Date | Description | Author | Reviewer | Approved By |
| --- | --- | --- | --- | --- | --- |
| 1.1 | 2026-04-12 | Added append-version upload contract and version transition rules | OpenAI Codex | Pending | Pending |
| 1.0 | 2026-04-12 | Initial release | OpenAI Codex | Pending | Pending |
