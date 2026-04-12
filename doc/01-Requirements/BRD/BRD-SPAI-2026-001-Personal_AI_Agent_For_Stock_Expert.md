# Business Requirements Document (BRD)

**MERCURY SOLUTIONS**  
**Software Engineering Excellence**

---

## DOCUMENT CONTROL

| Field | Value |
| --- | --- |
| **Document ID** | BRD-SPAI-2026-001 |
| **Template Version** | 1.0 |
| **Document Version** | 0.1 |
| **Project Name** | Security Personal AI |
| **Document Status** | Draft |
| **Classification** | Confidential |
| **Author** | OpenAI Codex, AI Business Draft |
| **Creation Date** | 2026-04-10 |
| **Last Updated** | 2026-04-10 |
| **Approved By** | Pending |
| **Approval Date** | Pending |
| **Next Review Date** | 2026-04-24 |
| **AI-Assisted** | [x] Yes - Tool: **Codex** |

---

## 1. EXECUTIVE SUMMARY

Security Personal AI là ý tưởng về một trợ lý AI cá nhân điều khiển bằng giọng nói dành cho một chuyên gia trong ngành chứng khoán. Ứng dụng giúp người dùng đọc hiểu nhanh hơn khối lượng lớn tài liệu làm việc như báo cáo PDF, file Word, file Excel, bài báo, ghi chú và tài liệu text đang lưu rải rác trong các thư mục cá nhân.

Thay vì phải mở từng file, tìm bằng tay rồi tự tổng hợp, người dùng có thể hỏi trực tiếp bằng giọng nói hoặc văn bản để tìm tài liệu, trích xuất số liệu quan trọng, tóm tắt ý chính, so sánh thông tin giữa nhiều tài liệu và xem lại nguồn tham chiếu gốc. Giá trị chính của hệ thống là tiết kiệm thời gian nghiên cứu, giảm bỏ sót thông tin quan trọng và tạo ra một cách làm việc nhanh hơn, tự nhiên hơn cho chuyên gia phân tích chứng khoán.

---

## 2. BUSINESS CONTEXT

### 2.1 Current Business Situation

**Current State:**

- Chuyên gia chứng khoán thường làm việc với nhiều loại tài liệu khác nhau như báo cáo doanh nghiệp, tin tức thị trường, file tổng hợp số liệu và ghi chú nội bộ.
- Tài liệu nằm rải rác trong nhiều thư mục và nhiều định dạng khác nhau, khiến việc tra cứu và tổng hợp mất thời gian.
- Khi cần trả lời nhanh một câu hỏi như doanh thu quý gần nhất, rủi ro chính của doanh nghiệp hoặc thay đổi trong triển vọng ngành, người dùng thường phải mở nhiều file và đọc thủ công.
- Quá trình tổng hợp hiện tại phụ thuộc nhiều vào trí nhớ cá nhân và thao tác tay, nên dễ bỏ sót dữ liệu hoặc mất dấu nguồn tham chiếu.

**Drivers for Change:**

- [x] Customer demand
- [x] Operational efficiency
- [x] Technology opportunity
- [x] Personal productivity improvement
- [ ] Regulatory compliance
- [ ] Technology obsolescence
- [ ] Other

### 2.2 Industry and Market Analysis

- **Market Trends:** Chuyên gia tài chính ngày càng cần xử lý lượng thông tin lớn hơn trong thời gian ngắn hơn. AI assistant và voice interaction đang trở thành cách tiếp cận tự nhiên để tăng tốc nghiên cứu cá nhân.
- **Competitive Landscape:** Nhiều công cụ AI hiện nay mạnh về hỏi đáp chung, nhưng chưa tối ưu cho việc đọc tài liệu cá nhân đa định dạng, truy ngược nguồn và phục vụ chuyên gia chứng khoán theo workflow thực tế.
- **User Reality:** Người dùng mục tiêu không cần một nền tảng phân tích thị trường khổng lồ ngay từ đầu. Họ cần một trợ lý cá nhân đáng tin, hiểu thư mục tài liệu của họ và giúp họ lấy thông tin đúng nhanh hơn.

### 2.3 Organizational Alignment

- Dự án phù hợp với định hướng xây dựng các ứng dụng AI có giá trị thực tế, bám sát workflow chuyên môn.
- Dự án có thể là bước đầu để phát triển thêm các giải pháp AI vertical cho tài chính, đầu tư và nghiên cứu doanh nghiệp.
- Phiên bản đầu tiên tập trung vào use case cá nhân, dễ thử nghiệm với người dùng thật và dễ điều chỉnh theo phản hồi thực tế.

---

## 3. BUSINESS OBJECTIVES

### 3.1 Primary Objectives

| Objective ID | Objective Statement | Success Metric | Target Value | Target Date | Owner |
| --- | --- | --- | --- | --- | --- |
| BO-001 | Giảm thời gian tìm tài liệu liên quan đến một câu hỏi chuyên môn | Thời gian từ lúc hỏi đến lúc thấy tài liệu phù hợp | Giảm ít nhất 70% so với cách thủ công | 2026-07-31 | Project Sponsor |
| BO-002 | Giảm thời gian tổng hợp ý chính từ nhiều tài liệu | Thời gian tạo bản tóm tắt nghiên cứu sơ bộ | Giảm ít nhất 60% | 2026-07-31 | Product Owner |
| BO-003 | Tăng khả năng truy xuất số liệu và thông tin có nguồn gốc rõ ràng | Tỷ lệ câu trả lời có dẫn chiếu nguồn | Từ 80% trở lên | 2026-07-31 | Product Owner |

### 3.2 Secondary Objectives

| Objective ID | Objective Statement | Success Metric | Target Value | Target Date | Owner |
| --- | --- | --- | --- | --- | --- |
| BO-101 | Tạo trải nghiệm tra cứu tự nhiên bằng giọng nói | Tỷ lệ truy vấn voice được xử lý thành công | Từ 85% trở lên trong phạm vi lệnh hỗ trợ | 2026-08-31 | Product Owner |
| BO-102 | Hỗ trợ người dùng rà soát nhanh các dữ liệu tài chính quan trọng trong tài liệu | Số loại dữ liệu cốt lõi được trích xuất ở MVP | Ít nhất 8 loại dữ liệu | 2026-08-31 | Business Analyst |

---

## 4. STAKEHOLDER ANALYSIS

### 4.1 Stakeholder Identification

| Stakeholder ID | Name/Role | Organization/Group | Interest | Influence | Engagement Strategy |
| --- | --- | --- | --- | --- | --- |
| STK-001 | Chuyên gia chứng khoán sử dụng hệ thống | End User | High | High | Phỏng vấn, demo, feedback theo tuần |
| STK-002 | Product Owner | Delivery Team | High | High | Chốt scope, ưu tiên chức năng, review tài liệu |
| STK-003 | Business Analyst | Delivery Team | High | Medium | Làm rõ nghiệp vụ, xác nhận use case, viết requirement |
| STK-004 | Technical Lead | Delivery Team | Medium | High | Đánh giá khả năng triển khai và lộ trình kỹ thuật |

### 4.2 Stakeholder Needs and Expectations

| Stakeholder ID | Primary Needs | Expectations | Success Criteria | Concerns/Risks |
| --- | --- | --- | --- | --- |
| STK-001 | Tìm đúng tài liệu và số liệu nhanh | Hỏi ít, ra kết quả nhanh, có nguồn kiểm tra | Câu trả lời hữu ích, tiết kiệm thời gian thật | Thông tin sai, thiếu nguồn, khó dùng |
| STK-002 | Có MVP rõ ràng, dễ demo với khách hàng | Chức năng đủ để chứng minh giá trị | Demo được workflow thực tế | Scope quá rộng từ đầu |
| STK-003 | Requirement rõ, tránh mơ hồ | Phân biệt rõ business và technical scope | BRD/SRS dễ đọc, dễ chuyển xuống thiết kế | Tài liệu bị sa đà kỹ thuật |
| STK-004 | Kiến trúc hợp lý, có đường đi ngắn tới MVP | Có khả năng triển khai theo từng giai đoạn | Xây được bản đầu nhanh, có chỗ mở rộng | Over-engineering quá sớm |

---

## 5. BUSINESS REQUIREMENTS

### 5.1 Functional Business Requirements

| Requirement ID | Requirement Statement | Business Value | Priority | Acceptance Criteria |
| --- | --- | --- | --- | --- |
| BR-FN-001 | Hệ thống phải cho phép người dùng kết nối và đọc tài liệu từ thư mục cá nhân được chỉ định | Tận dụng ngay tài liệu đang có, không phải nhập tay | Must Have | Người dùng chọn được thư mục và hệ thống nhận diện được các file hỗ trợ |
| BR-FN-002 | Hệ thống phải hỗ trợ đọc nội dung từ các định dạng tài liệu phổ biến gồm PDF, Word, Excel và bài báo/text file | Bao phủ đúng workflow nghiên cứu hiện tại | Must Have | Có thể lấy nội dung từ tối thiểu 4 nhóm định dạng tài liệu chính |
| BR-FN-003 | Hệ thống phải cho phép người dùng hỏi bằng văn bản hoặc giọng nói để tìm tài liệu liên quan | Tăng tốc tra cứu, giảm thao tác tay | Must Have | Người dùng gửi câu hỏi và nhận được danh sách kết quả phù hợp |
| BR-FN-004 | Hệ thống phải trả lời tóm tắt ngắn gọn từ một hoặc nhiều tài liệu liên quan | Tiết kiệm thời gian đọc và tổng hợp | Must Have | Hệ thống tạo được bản tóm tắt sơ bộ kèm nguồn tham chiếu |
| BR-FN-005 | Hệ thống phải cho phép trích xuất các dữ liệu quan trọng từ tài liệu như doanh thu, lợi nhuận, EPS, kỳ báo cáo hoặc chỉ tiêu liên quan | Giảm thời gian tìm số liệu và đối chiếu thủ công | Must Have | Người dùng yêu cầu trích xuất và nhận được kết quả có nêu rõ nguồn |
| BR-FN-006 | Hệ thống phải cho phép so sánh thông tin giữa nhiều tài liệu hoặc nhiều kỳ báo cáo | Hỗ trợ phân tích biến động và đối chiếu nhận định | Should Have | Người dùng chọn hoặc hỏi nhiều tài liệu và nhận được bảng so sánh hoặc summary so sánh |
| BR-FN-007 | Hệ thống phải hiển thị hoặc dẫn chiếu lại nguồn gốc của câu trả lời | Tăng độ tin cậy và khả năng kiểm chứng | Must Have | Mỗi câu trả lời quan trọng có ít nhất một nguồn tham chiếu đi kèm |
| BR-FN-008 | Hệ thống phải hỗ trợ danh sách lệnh voice cơ bản như tìm tài liệu, tóm tắt, trích xuất số liệu và đọc lại kết quả | Tạo trải nghiệm hands-free tự nhiên hơn | Should Have | Người dùng dùng được bộ lệnh voice MVP đã định nghĩa |
| BR-FN-009 | Hệ thống phải ghi nhớ lịch sử phiên hỏi đáp gần nhất để người dùng nối tiếp câu hỏi | Giảm lặp lại câu hỏi và tăng tính tự nhiên | Could Have | Người dùng hỏi tiếp theo ngữ cảnh gần nhất và hệ thống xử lý đúng trong phạm vi phiên làm việc |

### 5.2 Non-Functional Business Requirements

| Requirement ID | Category | Requirement Statement | Target Value | Acceptance Criteria |
| --- | --- | --- | --- | --- |
| BR-NF-001 | Performance | Truy vấn tìm kiếm cơ bản phải phản hồi đủ nhanh để phù hợp với workflow làm việc hằng ngày | Kết quả sơ bộ trong vòng 5 giây cho truy vấn phổ biến | Đo trong môi trường pilot |
| BR-NF-002 | Accuracy | Kết quả trích xuất và tóm tắt phải có khả năng kiểm chứng từ nguồn gốc | 100% kết quả quan trọng có nguồn tham chiếu | Kiểm tra qua UAT |
| BR-NF-003 | Privacy | Tài liệu người dùng phải được xử lý theo nguyên tắc bảo mật và riêng tư | Chỉ xử lý trong phạm vi được người dùng cấp quyền | Xác nhận trong thiết kế và UAT |
| BR-NF-004 | Usability | Người dùng không rành kỹ thuật vẫn có thể hiểu cách dùng cơ bản | Người dùng pilot thao tác được sau buổi hướng dẫn ngắn | UAT với người dùng thật |
| BR-NF-005 | Scalability | Hệ thống phải xử lý được kho tài liệu cá nhân tăng dần theo thời gian | Hỗ trợ vài nghìn tài liệu trong giai đoạn đầu | Kiểm tra qua pilot dataset |
| BR-NF-006 | Auditability | Kết quả trả lời cần có khả năng truy ngược về tài liệu nguồn | Có thể xem file nguồn hoặc đoạn nguồn liên quan | Demo/UAT xác nhận được |

### 5.3 Business Process Requirements

| Process ID | Process Name | Current State | Desired Future State | Impact |
| --- | --- | --- | --- | --- |
| BP-001 | Tìm tài liệu phục vụ phân tích | Người dùng tự nhớ vị trí file, mở nhiều tài liệu và tìm tay | Người dùng hỏi trực tiếp, hệ thống trả kết quả theo mức độ liên quan | High |
| BP-002 | Tổng hợp ý chính từ nhiều tài liệu | Người dùng đọc và tự viết summary thủ công | Hệ thống tạo summary sơ bộ để người dùng rà soát và dùng tiếp | High |
| BP-003 | Tìm và đối chiếu số liệu | Người dùng tìm trong PDF/Excel bằng mắt hoặc copy sang nơi khác | Hệ thống trích xuất và trả lại số liệu cùng nguồn | High |
| BP-004 | Xử lý câu hỏi nhanh khi đang làm việc | Người dùng phải ngừng việc hiện tại để mở file và tìm thông tin | Người dùng hỏi bằng giọng nói hoặc văn bản ngay trong phiên làm việc | Medium |

---

## 6. SUCCESS CRITERIA

### 6.1 Measurable Success Criteria

| Criterion ID | Success Criterion | Baseline Value | Target Value | Measurement Method | Measurement Frequency |
| --- | --- | --- | --- | --- | --- |
| SC-001 | Thời gian tìm được tài liệu phù hợp cho một câu hỏi cụ thể | Thủ công, thường mất nhiều phút | Giảm tối thiểu 70% | UAT theo kịch bản thực tế | Theo đợt pilot |
| SC-002 | Thời gian tạo summary sơ bộ cho một chủ đề hoặc doanh nghiệp | Thủ công, phải đọc nhiều file | Giảm tối thiểu 60% | So sánh trước và sau pilot | Theo đợt pilot |
| SC-003 | Tỷ lệ câu trả lời có nguồn tham chiếu rõ ràng | Chưa có hệ thống | Từ 80% trở lên | Review mẫu kết quả | Hằng tuần trong pilot |
| SC-004 | Mức hài lòng của người dùng pilot | Chưa có | Từ 8/10 trở lên | Phỏng vấn và survey | Cuối pilot |

### 6.2 Acceptance Criteria

Dự án được xem là thành công ở mức MVP khi:

- [ ] Người dùng có thể kết nối thư mục tài liệu cá nhân và hệ thống đọc được các file hỗ trợ
- [ ] Người dùng có thể hỏi để tìm tài liệu liên quan
- [ ] Người dùng có thể yêu cầu tóm tắt nội dung từ một hoặc nhiều tài liệu
- [ ] Người dùng có thể yêu cầu trích xuất một số dữ liệu tài chính cốt lõi
- [ ] Kết quả quan trọng có dẫn chiếu nguồn
- [ ] Có thể demo ít nhất 3 workflow thực tế của chuyên gia chứng khoán

---

## 7. CONSTRAINTS AND ASSUMPTIONS

### 7.1 Constraints

- Giai đoạn đầu ưu tiên giá trị sử dụng thực tế cho một chuyên gia cụ thể, không mở rộng ngay thành nền tảng cho nhiều người dùng.
- Phạm vi MVP tập trung vào tài liệu có sẵn trong thư mục cá nhân, chưa bao gồm dữ liệu market feed thời gian thực.
- Chất lượng đầu ra phụ thuộc vào chất lượng file nguồn và khả năng đọc được nội dung từ từng định dạng.
- Voice interaction trong giai đoạn đầu nên giới hạn ở tập lệnh rõ ràng, chưa kỳ vọng hội thoại quá mở.

### 7.2 Assumptions

- Người dùng mục tiêu có sẵn một kho tài liệu cá nhân đủ lớn để tạo giá trị ngay khi ingest.
- Người dùng chấp nhận thử nghiệm pilot để tinh chỉnh bộ câu hỏi, cách tóm tắt và loại dữ liệu cần trích xuất.
- Nhu cầu đầu tiên là productivity cá nhân, chưa phải cộng tác nhóm.
- Người dùng ưu tiên tốc độ tra cứu và khả năng kiểm chứng hơn là giao diện phức tạp.

---

## 8. RISKS AND DEPENDENCIES

### 8.1 Key Risks

| Risk ID | Risk Description | Impact | Mitigation Direction |
| --- | --- | --- | --- |
| R-001 | Một số file PDF hoặc Excel khó đọc tự động | High | Chọn rõ phạm vi file hỗ trợ tốt ở MVP và xử lý ngoại lệ |
| R-002 | Kết quả AI có thể tóm tắt chưa đúng ý người dùng trong một số trường hợp | High | Luôn kèm nguồn tham chiếu và cho phép người dùng kiểm tra lại |
| R-003 | Scope dễ mở rộng quá nhanh sang tính năng phân tích đầu tư chuyên sâu | High | Chốt rõ MVP là trợ lý tra cứu và trích xuất thông tin |
| R-004 | Voice interaction có thể gây kỳ vọng quá cao ngay từ đầu | Medium | Giới hạn tập lệnh voice trong giai đoạn đầu |

### 8.2 Dependencies

- Có tập tài liệu mẫu của khách hàng để xác thực workflow thật.
- Có thời gian làm workshop ngắn với người dùng chuyên gia để chốt các use case ưu tiên.
- Có danh sách dữ liệu tài chính nào là quan trọng nhất với người dùng trong giai đoạn đầu.

---

## 9. BUSINESS CASE

### 9.1 Expected Benefits

- Tiết kiệm đáng kể thời gian tìm kiếm và tổng hợp thông tin.
- Giảm rủi ro bỏ sót tài liệu hoặc số liệu quan trọng.
- Tăng tốc quá trình chuẩn bị phân tích, trao đổi hoặc ra quyết định.
- Tạo nền tảng để mở rộng sau này sang trợ lý nghiên cứu ngành hoặc trợ lý đầu tư cá nhân hóa.

### 9.2 Investment Logic

Dự án có giá trị vì tập trung vào một pain point rất cụ thể và lặp lại hằng ngày: chuyên gia chứng khoán phải đọc quá nhiều tài liệu và mất quá nhiều thời gian để tìm đúng thông tin. Nếu hệ thống giúp giảm thời gian tra cứu và tổng hợp ngay trong workflow thực tế, giá trị mang lại sẽ rất rõ ràng dù phiên bản đầu chưa cần bao phủ toàn bộ bài toán đầu tư.

### 9.3 Recommended Scope for MVP

MVP nên tập trung vào:

1. đọc tài liệu từ thư mục cá nhân
2. hỗ trợ các định dạng tài liệu chính
3. tìm kiếm và hỏi đáp trên tài liệu
4. tóm tắt nội dung
5. trích xuất dữ liệu tài chính cơ bản
6. voice command ở mức cơ bản

Không nên đưa vào MVP:

- cảnh báo giao dịch thời gian thực
- kết nối broker
- khuyến nghị đầu tư tự động
- workflow nhiều người dùng

---

## 10. APPROVAL

| Role | Name | Decision | Date | Signature |
| --- | --- | --- | --- | --- |
| Executive Sponsor | Pending | Pending | Pending | Pending |
| Product Owner | Pending | Pending | Pending | Pending |
| Customer Representative | Pending | Pending | Pending | Pending |

---

## 11. APPENDICES

### Appendix A - Example User Questions

- “Tóm tắt nhanh báo cáo quý gần nhất của FPT.”
- “Trong các tài liệu về VCB, tìm giúp tôi các đoạn nói về chất lượng tài sản.”
- “Trích xuất doanh thu, lợi nhuận sau thuế và EPS từ báo cáo này.”
- “So sánh nhận định của hai báo cáo phân tích về triển vọng ngành thép.”
- “Đọc cho tôi 3 rủi ro chính được nhắc đến trong tài liệu này.”

### Appendix B - Initial Feature List for Customer Discussion

- Kết nối thư mục tài liệu cá nhân
- Đọc nhiều định dạng file
- Tìm kiếm theo câu hỏi tự nhiên
- Tóm tắt tài liệu
- Trích xuất số liệu quan trọng
- So sánh thông tin giữa nhiều tài liệu
- Truy nguồn về file gốc
- Hỏi đáp bằng giọng nói
- Đọc lại câu trả lời bằng giọng nói
