# Calculation Logic Specification

## 1. PURPOSE

Mo ta mandatory document versioning model va state transition logic.

## 2. INPUT DATA SOURCES

| Source | Type | Location / Table | Filters / Conditions | Refresh Cadence | Data Owner |
| --- | --- | --- | --- | --- | --- |
| Upload metadata | API form | `POST /documents` | visible user only | per request | Frontend/API |
| Document registry | DB | `documents` | active documents | real-time | Platform |
| Version registry | DB | `document_versions` | by document_id | real-time | Platform |

## 3. BUSINESS RULES & DEFINITIONS

| Metric / KPI | Definition | Requirement ID(s) | Notes |
| --- | --- | --- | --- |
| Logical document | Doi tuong on dinh dai dien mot tai lieu nghiep vu | BR-FN-001 | `document_id` |
| Document version | Ban ingest/version cu the cua logical document | BR-FN-001 | `document_version_id` |
| Current version | Version moi nhat duoc xem la chinh | BR-FN-007 | Duy nhat mot ban |

## 4. CALCULATION LOGIC

### 4.1 Formula Representation

```text
On upload:
1. Resolve logical document by source metadata policy.
2. Create new document_version_id.
3. Mark new version = accepted.
4. If upload supersedes current version, set previous current version parse_status = superseded and is_current_version = false.
5. Set new version is_current_version = true after indexing success.
6. Update documents.current_version_id.
```

### 4.2 Aggregation & Windowing

| Step | Description | Window | Tool / Engine | Notes |
| --- | --- | --- | --- | --- |
| Acceptance | Create provisional version | request-time | API/service | sync |
| Indexing success | Promote to current | async worker | ingestion | deferred |
| Failure | Keep previous current version | async worker | ingestion | no destructive switch |

### 4.3 Edge Cases

- Neu version moi fail indexing, `documents.current_version_id` khong duoc chuyen sang version loi.
- Neu tai lieu bi thu hoi, current version co the thanh `withdrawn` va UI phai hien status.
- Neu metadata khong resolve duoc logical document, tao document moi.

## 5. OUTPUT SPECIFICATION

| Field | Description | Data Type | Units / Format | Rounding | Consumer |
| --- | --- | --- | --- | --- | --- |
| `current_version_id` | version dang duoc dung | string | id | n/a | frontend/backend |
| `version_label` | human label | string | `v1`, `v2` | n/a | frontend |
| `parse_status` | version lifecycle status | enum | status | n/a | frontend/backend |

## 6. VALIDATION & TESTING

| Test Case ID | Scenario | Input Data | Expected Result | Owner | Status |
| --- | --- | --- | --- | --- | --- |
| TC-DOC-001 | First upload | no existing document | create v1 current | Backend | Planned |
| TC-DOC-002 | Superseding upload success | existing v1 indexed | v2 current, v1 superseded | Backend | Planned |
| TC-DOC-003 | Superseding upload fail | existing v1 indexed | v1 stays current | Backend | Planned |

## 7. CHANGE MANAGEMENT

- **Impact Analysis:** Versioning policy doi se anh huong left tree, citations, preview.
- **Approval Workflow:** Can cap nhat LLD, OpenAPI, backend tests.
- **Versioning Strategy:** Policy changes phai semantically backward compatible voi IDs.

## 8. APPENDICES

- **References:** OpenAPI `DocumentResource`, `DocumentVersionResource`.

## 9. CHANGE HISTORY

| Version | Date | Description | Author | Reviewer | Approved By |
| --- | --- | --- | --- | --- | --- |
| 1.0 | 2026-04-12 | Initial release | OpenAI Codex | Pending | Pending |
