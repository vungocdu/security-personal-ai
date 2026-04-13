# Calculation Logic Specification

## 1. PURPOSE

Mo ta deterministic contract cho hybrid retrieval va rerank trong MVP.

## 2. INPUT DATA SOURCES

| Source | Type | Location / Table | Filters / Conditions | Refresh Cadence | Data Owner |
| --- | --- | --- | --- | --- | --- |
| Dense index | Vector DB | Qdrant `document_chunks` | access_level, ticker, document_type, language | near-real-time | Platform |
| Sparse index | Search index / payload terms | chunk payload | access_level, source, keyword terms | near-real-time | Platform |
| Metadata registry | DB | PostgreSQL `documents`, `document_versions` | document visibility | near-real-time | Platform |

## 3. BUSINESS RULES & DEFINITIONS

| Metric / KPI | Definition | Requirement ID(s) | Notes |
| --- | --- | --- | --- |
| Candidate | Chunk hoac document co score retrieval | BR-FN-003 | Intermediate only |
| Fused rank | Thu hang sau khi hop dense va sparse | BR-NF-002 | Truoc rerank |
| Final rank | Thu hang sau rerank | BR-NF-002 | Dung cho top results |

## 4. CALCULATION LOGIC

### 4.1 Formula Representation

- **Contract form:**
  - `dense_candidates = DenseRetriever.retrieve(query, filters)`
  - `sparse_candidates = SparseRetriever.retrieve(query, filters)`
  - `visible_candidates = apply_access_filter(dense_candidates, sparse_candidates, filters)`
  - `fused_candidates = ResultFusion.fuse(visible_dense, visible_sparse)`
  - `final_candidates = Reranker.rerank(query, fused_candidates[:fused_top_k])`

- **Pseudo-code:**

```text
1. Normalize query and filters.
2. Run dense and sparse retrieval independently.
3. Remove candidates failing access or metadata filter.
4. Fuse by document_version_id + chunk_id identity.
5. Rerank top fused candidates.
6. Emit result payload with dense/sparse/rerank scores when available.
```

### 4.2 Aggregation & Windowing

| Step | Description | Window | Tool / Engine | Notes |
| --- | --- | --- | --- | --- |
| Dense retrieval | Semantic top-k | 30 default | vector store | configurable |
| Sparse retrieval | Keyword top-k | 30 default | sparse search | configurable |
| Fusion | Combine candidates | 20 default | in-process | before rerank |
| Rerank | Final ordering | 20 default | reranker | mandatory contract |

### 4.3 Edge Cases

- Neu dense tra rong nhung sparse co ket qua, van di tiep qua fusion/rerank.
- Neu rerank unavailable, giu fused order va `rerank` score nullable, dong thoi ghi log fallback.
- Neu preview_url khong co, result van hop le nhung UI phai co fallback action.

## 5. OUTPUT SPECIFICATION

| Field | Description | Data Type | Units / Format | Rounding | Consumer |
| --- | --- | --- | --- | --- | --- |
| `scores.dense` | semantic similarity score | float | 0..1 | raw | frontend/backend debug |
| `scores.sparse` | keyword score | float | provider-specific | raw | frontend/backend debug |
| `scores.rerank` | rerank relevance score | float | 0..1 | raw | frontend/backend debug |

## 6. VALIDATION & TESTING

| Test Case ID | Scenario | Input Data | Expected Result | Owner | Status |
| --- | --- | --- | --- | --- | --- |
| TC-SRCH-001 | Dense + sparse both return same chunk | stub candidates | one fused result | Backend | Planned |
| TC-SRCH-002 | Rerank unavailable | stub failure | fused order fallback | Backend | Planned |
| TC-SRCH-003 | Access denied chunk | mixed visibility | forbidden chunk absent | Backend | Planned |

## 7. CHANGE MANAGEMENT

- **Impact Analysis:** Thay doi retrieval windows se anh huong relevance va latency.
- **Approval Workflow:** Can cap nhat LLD + OpenAPI neu wire payload doi.
- **Versioning Strategy:** Contract-level versioning theo OpenAPI minor version.

## 8. APPENDICES

- **References:** OpenAPI `SearchResponse`, AD section hybrid retrieval.

## 9. CHANGE HISTORY

| Version | Date | Description | Author | Reviewer | Approved By |
| --- | --- | --- | --- | --- | --- |
| 1.0 | 2026-04-12 | Initial release | OpenAI Codex | Pending | Pending |
