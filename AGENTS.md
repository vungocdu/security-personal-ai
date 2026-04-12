# AGENTS.md

## Project

- Project name: `security-personal-ai`
- Product direction: Personal AI Agent điều khiển bằng giọng nói cho chuyên gia trong ngành chứng khoán
- Primary goal: giúp người dùng tìm, trích xuất, tóm tắt và đối chiếu thông tin từ tài liệu lưu trong thư mục cá nhân mà không phải mở từng file thủ công

## Product Summary

Ứng dụng này không phải chatbot chung chung.

Đây là một trợ lý cá nhân chuyên xử lý tri thức tài chính, báo cáo, bài báo, bảng số liệu và tài liệu làm việc của một chuyên gia chứng khoán. Hệ thống ưu tiên:

- tra cứu nhanh bằng giọng nói hoặc văn bản
- trích xuất dữ liệu từ `pdf`, `docx`, `xlsx`, bài báo và tài liệu text
- trả lời có căn cứ từ tài liệu nguồn
- hỗ trợ so sánh, tóm tắt, gom ý chính và tìm số liệu quan trọng
- bảo vệ dữ liệu riêng tư, ưu tiên xử lý trong phạm vi thư mục cục bộ của người dùng

## Core User

- Chuyên gia phân tích chứng khoán
- Chuyên gia tư vấn đầu tư
- Người quản lý danh mục cá nhân hoặc khách hàng
- Người thường xuyên đọc báo cáo doanh nghiệp, tin tức thị trường và file tổng hợp số liệu

## Business Capabilities

Hệ thống cần hỗ trợ 6 nhóm năng lực chính:

1. Ingest tài liệu từ thư mục người dùng.
2. Chuyển tài liệu nhiều định dạng về text chuẩn hóa để tìm kiếm và phân tích.
3. Tìm kiếm ngữ nghĩa và tìm kiếm từ khóa trên toàn bộ kho tài liệu.
4. Trích xuất dữ liệu quan trọng như mã cổ phiếu, doanh thu, lợi nhuận, EPS, kỳ báo cáo, giá mục tiêu, rủi ro nổi bật.
5. Tương tác bằng giọng nói để hỏi nhanh, ra lệnh nhanh và nghe câu trả lời ngắn gọn.
6. Tạo câu trả lời có dẫn chiếu theo tài liệu gốc để người dùng dễ kiểm chứng.

## System Design Baseline

Thiết kế nền tảng hiện tại bám theo mô hình nhiều lớp:

1. `Voice Gateway`
   Nhận lệnh giọng nói, chuyển giọng nói thành văn bản, đọc lại câu trả lời.

2. `Agent Orchestrator`
   Xác định ý định người dùng, chọn workflow phù hợp như tìm kiếm, trích xuất, tóm tắt, so sánh hoặc lập brief.

3. `Ingestion Gateway`
   Theo dõi thư mục nguồn và đọc tài liệu đầu vào từ `pdf`, `docx`, `xlsx`, `html`, `md`, `txt`.

4. `Normalization Layer`
   Chuẩn hóa nội dung, chia section, gắn metadata và tạo text canonical.

5. `Fact Extraction Layer`
   Trích xuất dữ liệu định lượng và thực thể nghiệp vụ quan trọng cho domain chứng khoán.

6. `Retrieval Layer`
   Dùng QMD làm lõi hybrid retrieval cho corpus text đã chuẩn hóa.

7. `Structured Data Store`
   Lưu metadata tài liệu, section, fact extraction, entity chứng khoán, lịch sử agent run.

## Expected Technical Architecture

- Retrieval engine: ưu tiên tái sử dụng `qmd` cho BM25, vector search, query expansion, rerank, MCP bridge.
- Structured persistence: dùng SQLite hoặc PostgreSQL cho metadata và extracted facts.
- File-first ingestion: không thao tác trực tiếp trên file nguồn ngoài việc đọc và theo dõi thay đổi.
- Agent answer strategy:
  - facts trước nếu câu hỏi cần số liệu
  - retrieval narrative sau nếu cần diễn giải
- Privacy-first:
  - tài liệu người dùng là dữ liệu nhạy cảm
  - không gửi corpus gốc lên dịch vụ ngoài nếu chưa có chấp thuận rõ ràng

## Initial Modules

- `watcher`
  Theo dõi thư mục và hàng đợi ingest.

- `parsers`
  Parser riêng cho `pdf`, `docx`, `xlsx`, `html`, `md`, `txt`.

- `normalizer`
  Chuẩn hóa text, section, heading, table block, metadata.

- `extractor`
  Rule-based và model-assisted extraction cho dữ liệu chứng khoán.

- `retrieval`
  Adapter kết nối QMD với kho dữ liệu của dự án.

- `agent`
  Intent router, planner, answer composer.

- `voice`
  STT, TTS, push-to-talk, session state.

- `ui`
  Giao diện desktop hoặc web nội bộ cho truy vấn, xem nguồn, xem summary.

## Data Model Direction

Ít nhất phải có các nhóm dữ liệu sau:

- `files`
- `documents`
- `document_sections`
- `extracted_facts`
- `companies`
- `tickers`
- `voice_sessions`
- `agent_runs`

Không thiết kế data model kiểu generic quá mức.

Domain chứng khoán cần các field rõ nghĩa như:

- `ticker`
- `company_name`
- `reporting_period`
- `metric_name`
- `metric_value`
- `unit`
- `published_at`
- `source_type`
- `confidence`

## Delivery Priorities

Giai đoạn 1, chỉ cần làm tốt:

1. đọc file từ thư mục
2. parse và chuẩn hóa
3. tìm kiếm và hỏi đáp trên tài liệu
4. trích xuất một số dữ liệu tài chính cốt lõi
5. voice command ở mức push-to-talk

Chưa cần làm ngay:

- trading integration
- portfolio optimization engine
- alerting thời gian thực từ market feed
- workflow cộng tác nhiều người dùng

## Documentation Rules

- Tài liệu business-facing đặt trong `doc/01-Requirements/BRD/`
- Tài liệu software requirement chi tiết đặt trong `doc/01-Requirements/SRS/`
- Kiến trúc hệ thống đặt trong `doc/02-Architecture/AD/`
- LLD theo module đặt trong `doc/05-LLD/`
- Mọi tài liệu mới nên viết theo hướng:
  - business trước
  - system behavior sau
  - technical detail cuối cùng

## Writing Rules For Future AI/Dev Work

- Luôn phân biệt rõ:
  - business requirement
  - system requirement
  - technical design
- Không biến BRD thành tài liệu kỹ thuật.
- Khi nói về tính năng, luôn nêu:
  - người dùng nào cần
  - vấn đề gì đang tồn tại
  - đầu ra giá trị là gì
- Với domain chứng khoán, ưu tiên tính đúng, khả năng kiểm chứng và trace về nguồn hơn là câu trả lời nghe tự nhiên.
- Nếu có dùng AI/LLM ở bước extraction hoặc summary, phải thiết kế để người dùng xem lại nguồn gốc thông tin.

## Near-Term Document Roadmap

Sau BRD sơ bộ này, nên tạo tiếp:

1. SRS cho MVP
2. Architecture Design cho ingest, retrieval, voice, fact extraction
3. Data model chi tiết
4. Security and privacy plan
5. LLD cho `parsers`, `extractor`, `retrieval adapter`, `voice gateway`
