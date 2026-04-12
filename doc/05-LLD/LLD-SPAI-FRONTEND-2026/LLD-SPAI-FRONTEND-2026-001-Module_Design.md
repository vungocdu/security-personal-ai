# Module Design Specification

## DOCUMENT CONTROL

| Field | Value |
| --- | --- |
| **Document ID** | LLD-SPAI-FRONTEND-2026-001 |
| **Template Version** | 1.0 |
| **Document Version** | 1.1 |
| **Project / Product** | Security Personal AI |
| **Module / Component** | Analyst Workspace Frontend |
| **Author** | OpenAI Codex, AI Implementation Draft |
| **Reviewer(s)** | Tech Lead, QA Lead, Design Lead |
| **Document Status** | Draft |
| **Classification** | Confidential |
| **Creation Date** | 2026-04-12 |
| **Last Updated** | 2026-04-12 |
| **AI-Assisted** | [x] Yes - Tool: **Codex** |

## 1. PURPOSE & SCOPE

- **Objective:** Dinh nghia LLD cho giao dien analyst workstation 3 cot, dong bo voi OpenAPI va phase 1 query-first architecture.
- **In Scope:** repository tree, upload action, chat/query workspace, voice input draft, evidence panel, preview viewer, responsive progressive panels, frontend state mapping.
- **Out of Scope:** query history, saved workspace, watchlist, alerts, collaboration, advanced voice assistant.

## 2. CONTEXT & ASSUMPTIONS

- **Dependencies:** Next.js App Router, TypeScript, shadcn-style primitives, OpenAPI-backed fetch layer, backend preview endpoints, Firebase Web SDK (Auth).
- **Assumptions & Constraints:**
  - Frontend moi hoan toan; UI tone nghiem tuc theo analyst terminal.
  - Auth Phase 1 su dung Firebase Auth; uu tien Email/Password, va co the mo rong Google sign-in (SSO). Frontend lay Firebase ID token va gui `Authorization: Bearer <id_token>` den backend.
  - Backend can duoc cau hinh CORS de cho phep frontend origin (Vercel preview/prod) goi API.
  - Preview Word/Excel co the fallback download neu artifact chua san sang.

## 3. FUNCTIONAL DECOMPOSITION

| Capability | Description | Trigger | Output | Related Requirements |
| --- | --- | --- | --- | --- |
| Repository panel | Hien folder tree, upload, status | app load / upload | document tree | BR-FN-001 |
| Version-aware upload | Upload file vao document dang chon de tao version moi | upload khi da chon document | append version status + refresh tree | BR-FN-001, BR-FN-007 |
| Query workspace | Nhap query, filters, xem answer | user submit | answer cards | BR-FN-003, BR-FN-004 |
| Evidence panel | Hien snippets va preview | click citation/result | synced right panel | BR-FN-007 |
| Voice draft | Ghi am co ban va do transcript vao composer | mic action | draft text | deferred-lite UX |
| Responsive paneling | Drawer for left/right on narrow screens | viewport change | mobile/tablet layout | BR-NF-004 |

- **Business Rules:**
  - Cột giữa la primary focus.
  - Neu user da chon document trong repository panel, upload action phai gui `document_id` de append version.
  - Click citation phai dong bo evidence item va preview target.
  - Left/right panels khong duoc chan luong query.
  - Empty/loading/error states phai ro thay vi de blank UI.
- **State Management:** App state gom `repositoryState`, `queryState`, `evidenceState`, `previewState`, `uiPanelState`.

## 4. SEQUENCE OF OPERATIONS

- **Primary Flow:** page load -> fetch documents -> user query -> render answer -> click citation -> hydrate preview -> sync right panel.
- **Alternate / Exception Flows:** upload accepted nhung indexing chua xong -> left tree status `indexing`; preview fail -> fallback card + download action.
- **Diagram:** [LLD-SPAI-FRONTEND-2026-003-Sequence_Diagram.md](./LLD-SPAI-FRONTEND-2026-003-Sequence_Diagram.md)

## 5. COMPONENT & CLASS DESIGN

- **Component Overview:**
  - `AnalystWorkspacePage`
  - `RepositoryPanel`
  - `QueryWorkspace`
  - `EvidencePanel`
  - `PreviewViewer`
  - `QueryComposer`
  - `VoiceInputButton`
  - `useWorkspaceState`
- **Design Patterns:** container/presentational split, typed API client, reducer/store cho cross-panel sync.
- **Class Diagram:** [LLD-SPAI-FRONTEND-2026-002-Class_Diagram.md](./LLD-SPAI-FRONTEND-2026-002-Class_Diagram.md)
- **Interfaces:**
  - `WorkspaceApi.listDocuments()`
  - `WorkspaceApi.executeQuery()`
  - `WorkspaceApi.search()`
  - `WorkspaceApi.getCitation()`
  - `WorkspaceApi.getPreview()`
  - `WorkspaceApi.uploadDocument(file, documentId?)`

## 6. INTERFACES & CONTRACTS

| Interface | Consumer | Provider | Protocol | DTO / Payload | Notes |
| --- | --- | --- | --- | --- | --- |
| Workspace page data load | UI components | API client | HTTP/JSON | `DocumentCollection` | left panel |
| Query submit | QueryComposer | API client | HTTP/JSON | `QueryRequest/Response` | center panel |
| Citation hydrate | Evidence panel | API client | HTTP/JSON | `CitationResource` | right panel |
| Preview load | Preview viewer | API client | HTTP/JSON | `PreviewResource` | signed URL aware |

- **Backward Compatibility:** Frontend view-model phai co adapter layer neu backend them field optional.
- **Error Models:** loading error, empty state, preview-not-ready state, upload validation state, append-version target not found state.

## 7. DATA DESIGN

- **Data Sources:** OpenAPI responses tu backend.
- **Schemas:** frontend se map sang view models `RepositoryNode`, `AnswerViewModel`, `EvidenceItem`, `PreviewTarget`.
- **Data Flow:** backend payload -> mapper -> reducer/store -> rendered components.
- **Retention & Archiving:** MVP khong persist query history local/server.

## 8. ERROR HANDLING & RESILIENCE

- **Failure Modes:** documents load fail, query fail, preview fail, upload fail, stale citation selection.
- **Fallbacks / Retries:** retry button cho load/query/preview; preview fallback download.
- **Idempotency:** UI actions GET/POST theo backend semantics.
- **Monitoring Hooks:** console-free production UI; logs thong qua structured fetch error handling neu can.

## 9. SECURITY & PRIVACY CONTROLS

- **Authentication & Authorization:**
  - Firebase Auth (Email/Password) cap Firebase ID token o client.
  - Google sign-in (SSO) neu duoc bat o Firebase project va authorized domains.
  - API client attach `Authorization: Bearer <Firebase ID token>` cho moi request can auth.
  - Backend verify token va ap dung enforcement theo config runtime (`AUTH_ENFORCE=true`).
- **Data Protection:** khong log raw snippets nhay cam o browser console.
- **Input Validation / Sanitisation:** trim query input, validate upload file selection.
- **Audit Logging:** khong local analytics; rely backend audit.
- **Threat Considerations:** sanitize preview URLs, khong render untrusted HTML thang.

## 10. PERFORMANCE & SCALABILITY

- **Key Metrics:** first usable workspace < 2s voi fixture data, citation click -> preview update < 500ms.
- **Capacity Planning:** panel rendering phai handle danh sach citation/documents vua phai; tree co the virtualize sau.
- **Caching Strategy:** client-side memo cache nhe cho documents/citations preview.
- **Load / Stress Considerations:** rapid citation switching va viewport changes.

## 11. OBSERVABILITY & OPERATIONS

- **Logs:** chi log error co kiem soat o API client.
- **Metrics:** khong them analytics stack trong MVP.
- **Tracing:** khong bat buoc client tracing.
- **Feature Flags / Configuration:**
  - `NEXT_PUBLIC_API_BASE_URL`
  - Firebase public config: `NEXT_PUBLIC_FIREBASE_API_KEY`, `NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN`,
    `NEXT_PUBLIC_FIREBASE_PROJECT_ID`, `NEXT_PUBLIC_FIREBASE_APP_ID`,
    `NEXT_PUBLIC_FIREBASE_MESSAGING_SENDER_ID`.

## 12. VERIFICATION & TESTABILITY

- **Unit Tests:** render 3 cot, upload CTA, upload-to-selected-document flow, query flow, citation sync, preview fallback, responsive drawers.
- **Integration Tests:** mocked API responses qua MSW hoac fetch mocks.
- **Performance Tests:** khong bat buoc; smoke build/test du.
- **Security Tests:** safe preview URL handling, no dangerous HTML render.
- **Traceability:** Cover BR-FN-001, BR-FN-003, BR-FN-007, BR-NF-004.

## 13. RISKS & OPEN ISSUES

| ID | Description | Impact | Mitigation / Action | Owner | Status |
| --- | --- | --- | --- | --- | --- |
| R-LLD-FE-001 | Frontend overbuild thanh generic chat UI | High | Bám 3-column analyst workstation va evidence-first panel | Frontend | Open |
| R-LLD-FE-002 | Word/Excel preview khong on dinh tren browser | Medium | fallback card + open/download action | Frontend | Open |

## 14. APPROVALS & CHANGE HISTORY

| Version | Date | Description | Author | Reviewer | Approved By |
| --- | --- | --- | --- | --- | --- |
| 1.2 | 2026-04-12 | Updated auth assumptions to Firebase Auth + clarified CORS requirement | OpenAI Codex | Pending | Pending |
| 1.1 | 2026-04-12 | Added version-aware upload flow and API contract update | OpenAI Codex | Pending | Pending |
| 1.0 | 2026-04-12 | Initial release | OpenAI Codex | Pending | Pending |
