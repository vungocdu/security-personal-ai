# Architecture Design

**Document ID:** AD-SPAI-2026-001  
**Template Version:** 1.0.0  
**Standard Alignment:** ISO/IEC/IEEE 42010, ISO/IEC 12207:2017 (6.4.4), ISO/IEC 15288:2023 (6.4.4), ISO/IEC/IEEE 29148:2018, ISO/IEC 27001:2022, PDPA (Singapore)

---

## Document Control

| Field | Value |
| --- | --- |
| **Project** | Security Personal AI |
| **System / Component** | Securities Research Document Intelligence Platform |
| **Document Version** | 0.3 Draft |
| **Status** | Draft |
| **Classification** | Confidential |
| **Author** | OpenAI Codex, AI Architecture Draft |
| **Architect / Tech Lead** | Pending |
| **Contributors** | Human review pending |
| **Creation Date** | 2026-04-12 |
| **Last Updated** | 2026-04-12 |
| **Approved By** | Pending |
| **Approval Date** | Pending |
| **Next Review Date** | 2026-04-26 |
| **AI-Assisted** | [x] Yes — Tool: **Codex** |

---

## ISO Traceability

| ISO Clause / Control | Addressed In | Evidence / Notes |
| --- | --- | --- |
| ISO/IEC 12207:2017 §6.4.4 (Architecture Definition) | Entire document | Defines views, decisions, constraints, runtime and operational concerns |
| ISO/IEC/IEEE 42010 §5 (Architecture Description) | Sections 1–7 | Stakeholders, concerns, viewpoints, views, rationale |
| ISO/IEC/IEEE 29148 §9 (Traceability) | §3, §12 | Requirement mapping to architecture response and risk handling |
| ISO/IEC 27001:2022 Annex A (Security) | §9, §11, §12 | Access control, logging, encryption, operational controls |
| PDPA (Singapore) | §9.3, §9.5 | Data minimization, retention boundary, privacy-first handling |

---

## 1. Executive Summary

**Solution Overview:**  
Hệ thống được thiết kế như một nền tảng RAG chuyên biệt cho chuyên gia chứng khoán để truy vấn kho tài liệu nghiệp vụ bằng ngôn ngữ tự nhiên, trả lời có citation và cho phép kiểm chứng nguồn ở cấp tài liệu, trang và đoạn. Kiến trúc Phase 1 theo hướng query-first, ưu tiên ingest, indexing, hybrid retrieval, metadata filtering, reranking, answer synthesis và citation preview. Bản v0.3 bổ sung metadata contract tối thiểu, mandatory document versioning, retrieval/rerank contract và citation preview contract để team có thể triển khai nhất quán, đồng thời giữ MVP ở trạng thái tối giản, không yêu cầu thêm observability stack nặng ngoài Langfuse và structured application logs. Các năng lực như query history, workspace, watchlist, alerts và analytics người dùng chưa đưa vào baseline giai đoạn này.

**Highlights / Key Changes:**

- Chuyển trọng tâm từ assistant đa workflow sang query-first RAG foundation cho tài liệu chuyên ngành.
- Tách rõ năng lực Phase 1 và các hạng mục deferred để tránh loãng retrieval core.
- Giữ security enforcement ở retrieval stage, không chỉ ở tầng UI hoặc post-filter.
- Bổ sung contract đủ chi tiết cho metadata, versioning, hybrid retrieval và citation preview.

**Compliance Status:**

- Architecture Review: Pending
- Security Review: Pending
- Traceability: Draft complete against BRD v0.1 with deferred items explicitly noted

---

## 2. Introduction

### 2.1 Purpose

Tài liệu này mô tả kiến trúc tổng thể cho hệ thống AI Assistant hỗ trợ chuyên gia chứng khoán truy vấn kho tài liệu văn bản chuyên ngành. Tài liệu được dùng làm baseline cho thiết kế chi tiết, triển khai Phase 1, review kiến trúc, review bảo mật và đối chiếu với BRD.

### 2.2 Scope

- **In Scope:** upload thủ công hoặc batch import đơn giản, parsing và chunking tài liệu, metadata enrichment cơ bản, indexing, hybrid retrieval, metadata filtering, reranking, answer synthesis có citation, preview nguồn trích dẫn, authentication và authorization, observability phục vụ vận hành truy vấn.
- **Out of Scope:** query history, search session history, saved workspace, watchlist, alerts, collaborative workspace, compare workflow phức tạp, timeline extraction đa bước, recommendation engine, analytics hành vi người dùng nâng cao, trading integration, OMS/EMS integration.

### 2.3 References

| Document | ID / Location | Description |
| --- | --- | --- |
| BRD | `/Users/steve/development/mercury/security-personal-ai/doc/01-Requirements/BRD/BRD-SPAI-2026-001-Personal_AI_Agent_For_Stock_Expert.md` | Business Requirements Document |
| AD Template | `/Users/steve/development/mercury/security-personal-ai/doc/02-Architecture/AD/TEMPLATE-ARCH-001-Architecture_Design.md` | Architecture Design template |
| Project Guidance | `/Users/steve/development/mercury/security-personal-ai/AGENTS.md` | Project direction and documentation rules |
| SRS | `/Users/steve/development/mercury/security-personal-ai/doc/01-Requirements/SRS/` | Pending detailed system requirements |
| ADR Index | `/Users/steve/development/mercury/security-personal-ai/doc/02-Architecture/ADR/` | Pending detailed ADR files |
| API Design | `/Users/steve/development/mercury/security-personal-ai/doc/02-Architecture/API/` | Pending API contract details |
| Data Model | `/Users/steve/development/mercury/security-personal-ai/doc/02-Architecture/Data_Model/` | Pending logical and physical data model |
| Security Plan | `/Users/steve/development/mercury/security-personal-ai/doc/02-Architecture/Security_Privacy/` | Pending security and privacy plan |

---

## 3. Requirements Traceability (ISO/IEC/IEEE 29148)

| Requirement ID | Description | Architectural Response (Section / View) | Verification Method |
| --- | --- | --- | --- |
| BR-FN-001 | Kết nối và đọc tài liệu từ nguồn người dùng chỉ định | §6.3 Container View, §8 Data Architecture | Integration test, UAT |
| BR-FN-002 | Hỗ trợ đọc PDF, Word, Excel, text/article | §6.4 Component View, §8.2 Logical & Physical Models | Parser test set, ingestion validation |
| BR-FN-003 | Truy vấn bằng ngôn ngữ tự nhiên để tìm tài liệu liên quan | §6.6 Runtime View, §10 Quality Attributes | Query relevance evaluation, UAT |
| BR-FN-004 | Tóm tắt từ một hoặc nhiều tài liệu có nguồn | §6.4, §6.6, §10 | Grounded answer test, citation inspection |
| BR-FN-005 | Trích xuất dữ liệu quan trọng từ tài liệu | Deferred to Phase 2; Phase 1 chỉ hỗ trợ retrieval và answer synthesis có citation | Scope review, roadmap tracking |
| BR-FN-006 | So sánh nhiều tài liệu hoặc nhiều kỳ báo cáo | Deferred to Phase 2 | Scope review, roadmap tracking |
| BR-FN-007 | Hiển thị hoặc dẫn chiếu nguồn gốc câu trả lời | §6.4 Citation Packaging, §8, §10 | UI inspection, citation coverage metric |
| BR-FN-008 | Voice command cơ bản | Deferred to later phase; Phase 1 ưu tiên text query | Scope review, roadmap tracking |
| BR-FN-009 | Ghi nhớ lịch sử phiên hỏi đáp gần nhất | Explicitly out of scope for Phase 1 per architecture baseline | Design review |
| BR-NF-001 | Kết quả sơ bộ trong vòng 5 giây cho truy vấn phổ biến | §10, §11 | Load test, latency dashboard |
| BR-NF-002 | Kết quả quan trọng có khả năng kiểm chứng từ nguồn | §6.6, §10 | Citation audit, UAT |
| BR-NF-003 | Bảo mật và riêng tư tài liệu người dùng | §9 | Security review, access control test |
| BR-NF-004 | Dễ sử dụng cho người dùng không rành kỹ thuật | §6.2, §6.4 | UX review, UAT |
| BR-NF-005 | Hỗ trợ vài nghìn tài liệu giai đoạn đầu | §6.3, §10, §11 | Pilot scale test |
| BR-NF-006 | Truy ngược về file hoặc đoạn nguồn | §8, §10 | UI inspection, traceability test |

**Notes:**  
BRD v0.1 có phạm vi rộng hơn Phase 1 ở các mục voice, extraction nâng cao, compare và query memory. AD này cố ý giới hạn baseline về query-first RAG foundation để bảo vệ chất lượng retrieval core trước khi mở rộng workflow.

---

## 4. Stakeholders & Concerns (ISO/IEC/IEEE 42010)

| Stakeholder | Role / Interest | Key Concerns | Contact / Review Status |
| --- | --- | --- | --- |
| Chuyên gia phân tích chứng khoán | End user | Truy vấn nhanh, câu trả lời có citation, không bịa nội dung | Pending |
| Research manager | Standardization | Tính nhất quán, khả năng kiểm chứng, khả năng scale use case sau pilot | Pending |
| Compliance / Legal | Governance | Access control, auditability, data leakage prevention | Pending |
| Product Owner | Business outcome | MVP rõ, chứng minh giá trị nhanh, tránh scope creep | Pending |
| Technical Lead | Delivery feasibility | Modularity, replaceable providers, maintainability | Pending |
| DevOps / Operations | Runtime support | Observability, rollback, cost, backup, failure handling | Pending |
| Security Officer | Risk & compliance | Encryption, least privilege, private deployment option | Pending |

---

## 5. Constraints & Architectural Principles

### 5.1 Constraints

| Constraint ID | Category | Description | Source |
| --- | --- | --- | --- |
| CON-ARCH-001 | Scope | Phase 1 chỉ tập trung query foundation, không ôm thêm query history/workspace | Product direction |
| CON-ARCH-002 | Data | Tài liệu đầu vào có thể không đồng nhất, có OCR quality không ổn định | Domain reality |
| CON-ARCH-003 | Security | Dữ liệu nội bộ nhạy cảm không được rò vào prompt khi user không có quyền | Security baseline |
| CON-ARCH-004 | Delivery | Chưa có SRS/ADR/API spec chi tiết, cần dùng AD làm baseline cho giai đoạn tiếp theo | Repository state |
| CON-ARCH-005 | Performance | Pilot phải đáp ứng workflow analyst với latency hợp lý trên vài nghìn tài liệu | BRD |

### 5.2 Architectural Principles

| Principle | Description | Implications |
| --- | --- | --- |
| Evidence-first | Câu trả lời phải gắn với nguồn tài liệu | Citation packaging là bắt buộc, answer không grounded phải từ chối hoặc nêu thiếu căn cứ |
| Retrieval before generation | LLM không phải source of truth | Orchestrator chỉ synthesis trên retrieved context |
| Metadata-driven intelligence | Precision đến từ metadata nghiệp vụ, không chỉ vector similarity | Bắt buộc có metadata normalization và filter builder |
| Security at retrieval stage | Quyền truy cập phải áp từ lúc lấy context | Access filter phải tham gia vào search payload |
| Loose coupling | Tách UI, API, orchestrator, stores, providers | Cho phép thay model/vector store mà không phá toàn hệ thống |
| Observable by default | Truy vấn, indexing, rerank, generation phải đo được | Trace, metric, log kỹ thuật là thành phần lõi |

---

## 6. Architecture Viewpoints & Views

### 6.1 Viewpoint Catalogue

| Viewpoint | Purpose | Stakeholder Concerns | View(s) Provided |
| --- | --- | --- | --- |
| Context | Xác định ranh giới hệ thống và external actors | Product Owner, Security, Compliance | §6.2 |
| Container | Xác định các deployable unit chính | Tech Lead, DevOps | §6.3 |
| Component | Mô tả module và trách nhiệm nội bộ | Developers, QA | §6.4 |
| Deployment | Mô tả topology runtime cho pilot và production | DevOps, Security | §6.5 |
| Sequence / Runtime | Mô tả các flow chính của query và indexing | QA, Ops, Product | §6.6 |

### 6.2 Context View

Hệ thống nằm giữa người dùng nghiệp vụ và kho tài liệu chuyên ngành. Các actor và external systems chính:

- Chuyên gia chứng khoán dùng web UI để hỏi bằng văn bản và kiểm tra citation.
- System administrator quản lý user, quyền truy cập và tình trạng indexing.
- Nguồn tài liệu vào gồm upload thủ công và batch import đơn giản từ repository nội bộ hoặc thư mục được chỉ định.
- Identity provider cung cấp xác thực và thông tin vai trò người dùng.
- Monitoring/logging platform nhận trace, metric, log kỹ thuật.

Trust boundary chính:

- Boundary 1: User browser tới frontend/backend.
- Boundary 2: Backend/orchestrator tới data stores và model providers.
- Boundary 3: Nguồn tài liệu thô tới ingestion pipeline.

### 6.3 Container View

| Container | Technology Direction | Responsibility |
| --- | --- | --- |
| Web Application | Next.js | Query input, metadata filters, citation list, preview, upload UI, indexing status |
| API Gateway | FastAPI | Authentication, authorization, query endpoint, document APIs, citation payload formatting |
| Orchestrator Service | LangGraph-based Python service | Intent classification nhẹ, entity extraction, filter builder, retrieval orchestration, rerank, synthesis, response validation |
| Ingestion Worker | Python background worker | Parsing, OCR orchestration, cleaning, chunking, metadata enrichment, embedding, indexing |
| Object Storage | S3/R2/MinIO | Lưu file gốc và preview artifacts |
| Metadata Database | PostgreSQL | Document registry, source registry, company/ticker mapping, user permission, indexing status, citation metadata |
| Vector Store | Qdrant | Chunk embeddings, chunk payload metadata, semantic retrieval index |
| Observability Stack | Langfuse + structured application logs | AI traces, latency/cost metrics, operational monitoring for MVP |

### 6.4 Component View

#### Presentation Layer

- Query Workspace: nhập câu hỏi, chọn filters, xem answer.
- Citation Panel: hiển thị document, page, section, snippet.
- Document Preview: mở đúng trang/đoạn nguồn để kiểm chứng.
- Upload & Index Monitor: nạp tài liệu và xem trạng thái indexing.

#### Application/API Layer

- Auth Controller: xác thực và nạp access scope.
- Query Controller: nhận query request, tạo trace, gọi orchestrator.
- Document Controller: upload, list, get status, reindex.
- Citation Controller: chuẩn hóa citation payload cho UI preview.

#### Intelligence Orchestration Layer

- Query Intake Node: chuẩn hóa request, validate input.
- Intent Classification Node: nhận diện query QA/search/summary ở mức đủ dùng cho Phase 1.
- Entity Extraction Node: tách ticker, company, date range, document type, source.
- Metadata Filter Builder: chuyển entity + user filters thành search constraints.
- Hybrid Retrieval Node: dense + sparse + metadata retrieval.
- Reranker Node: sắp lại relevance của candidate chunks.
- Answer Synthesis Node: sinh câu trả lời grounded trên context.
- Citation Packaging Node: đóng gói citation tới cấp document/page/chunk.
- Response Validation Node: chặn answer thiếu căn cứ hoặc vượt context.

#### Data Processing & Retrieval Layer

- Parsers: PDF, DOCX, XLSX, HTML, TXT/MD.
- OCR Adapter: xử lý scan PDF khi cần.
- Cleaner/Normalizer: loại header/footer lặp, chuẩn hóa ký tự, nhận diện heading.
- Structural Chunker: chunk theo section, không chỉ token window cứng.
- Metadata Enricher: ticker, company, report type, publish date, fiscal period, source, language, access scope.
- Embedding Adapter: gọi embedding model đa ngôn ngữ.
- Sparse Retrieval Adapter: lập chỉ mục và truy vấn keyword/BM25 hoặc sparse vector cho ticker, legal term, financial term, numeric phrase.
- Index Writer: đồng bộ object storage, PostgreSQL và Qdrant.

### 6.5 Deployment View

#### Pilot / MVP Topology

- Frontend: Vercel hoặc nền tảng tương đương.
- FastAPI + orchestrator + ingestion workers: container service managed.
- PostgreSQL: managed database.
- Qdrant: cloud managed hoặc self-host nhỏ.
- Object storage: managed private bucket.
- Langfuse Cloud hoặc self-host nhỏ cho trace.

**MVP note:** Pilot không yêu cầu Redis riêng, Prometheus, Grafana hoặc logging cluster riêng. Structured logs từ ứng dụng và trace từ Langfuse là đủ để vận hành giai đoạn đầu.

#### Production / Enterprise Topology

- Frontend: Vercel private hosting hoặc internal hosting.
- API và workers: Kubernetes, ECS hoặc VM cluster trong private network.
- PostgreSQL và Qdrant: private subnet, backup và access control riêng.
- Object storage: encrypted private bucket.
- Secret manager, network policy, audit sink.

#### Environment Model

- Development: thử nghiệm parser, retrieval, UI.
- Staging: dữ liệu mẫu kiểm soát, test hiệu năng và security.
- Production: dữ liệu thực, RBAC/ABAC, logging/audit, backup đầy đủ.

### 6.6 Runtime / Sequence Views

#### Query Flow

1. User nhập câu hỏi và chọn filters tại UI.
2. Frontend gửi request tới FastAPI.
3. FastAPI xác thực user, nạp access scope và tạo trace ID.
4. Request được chuyển tới orchestrator.
5. Orchestrator chạy intent classification và entity extraction.
6. Metadata Filter Builder tạo filter từ user input, entity và access policy.
7. Hybrid retrieval lấy candidate chunks từ dense, sparse và metadata index.
8. Reranker sắp lại candidate chunks.
9. LLM tổng hợp câu trả lời dựa trên context được phép truy cập.
10. Citation Packaging gắn document/page/chunk/snippet.
11. Response Validation kiểm tra grounding và citation coverage.
12. Backend trả answer, citations và preview links về frontend.
13. Frontend render answer, citation list và document preview.

**Note:** Phase 1 không bắt buộc lưu query history sau khi trả kết quả. Chỉ lưu technical log tối thiểu phục vụ trace, debug, latency và security audit.

#### Document Ingestion Flow

1. User upload file hoặc batch import tài liệu.
2. Hệ thống lưu file gốc vào object storage.
3. Ingestion worker parse nội dung hoặc gọi OCR nếu cần.
4. Cleaner/Normalizer chuẩn hóa text và cấu trúc.
5. Structural Chunker chia tài liệu theo section nghiệp vụ.
6. Metadata Enricher gắn metadata domain và access scope.
7. Embedding Adapter sinh vector cho chunks.
8. Sparse Retrieval Adapter ghi sparse index hoặc sparse payload cho keyword retrieval.
9. Index Writer ghi metadata vào PostgreSQL và vectors vào Qdrant.
10. Validation kiểm tra chunk rỗng, parse success rate, metadata tối thiểu.
11. Document status được cập nhật sang indexed hoặc failed.

### 6.7 Cross-cutting Concerns

- **Observability:** trace theo request ID, metric cho indexing/query, log lỗi parser/OCR/retrieval/generation.
- **Configuration Management:** config theo môi trường, secret trong secret manager, feature flags cho model provider và reranker.
- **Error Handling / Resilience:** retry có kiểm soát cho ingestion jobs, timeout cho external model provider, graceful degradation khi một retrieval source thất bại.

---

## 7. Architecture Decisions (ADR Summary)

| ADR ID | Decision | Status | Rationale | Implications |
| --- | --- | --- | --- | --- |
| ADR-0001 | Chọn query-first RAG foundation cho Phase 1 | Accepted | Tập trung vào pain point cốt lõi là truy vấn tài liệu đúng và có citation | Các tính năng workflow và personalization bị deferred |
| ADR-0002 | Dùng hybrid retrieval thay vì vector-only | Accepted | Tài liệu chứng khoán chứa ticker, thuật ngữ pháp lý, kỳ báo cáo và số liệu cần keyword precision | Hệ thống retrieval phức tạp hơn nhưng precision tốt hơn |
| ADR-0003 | Tách PostgreSQL khỏi Qdrant | Accepted | Metadata nghiệp vụ và transactional status không phù hợp nằm hoàn toàn trong vector DB | Cần đồng bộ trạng thái index giữa hai kho |
| ADR-0004 | Dùng structural chunking | Accepted | Giữ ngữ nghĩa section tài chính/pháp lý tốt hơn token split cứng | Pipeline parsing/normalization phức tạp hơn |
| ADR-0005 | Enforce authorization ở retrieval stage | Accepted | Tránh rò dữ liệu vào prompt | Access scope phải hiện diện trong metadata index |
| ADR-0006 | Không lưu query history trong Phase 1 | Accepted | Giảm độ phức tạp, tránh loãng mục tiêu và data retention không cần thiết | Chỉ giữ log kỹ thuật tối thiểu cho vận hành và audit |
| ADR-0007 | Hybrid retrieval phải gồm dense + sparse + metadata filter + fusion + rerank | Accepted | Tránh trượt về vector search thuần, tăng precision cho ticker, pháp lý và thuật ngữ tài chính | Cần định nghĩa retrieval contract và scoring pipeline rõ ràng |
| ADR-0008 | Document versioning là bắt buộc ngay từ Phase 1 | Accepted | Tài liệu chứng khoán có bản sửa đổi, cập nhật, revised report, amended filing | Citation và retrieval phải luôn tham chiếu bản hiệu lực đúng |
| ADR-0009 | Citation preview phải support page-level và chunk-level anchor | Accepted | User cần bấm citation và thấy đúng bằng chứng, không chỉ mở đúng file | Cần preview artifacts, text offset mapping và API payload chuẩn |

---

## 8. Data Architecture

### 8.1 Data Domains & Ownership

| Domain | Owner | Systems of Record | Notes |
| --- | --- | --- | --- |
| Document Registry | Application team | PostgreSQL | Trạng thái tài liệu và indexing |
| Source Files | Platform storage | Object storage | File gốc và preview assets |
| Retrieval Index | Search/RAG layer | Qdrant | Chunk embeddings và payload |
| Access Control Metadata | Application team | PostgreSQL | User/document scope |
| Reference Data | Application team | PostgreSQL | Company master, ticker alias |

### 8.2 Logical & Physical Models

**Logical model summary:**

- `sources`
- `documents`
- `document_versions`
- `document_chunks`
- `document_citations`
- `companies`
- `ticker_aliases`
- `user_roles`
- `user_document_permissions`
- `index_jobs`

**Physical storage:**

- PostgreSQL lưu registry, status, metadata nghiệp vụ, access control và citation mapping metadata.
- Qdrant lưu embedding của chunk cùng payload cần cho retrieval.
- Object storage lưu file gốc, preview image/page artifact, OCR intermediate nếu cần.

**Integration flows:**

- Ingestion worker ghi object storage trước, sau đó parse/chunk/enrich và ghi PostgreSQL + Qdrant.
- Query runtime đọc metadata/access policy từ PostgreSQL và context chunks từ Qdrant.

### 8.3 Metadata Contract

#### 8.3.1 Document-level minimum metadata

| Field | Required | Description |
| --- | --- | --- |
| `document_id` | Yes | Định danh bất biến cho logical document |
| `document_version_id` | Yes | Định danh cho bản cụ thể được index |
| `title` | Yes | Tên tài liệu hiển thị cho user |
| `source` | Yes | Nguồn tài liệu, ví dụ upload, internal repository, crawl |
| `language` | Yes | Ngôn ngữ chính của tài liệu |
| `document_type` | Yes | Annual report, financial statement, research report, legal document... |
| `ticker` | Conditional | Mã cổ phiếu chính nếu áp dụng |
| `company_name` | Conditional | Tên công ty chính nếu áp dụng |
| `sector` | Conditional | Ngành của doanh nghiệp hoặc tài liệu |
| `market` | Conditional | Sàn hoặc thị trường liên quan |
| `reporting_period` | Conditional | Kỳ báo cáo, ví dụ FY2024, Q3-2024 |
| `fiscal_year` | Conditional | Năm tài chính |
| `quarter` | Conditional | Quý tài chính nếu có |
| `publication_date` | Yes | Ngày phát hành hoặc công bố |
| `author_org` | Conditional | Tổ chức phát hành, công ty chứng khoán, cơ quan quản lý |
| `access_level` | Yes | Public, internal, restricted... |
| `version` | Yes | Nhãn version hiển thị, ví dụ v1, amended-2 |
| `is_current_version` | Yes | Bản hiện hành có được dùng mặc định hay không |
| `supersedes_version_id` | Conditional | Tham chiếu bản cũ bị thay thế |
| `ingested_at` | Yes | Thời điểm ingest |
| `checksum` | Yes | Dùng cho dedupe và integrity |
| `parse_status` | Yes | indexed, failed, superseded, draft |

#### 8.3.2 Chunk-level minimum metadata

| Field | Required | Description |
| --- | --- | --- |
| `chunk_id` | Yes | Định danh chunk |
| `document_id` | Yes | Logical document owner |
| `document_version_id` | Yes | Bản tài liệu chứa chunk |
| `page_number` | Conditional | Trang nguồn nếu có |
| `section_heading` | Conditional | Heading hoặc subheading gần nhất |
| `chunk_sequence` | Yes | Thứ tự chunk trong tài liệu |
| `chunk_text` | Yes | Nội dung text canonical |
| `chunk_summary` | No | Summary ngắn phục vụ rerank/preview nếu có |
| `text_offset_start` | Conditional | Offset trong canonical text |
| `text_offset_end` | Conditional | Offset trong canonical text |
| `table_reference` | No | Liên kết tới bảng liên quan nếu chunk thuộc table context |
| `ticker` | Conditional | Denormalized để filter nhanh |
| `document_type` | Yes | Denormalized để filter nhanh |
| `publication_date` | Yes | Denormalized để filter nhanh |
| `access_level` | Yes | Dùng cho retrieval authorization |
| `embedding_model` | Yes | Model dùng sinh vector |
| `sparse_terms_version` | Conditional | Phiên bản tokenizer/term expansion cho sparse retrieval |
| `ocr_quality_score` | Conditional | Điểm OCR nếu chunk đến từ scan |

**Contract rule:** Document nào thiếu metadata required sẽ không được publish vào searchable index. Có thể lưu ở trạng thái `failed_metadata_validation`, nhưng không được dùng cho query runtime.

### 8.4 Document Versioning Model

#### 8.4.1 Versioning rules

- Mỗi logical document phải có ít nhất một record trong `documents` và một hoặc nhiều record trong `document_versions`.
- Retrieval mặc định chỉ search trên `document_versions.is_current_version = true`, trừ khi user hoặc workflow yêu cầu include lịch sử version.
- Khi ingest một bản mới:
  - tạo `document_version_id` mới,
  - đánh dấu bản cũ `is_current_version = false`,
  - set `superseded_at`,
  - giữ nguyên bản cũ cho audit và citation lịch sử.
- Citation luôn phải chứa cả `document_id` và `document_version_id`.
- Nếu một version bị thu hồi hoặc phát hiện parse sai nghiêm trọng, trạng thái phải chuyển sang `withdrawn` hoặc `invalidated`, và version đó không được retrieve nữa.

#### 8.4.2 Runtime implication

- Query runtime chỉ được synthesize trên version hợp lệ và đang hiệu lực theo policy.
- Preview UI phải hiển thị rõ version label khi citation không thuộc current version.
- Reindex một document không được overwrite version cũ theo kiểu destructive.

### 8.5 Data Classification & Retention

| Entity | Classification | Retention Policy | Control Reference |
| --- | --- | --- | --- |
| Source documents | Confidential | Theo chính sách lưu trữ tài liệu nghiệp vụ | Security plan pending |
| Document metadata | Internal / Confidential | Gắn theo vòng đời tài liệu | Security plan pending |
| Query technical logs | Internal | Giữ tối thiểu để vận hành và audit | Operations policy pending |
| User permissions | Confidential | Cho đến khi quyền bị thu hồi hoặc user offboard | Access control policy |

**Explicitly not stored in Phase 1:**

- query history
- search session history
- saved prompts/workspace
- personalization profile
- detailed feedback history

### 8.6 Data Quality & Governance

- Validation bắt buộc cho parse success rate, non-empty chunk ratio, metadata tối thiểu.
- Alias mapping cho ticker/company để giảm miss retrieval.
- OCR quality score cần được lưu để xác định tài liệu nào cần manual review.
- Tài liệu failed index phải có trạng thái rõ ràng và lý do lỗi.
- Version transition phải có audit trail để biết bản nào supersede bản nào.

---

## 9. Security & Privacy Architecture

### 9.1 Threat Model Summary

- **Primary threats:** unauthorized document access, prompt leakage, data exfiltration via external providers, tampered citations, insecure upload pipeline, excessive logging of sensitive content.
- **Attack surfaces:** web UI, query APIs, upload APIs, orchestrator-to-model provider calls, object storage, metadata DB, vector store.
- **Risk posture:** medium for pilot, requires strict retrieval-level authorization and secret management before production.

### 9.2 Authentication & Authorization

| Area | Design | Control Reference |
| --- | --- | --- |
| Identity Provider | OIDC/OAuth compatible provider hoặc SSO nội bộ | Security plan pending |
| Session Management | Short-lived session/JWT with backend validation | Security plan pending |
| RBAC / ABAC | Role + document sensitivity + source ownership + organization/team scope | RBAC matrix pending |

### 9.3 Data Protection

| Layer | Control | Notes |
| --- | --- | --- |
| In transit | TLS for browser, service-to-service encryption | Bắt buộc cho mọi môi trường ngoài local dev |
| At rest | Encryption for object storage, PostgreSQL, Qdrant volumes | Managed KMS hoặc equivalent |
| Data minimization | Không lưu query history trong Phase 1; log chỉ giữ technical metadata cần thiết | Giảm rủi ro privacy và retention |

### 9.4 Logging, Monitoring, & Incident Response

- Log theo request ID, document ID, job ID; không log full corpus tràn lan.
- MVP chỉ cần các cảnh báo cơ bản cho indexing failure, vector DB unavailability, provider timeout spike.
- Runbook cần có quy trình revoke access, rotate secrets, tạm dừng provider nếu có data exposure concern.

### 9.5 Compliance & Privacy

- Privacy-first: tài liệu người dùng là dữ liệu nhạy cảm, không đẩy corpus gốc ra ngoài nếu chưa được chấp thuận.
- Cần có chế độ private deployment cho dữ liệu nội bộ hoặc highly confidential.
- Auditability tập trung vào ai truy cập tài liệu nào, query nào gọi model nào, chunks nào được dùng để trả lời.
- Access control phải áp trên `document_version` và payload metadata của chunk, không chỉ logical document.

---

## 10. Quality Attributes & Non-Functional Requirements

| Attribute | Target / KPI | Architecture Strategies | Verification |
| --- | --- | --- | --- |
| Performance | Kết quả sơ bộ trong vòng 5 giây cho truy vấn phổ biến ở pilot dataset | Hybrid retrieval tối ưu, rerank scope hợp lý, async ingestion, optional cache | Load test, latency dashboards |
| Accuracy | Citation coverage cao, grounded answer, retrieval precision phù hợp use case analyst | Structural chunking, metadata filters, reranking, response validation | Golden query set, citation audit |
| Scalability | Hỗ trợ vài nghìn tài liệu ở giai đoạn đầu và mở rộng ngang sau đó | Stateless API, worker-based ingestion, separate stores | Pilot scale test |
| Security | Không rò tài liệu ngoài quyền truy cập | Retrieval-level authorization, encrypted storage, secret management | Security review, access tests |
| Maintainability | Thay model/vector store không phá vỡ toàn hệ thống | Provider abstraction, modular nodes, clear boundaries | Design review, integration test |
| Reliability | Query và indexing có retry/failure status rõ ràng | Job status tracking, timeout, circuit breaker cho provider | Chaos/failure test nhỏ |
| Observability | Theo dõi end-to-end query/index pipeline | Trace + metric + structured log | Dashboard review |

---

## 11. Retrieval & Citation Contracts

### 11.1 Hybrid Retrieval Contract

#### 11.1.1 Retrieval stages

1. Query normalization và entity extraction.
2. Metadata filter construction từ user filters + extracted entities + access scope.
3. Dense retrieval trên embedding index.
4. Sparse retrieval trên keyword/BM25 hoặc sparse-vector index.
5. Merge candidate set bằng fusion strategy chuẩn.
6. Rerank top candidates bằng reranker model.
7. Build final context window cho synthesis.

#### 11.1.2 Mandatory contract

- Hybrid retrieval trong Phase 1 bắt buộc có đủ 4 phần:
  - dense retrieval,
  - sparse retrieval,
  - metadata filtering,
  - reranking.
- Dense retrieval không được chạy trên corpus không qua metadata access filter.
- Sparse retrieval phải hỗ trợ chính xác cho:
  - ticker,
  - company alias,
  - legal term,
  - financial term,
  - reporting period phrase,
  - numeric phrase quan trọng nếu parser giữ được.
- Fusion strategy chuẩn mặc định là reciprocal rank fusion hoặc weighted rank fusion. Strategy cụ thể phải được cố định trong ADR/API config, không để mỗi môi trường tự chọn.
- Candidate budget cần được cấu hình rõ, ví dụ:
  - dense top-k pre-fusion,
  - sparse top-k pre-fusion,
  - fused top-k pre-rerank,
  - final top-n for context.
- Reranker chỉ chạy trên fused candidates đã qua metadata và access filtering.

### 11.2 Rerank Contract

- Reranker input phải gồm:
  - rewritten query,
  - original query,
  - chunk text,
  - key metadata tối thiểu: document type, publication date, ticker, section heading.
- Reranker output phải trả:
  - rerank score,
  - final order,
  - optional rationale/debug payload cho observability.
- Nếu reranker unavailable:
  - hệ thống có thể degrade sang fused order,
  - nhưng response phải được trace rõ để phục vụ quality review.
- Không được synthesize trên candidate vượt quá access policy, dù reranker score cao.

### 11.3 Citation Preview Contract

#### 11.3.1 Citation object minimum fields

| Field | Required | Description |
| --- | --- | --- |
| `citation_id` | Yes | ID citation trong response |
| `document_id` | Yes | Logical document reference |
| `document_version_id` | Yes | Exact source version |
| `title` | Yes | Tên tài liệu |
| `source` | Yes | Nguồn tài liệu |
| `document_type` | Yes | Loại tài liệu |
| `page_number` | Conditional | Trang cần mở |
| `section_heading` | Conditional | Mục liên quan |
| `chunk_id` | Yes | Chunk source |
| `snippet` | Yes | Đoạn trích hiển thị cho user |
| `text_offset_start` | Conditional | Offset đầu |
| `text_offset_end` | Conditional | Offset cuối |
| `preview_url` | Conditional | Link preview artifact |
| `viewer_anchor` | Conditional | Anchor để frontend mở đúng vị trí |
| `version_label` | Yes | Nhãn version hiển thị |
| `confidence` | No | Mức tin cậy của citation packaging |

#### 11.3.2 Preview behavior rules

- Nếu tài liệu là PDF text-based:
  - frontend phải mở đúng `page_number`,
  - cố gắng highlight theo `viewer_anchor` hoặc text offsets.
- Nếu là scan/OCR PDF:
  - ưu tiên page-level preview,
  - nếu offset mapping không đáng tin thì hiển thị snippet + page anchor, không fake highlight.
- Nếu là DOCX/HTML/TXT:
  - preview mở canonical rendered artifact hoặc extracted text viewer với anchor tới chunk.
- Nếu citation thuộc superseded version:
  - UI phải hiển thị cảnh báo version để user biết đây không phải current version.

### 11.4 API Payload Example

```json
{
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
    "insufficient_evidence": false
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
      "preview_url": "/api/documents/doc_hpg_ar_2024/versions/docver_hpg_ar_2024_v1/preview/87",
      "viewer_anchor": "page=87&chunk=chk_009182",
      "version_label": "v1",
      "confidence": 0.91
    }
  ],
  "debug": {
    "retrieval_strategy": "dense+sparse+metadata+rerank",
    "dense_top_k": 30,
    "sparse_top_k": 30,
    "fused_top_k": 20,
    "context_top_n": 8
  }
}
```

---

## 12. Operational Considerations

### 12.1 Environments

| Environment | URL / Identifier | Purpose | Differences |
| --- | --- | --- | --- |
| Dev | Pending | Parser/retrieval development | Có thể dùng sample data và mock provider |
| Staging | Pending | Pre-production validation | Dataset kiểm soát, production-like config |
| Production | Pending | User-facing secure environment | Strict RBAC/ABAC, backup, audit |

### 12.2 CI/CD & Release Management

- **Pipeline stages:** doc review, lint/test, build, deploy, smoke test.
- **Migration strategy:** schema migration có versioning cho PostgreSQL; index migration theo batch/rebuild strategy cho Qdrant.
- **Rollback plan:** rollback app version, giữ backward compatibility ngắn hạn cho metadata schema, reindex selected documents nếu cần.

### 12.3 Observability & SRE

- **Logging:** structured logs theo request/job/document identifiers.
- **Metrics:** query latency, retrieval latency, rerank latency, generation latency, indexing latency, token usage, cost per query, citation coverage, error rate, lấy từ application logs và Langfuse traces.
- **Alerts:** MVP chỉ cần cảnh báo cho index pipeline failure, provider timeout spike, vector store outage.

**MVP note:** Chưa cần Prometheus, Grafana hoặc observability platform riêng ngoài Langfuse và log của ứng dụng. Nếu pilot chứng minh có nhu cầu scale vận hành, các stack này mới được xem xét ở giai đoạn sau.

### 12.4 Business Continuity & DR

- **Backup cadence:** daily backup cho PostgreSQL; object storage versioning/snapshot theo policy; Qdrant snapshot định kỳ.
- **Recovery Time Objective (RTO):** target pilot ≤ 8 hours.
- **Recovery Point Objective (RPO):** target pilot ≤ 24 hours.
- **Failover process:** manual failover acceptable ở pilot; automation cần bổ sung cho production.

---

## 13. Risks & Mitigations

| Risk ID | Description | Likelihood | Impact | Mitigation / Control | Residual Status |
| --- | --- | --- | --- | --- | --- |
| RISK-001 | OCR chất lượng kém làm retrieval sai | M | H | OCR quality score, manual review cho tài liệu quan trọng, ưu tiên digital-native docs | Active |
| RISK-002 | Metadata sai hoặc thiếu làm filter sai | M | H | Metadata validation, alias dictionary, review tài liệu high-value | Active |
| RISK-003 | Hallucination hoặc answer vượt quá evidence | M | H | Strict grounding, citation requirement, response validation, insufficient-evidence fallback | Active |
| RISK-004 | Scope creep từ voice/history/compare làm yếu retrieval core | H | H | Freeze Phase 1 scope theo query-first roadmap | Active |
| RISK-005 | Dữ liệu nhạy cảm bị truy cập sai do policy không đồng bộ | M | H | Retrieval-level authorization, permission sync, audit logging | Active |
| RISK-006 | Chi phí inference tăng mạnh khi scale | M | M | Smaller models cho classification/rewrite, cache hợp lý, giới hạn context/rerank depth | Monitor |
| RISK-007 | Citation mở đúng file nhưng sai version hoặc sai vị trí | M | H | Mandatory versioning + citation preview contract + offset/page anchor validation | Active |

---

## 14. Compliance & Verification Plan

| Compliance Item | Responsible Party | Evidence Required | Review Cadence |
| --- | --- | --- | --- |
| Architecture Review approval | Architect / Tech Lead | Review minutes, checklist, approved AD | Per major release |
| Security sign-off | Security Officer | Threat model, access control review, test evidence | Before production |
| Retrieval quality validation | Product Owner + QA | Golden queries, citation audit results, UAT results | Per milestone |
| Citation preview validation | QA + Product Owner | Click-through tests for page/chunk accuracy across formats | Per milestone |
| Data retention validation | DevOps + Security | Logging/retention config and audit evidence | Quarterly |
| ADR currency | Tech Lead | ADR index review and updates | Quarterly |

---

## 15. Appendices

- **Appendix A:** Suggested next documents
  - SRS for Phase 1 query foundation
  - ADR files for hybrid retrieval contract, authorization at retrieval stage, no-history Phase 1 scope, mandatory versioning
  - API Design for Query/Search/Upload/Citation/Document APIs
  - Data Model for PostgreSQL and Qdrant payload
  - Security & Privacy Plan
- **Appendix B:** Phase Roadmap

| Phase | Name | Scope Summary |
| --- | --- | --- |
| 1 | Query Foundation | ingest, parse/chunk, metadata, hybrid retrieval, metadata filter, rerank, answer with citation, preview nguồn |
| 2 | Analyst Productivity | compare mode, timeline extraction, risk/thesis extraction, recent query memory nếu thực sự cần |
| 3 | Enterprise Intelligence | watchlist alerts, collaborative workspace, advanced policy, quality dashboard, user analytics |

- **Appendix C:** Change Log

| Version | Date | Author | Summary |
| --- | --- | --- | --- |
| 0.3 | 2026-04-12 | OpenAI Codex | Added metadata contract, mandatory versioning, hybrid retrieval/rerank contract, citation preview contract |
| 0.2 | 2026-04-12 | OpenAI Codex | Initial architecture draft aligned to Phase 1 query-first scope |

---

## 16. Approvals

| Role | Name | Signature | Date |
| --- | --- | --- | --- |
| Product Owner (Approve) | Pending | Pending | Pending |
| Tech Lead / Architect (Approve) | Pending | Pending | Pending |
| Security Officer (Concur) | Pending | Pending | Pending |
| DevOps Lead (Concur) | Pending | Pending | Pending |
| Quality Manager (Informed) | Pending | Pending | Pending |

---

**Distribution:** Store the approved version in the project knowledge base and link it from SRS, ADR index, API design, data model, and security plan once those documents are created.
