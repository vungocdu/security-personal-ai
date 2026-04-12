# Module Design Specification

## DOCUMENT CONTROL

| Field | Value |
| --- | --- |
| **Document ID** | LLD-SPAI-CITATION-2026-001 |
| **Template Version** | 1.0 |
| **Document Version** | 1.1 |
| **Project / Product** | Security Personal AI |
| **Module / Component** | Citation Preview and Source Verification |
| **Author** | OpenAI Codex, AI Implementation Draft |
| **Reviewer(s)** | Tech Lead, QA Lead, Security Lead |
| **Document Status** | Draft |
| **Classification** | Confidential |
| **Creation Date** | 2026-04-12 |
| **Last Updated** | 2026-04-12 |
| **AI-Assisted** | [x] Yes - Tool: **Codex** |

## 1. PURPOSE & SCOPE

- **Objective:** Dinh nghia citation preview contract va cac endpoint giup frontend mo dung tai lieu/version/page/anchor de kiem chung evidence.
- **In Scope:** `GET /api/v1/citations/{citationId}`, `GET /preview/{pageNumber}`, preview payload, source verification behavior, signed preview URL semantics.
- **Out of Scope:** annotation, comment thread, in-document compare, OCR correction.

## 2. CONTEXT & ASSUMPTIONS

- **Dependencies:** Document module, object storage previews, citation metadata mapping, frontend evidence panel.
- **Assumptions & Constraints:** Citation payload phai du de frontend hydrate right panel ma khong can query them field ngoai contract; preview resource co the PDF/Word/Excel.

## 3. FUNCTIONAL DECOMPOSITION

| Capability | Description | Trigger | Output | Related Requirements |
| --- | --- | --- | --- | --- |
| Citation hydration | Lay chi tiet citation | click citation chip | `CitationResource` | BR-FN-007 |
| Preview resolution | Resolve preview URL cho page/version | open preview | `PreviewResource` | BR-FN-007, BR-FN-002 |
| Source verification | Dam bao citation tro dung document/page/chunk | response build | preview contract | BR-NF-002 |

- **Business Rules:**
  - Citation bat buoc co `document_id`, `document_version_id`, `chunk_id`, `version_label`.
  - Preview resolver phai xac thuc `document_version_id` thuoc `document_id` truoc khi tra URL.
  - Neu version ton tai nhung chua o trang thai co the preview (`accepted`, `indexing`, `failed`) thi phai tra `409 preview_not_ready`.
  - Neu co preview thi phai tra `preview_url`; neu khong co phai tra `409 PreviewNotReady` hoac field nullable tuy endpoint.
  - `viewer_anchor` duoc dung de scroll/highlight page/chunk trong viewer.
- **State Management:** Citation la read-only lookup; preview resource co TTL thong qua `expires_at`.

## 4. SEQUENCE OF OPERATIONS

- **Primary Flow:** User click citation chip -> frontend goi `GET /citations/{id}` neu can hydrate -> goi preview endpoint -> render viewer.
- **Alternate / Exception Flows:** preview artifact chua san sang -> 409; citation khong ton tai -> 404.
- **Diagram:** [LLD-SPAI-CITATION-2026-003-Sequence_Diagram.md](./LLD-SPAI-CITATION-2026-003-Sequence_Diagram.md)

## 5. COMPONENT & CLASS DESIGN

- **Component Overview:** `CitationRouter`, `CitationService`, `PreviewService`, `PreviewUrlSigner`, `CitationMapper`.
- **Design Patterns:** mapper/presenter cho payload, service layer cho preview resolution.
- **Class Diagram:** [LLD-SPAI-CITATION-2026-002-Class_Diagram.md](./LLD-SPAI-CITATION-2026-002-Class_Diagram.md)
- **Interfaces:**
  - `get_citation(citation_id: str) -> CitationResource`
  - `get_preview(document_id: str, version_id: str, page_number: int) -> PreviewResource`

## 6. INTERFACES & CONTRACTS

| Interface | Consumer | Provider | Protocol | DTO / Payload | Notes |
| --- | --- | --- | --- | --- | --- |
| `GET /api/v1/citations/{citationId}` | Frontend right panel | FastAPI | REST | `CitationResource` | hydration on demand |
| `GET /api/v1/documents/{documentId}/versions/{versionId}/preview/{pageNumber}` | Frontend viewer | FastAPI | REST | `PreviewResource` | preview resolver |

- **Backward Compatibility:** `viewer_anchor` va `preview_url` la fields UI-critical; khong duoc doi semantics.
- **Error Models:** `resource_not_found`, `preview_not_ready`, `auth_forbidden`.

## 7. DATA DESIGN

- **Data Sources:** citation mapping metadata, document versions, preview manifest.
- **Schemas:**
  - Citation toi thieu: `citation_id`, `document_id`, `document_version_id`, `title`, `source`, `document_type`, `page_number`, `section_heading`, `chunk_id`, `snippet`, `preview_url`, `viewer_anchor`, `version_label`, `confidence`.
  - Preview toi thieu: `document_id`, `document_version_id`, `page_number`, `mime_type`, `preview_url`, `viewer_anchor`, `expires_at`.
- **Data Flow:** answer/search result -> citation click -> citation detail -> preview resource -> viewer.
- **Retention & Archiving:** preview artifacts co the duoc rotate; citation ids phai on dinh voi version.

## 8. ERROR HANDLING & RESILIENCE

- **Failure Modes:** preview artifact missing, expired signed URL, citation mapping stale, document/version mismatch.
- **Fallbacks / Retries:** frontend co the re-request preview endpoint de lay signed URL moi; citation detail van hien snippet neu preview chua san sang.
- **Idempotency:** GET endpoints read-only.
- **Monitoring Hooks:** log preview_resolved, preview_not_ready, citation_not_found.

## 9. SECURITY & PRIVACY CONTROLS

- **Authentication & Authorization:** preview va citation detail deu check access theo document/version.
- **Data Protection:** signed URL ngan han, khong expose direct object key.
- **Input Validation / Sanitisation:** path params co schema ro rang.
- **Audit Logging:** log ai mo preview cua tai lieu nao, version nao.
- **Threat Considerations:** tranh direct enumeration preview URLs bang signed short-lived link.

## 10. PERFORMANCE & SCALABILITY

- **Key Metrics:** citation lookup < 200ms, preview resolver < 300ms.
- **Capacity Planning:** preview endpoint phai nhe vi co the bi click lien tuc.
- **Caching Strategy:** co the cache preview manifests o service layer; signed URL khong cache lau.
- **Load / Stress Considerations:** nhieu clicks tren evidence panel co the tang signed URL generation.

## 11. OBSERVABILITY & OPERATIONS

- **Logs:** `citation_resolved`, `preview_resolved`, `preview_expired`.
- **Metrics:** preview_requests, preview_not_ready_count.
- **Tracing:** `citation.lookup`, `preview.resolve`.
- **Feature Flags / Configuration:** `PREVIEW_URL_TTL_MINUTES`, `ENABLE_EXCEL_PREVIEW`.

## 12. VERIFICATION & TESTABILITY

- **Unit Tests:** citation detail shape, preview resolver shape, 404/409 behavior, viewer anchor pass-through.
- **Integration Tests:** query/search results co the hydrate sang citation/preview endpoints.
- **Performance Tests:** repeated preview resolve smoke test.
- **Security Tests:** forbidden citation access, signed URL ttl semantics.
- **Traceability:** Cover BR-FN-007, BR-FN-002, BR-NF-002, BR-NF-003.

## 13. RISKS & OPEN ISSUES

| ID | Description | Impact | Mitigation / Action | Owner | Status |
| --- | --- | --- | --- | --- | --- |
| R-LLD-CIT-001 | Preview contract khong dong bo giua query/search/citation endpoints | High | Mot `PreviewTarget` view-model duy nhat cho frontend | Backend/Frontend | Open |
| R-LLD-CIT-002 | Word/Excel preview phu thuoc artifact provider | Medium | fallback download CTA + preview_not_ready semantics | Backend/Frontend | Open |

## 14. APPROVALS & CHANGE HISTORY

| Version | Date | Description | Author | Reviewer | Approved By |
| --- | --- | --- | --- | --- | --- |
| 1.1 | 2026-04-12 | Added strict version-to-document validation and preview-not-ready semantics | OpenAI Codex | Pending | Pending |
| 1.0 | 2026-04-12 | Initial release | OpenAI Codex | Pending | Pending |
