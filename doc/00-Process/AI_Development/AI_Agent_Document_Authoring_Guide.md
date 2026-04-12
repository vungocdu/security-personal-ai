# AI Agent Document Authoring Guide (ISO‑Aligned)

**Applies to**: ActiveSG documentation in `ISO_Doc_Kit_ActiveSG`  
**Standards**: ISO/IEC/IEEE 29148 (Requirements), 42010 (Architecture), 12207/15288 (Lifecycle), 25010 (Quality)

---

## 0) TL;DR — 10 Quy tắc vàng

1. **Đúng chuẩn**: bám cấu trúc ISO đã định; không tự ý đổi thư mục/định danh.
2. **Định danh ổn định**: REQ/ADR/TEST/RISK/CHG… không đổi sau khi baseline.
3. **Truy vết 2 chiều**: mọi REQ phải có Test/Design/API/DB liên kết trong _Traceability_Matrix.md_.
4. **Đo lường được**: NFR có metric, đơn vị, mục tiêu và cách đo (SLO/SLI).
5. **Không mơ hồ**: tránh “nhanh”, “tối ưu”, “linh hoạt” nếu không có số liệu.
6. **An toàn & PII**: phân loại dữ liệu, RBAC theo endpoint, kế hoạch retention.
7. **Hợp đồng API = nguồn chân lý**: OpenAPI luôn cập nhật trước code/client.
8. **Change qua CR**: mọi thay đổi lớn đi qua _TEMPLATE-LC-002-Change_Impact_Assessment.md_ → Release Notes.
9. **Kiểm tra chất lượng**: chạy _Quality Gate Checklist_ trước khi hoàn tất.
10. **Nhất quán**: tên tệp, heading, bảng, ví dụ—đồng bộ xuyên suốt.

---

## 1) Phạm vi & Chuẩn tham chiếu

- **ISO/IEC/IEEE 29148** — SRS, NFR, truy vết yêu cầu.
- **ISO/IEC/IEEE 42010** — AD: stakeholders, concerns, viewpoints/views, ADRs.
- **ISO/IEC/IEEE 12207/15288** — Quy trình vòng đời, V&V/Test, Change/Release, vận hành.
- **ISO/IEC 25010** — Khung chất lượng sản phẩm (security, performance, reliability, usability…).

---

## 2) Thư mục & Quy ước đặt tên

- **Nơi viết**: dùng đúng thư mục trong bộ kit.
- **Quy ước ID** (không trùng – tăng dần, 3 chữ số):
  - Yêu cầu: `REQ-<AREA>-NNN` (vd: `REQ-AUTH-001`)
  - Quyết định kiến trúc: `ADR-NNN`
  - Kiểm thử: `TEST-<AREA>-NNN`
  - Rủi ro: `RISK-NNN`
  - Thay đổi: `CHG-YYYY-NNN`
- **Tệp chính**: một artifact = một tệp/nhóm tệp tương ứng trong thư mục chuẩn (xem Mục 4).

---

## 3) Header chuẩn cho mọi tài liệu

Ở đầu mỗi tệp `.md` thêm block metadata:

```
**Title**: <Document Title>
**Doc-ID**: <TYPE>-<ID or NA>
**Owner**: <Role/Name>
**Version**: <x.y>  **Status**: Draft/Review/Approved  **Last Updated**: <YYYY-MM-DD>
**Related**: REQ-..., ADR-..., TEST-..., CHG-...
```

> _Doc-ID_ có thể để `NA` nếu không áp dụng (ví dụ Runbook).

---

## 4) Quy tắc biên soạn theo từng artifact

### 4.1 SRS (01-Requirements/SRS/MS_SRS_Template.md)

- Điền đủ mục 1→8 theo 29148.
- **FR** (4.1) & **NFR** (4.2) phải có _Acceptance Criteria_.
- **Data Requirements** (4.4): phân loại PII/PHI & liên kết _TEMPLATE-ARCH-301-Data_Retention_Matrix.md_.
- Cập nhật _Traceability_Matrix.md_ sau mỗi bổ sung REQ.

### 4.2 Traceability (01-Requirements/Traceability_Matrix.md)

- Mỗi `REQ-*` phải liệt kê: Design (AD/LLD), API, DB, Test.
- Không để trống cột _Status_ (Draft/In Progress/Done).

### 4.3 NFR Criteria (01-Requirements/NFR_Criteria.md)

- Định nghĩa metric, mục tiêu, cách đo và công cụ (APM/log/trace).

### 4.4 AD & ADR (02-Architecture/AD, 02-Architecture/ADR)

- AD: mô tả viewpoints (Context/Container/Component/Deployment/Runtime), stakeholders & concerns.
- ADR: dùng _TEMPLATE-ARCH-101-Architecture_Decision_Record.md_; đảm bảo _Links_ trỏ tới REQ/Issue.

### 4.5 Data Model (02-Architecture/Data_Model/...)

- Logical/Physical, ràng buộc, index, phân vùng, phân loại dữ liệu.
- Chính sách migration & tương thích ngược.

### 4.6 API Design & OpenAPI (02-Architecture/API/...)

- _TEMPLATE-ARCH-102-API_Design.md_: nguyên tắc versioning, idempotency, lỗi.
- _OpenAPI_Guide.md_: OpenAPI là **nguồn chân lý**; mọi thay đổi API → cập nhật spec trước.

### 4.7 Security & Privacy (02-Architecture/Security_Privacy/...)

- Threat model ngắn gọn, AuthN/AuthZ, nhật ký/audit.
- _RBAC_Matrix_By_Endpoint.md_: role→permission→field-level.
- PII masking & retention links.

### 4.8 Data Retention (02-Architecture/Data_Retention/...)

- Bảng retention theo entity; quy trình xóa (soft→hard purge) & căn cứ pháp lý.

### 4.9 Risk Register (02-Architecture/TEMPLATE-ARCH-501-Risk_Register.md)

- Rủi ro ở mức dự án/sản phẩm, chủ sở hữu & biện pháp giảm thiểu.

### 4.10 V&V/Test (03-Lifecycle/Test/TEMPLATE-LC-011-Test_Plan_VnV.md)

- Loại test, môi trường, dữ liệu test, entry/exit, báo cáo.
- Map `TEST-*` tới `REQ-*` trong Traceability Matrix.

### 4.11 CI/CD (03-Lifecycle/CICD/TEMPLATE-LC-001-CI_CD_Strategy.md)

- Pipeline, kiểm tra tĩnh, contract test, artifact, chiến lược deploy (blue/green/canary).

### 4.12 Deployment (03-Lifecycle/Deployment/TEMPLATE-LC-005-Deployment_Plan.md)

- Tiền kiểm (migrate, secrets), bước triển khai, smoke test, rollback.

### 4.13 Runbook (03-Lifecycle/Runbook/TEMPLATE-LC-009-Operational_Runbook.md)

- Lịch trực/on-call, quy trình incident, backup/khôi phục (RTO/RPO).

### 4.14 Observability (03-Lifecycle/Observability/TEMPLATE-LC-008-SLO_SLI_Plan.md)

- SLI/SLO theo service, dashboard, alert & leo thang.

### 4.15 Change & Release (03-Lifecycle/ChangeMgmt/...)

- Tạo _TEMPLATE-LC-002-Change_Impact_Assessment.md_ cho mỗi thay đổi đáng kể (ID `CHG-YYYY-NNN`).
- Cập nhật _TEMPLATE-LC-003-Release_Notes.md_ theo phiên bản phát hành.

### 4.16 Config & Env (03-Lifecycle/Config_Env/TEMPLATE-LC-004-Configuration_Management.md)

- ENV & secrets, xoay vòng, phát hiện trôi cấu hình.

### 4.17 Go-Live (03-Lifecycle/GoLive/TEMPLATE-LC-007-Go_Live_Checklist.md)

- Hoàn tất điều kiện sẵn sàng; xác nhận SLO ở staging.

### 4.18 Supporting (04-Supporting/...)

- _Naming_Repo_Conventions.md_: quy ước repo/nhánh/commit/tag.
- Accessibility, DR/Backup, User/Admin Manuals.

### 4.19 LLD (05-LLD/Module_Template/…)

- _TEMPLATE-LLD-001-Module_Design.md_: trình tự xử lý, thành phần, API, dữ liệu, hiệu năng, bảo mật, observability.
- _TEMPLATE-LLD-002-Class_Diagram.md_: cấu trúc lớp, quan hệ, trách nhiệm.
- _TEMPLATE-LLD-003-Calculation_Logic.md_: công thức/báo cáo/kho dữ liệu.
- _TEMPLATE-LLD-004-Sequence_Diagram.md_: luồng tương tác, luồng lỗi & ngoại lệ.

---

## 5) Quy tắc Truy vết (bắt buộc)

- `REQ-*` → phải có: `TEST-*`, _Design Ref_ (AD/LLD), _API Spec_, _DB Schema_.
- Ví dụ dòng trong _Traceability_Matrix.md_:

```
REQ-AUTH-001 | Login | Must | AD:View-Component-Auth; LLD:Auth | /v1/auth/login | users,sessions | TEST-AUTH-01.. | Draft
```

---

## 6) Quality Gate — Checklist tự kiểm

- [ ] Không còn từ mơ hồ (xem Mục 8).
- [ ] Mọi NFR có metric, mục tiêu, phép đo.
- [ ] Tất cả `REQ-*` có Test/Design/API/DB trong Traceability.
- [ ] RBAC theo endpoint đã phủ đủ & đánh dấu PII.
- [ ] Retention có cơ sở pháp lý & quy trình xóa.
- [ ] OpenAPI được cập nhật & hợp lệ (lint).
- [ ] Bảng/Heading/Code block hợp lệ Markdown; không lỗi chính tả nghiêm trọng.
- [ ] Cập nhật _Document_Index.md_ & _Related_ trong header.

---

## 7) Quy trình cập nhật (Change & Versioning)

1. Tạo `CHG-YYYY-NNN` trong _TEMPLATE-LC-002-Change_Impact_Assessment.md_.
2. Sửa các tài liệu liên quan (SRS/AD/LLD/API/Data/Test…).
3. Cập nhật Traceability & Release Notes.
4. Tăng **Version** trong header tài liệu & ký duyệt (_Status: Approved_).

---

## 8) Ngôn từ cần tránh (anti‑ambiguity)

- Tránh: _nhanh_, _tốt_, _cao cấp_, _mạnh mẽ_, _dễ dùng_, _ổn định_, _tối ưu_, _an toàn_…
- Thay bằng số liệu: thời gian (ms), thông lượng (rps), tỉ lệ lỗi (%), độ sẵn sàng (%), MTTR, MTTD, P95/P99, kích thước (MB), hạn xóa (ngày).

---

## 9) Prompt gợi ý (dành cho AI Agent)

- **Sinh SRS cho tính năng X**: “Tạo mục 4.1/4.2 cho X, sinh REQ-<AREA>-NNN với Acceptance Criteria dạng Gherkin; bổ sung Data Requirements 4.4 (PII/retention) và cập nhật Traceability row.”
- **Sinh ADR**: “Dựa trên concerns A/B/C, so sánh 2 phương án, chọn 1, ghi hậu quả & liên kết REQ/Issue.”
- **Cập nhật API**: “Điều chỉnh OpenAPI cho /v1/...; đảm bảo idempotency, lỗi chuẩn hóa; thêm example.”
- **Viết LLD**: “Vẽ trình tự (Mermaid/PlantUML) cho flow Y, liệt kê lỗi & log cần thiết; nêu chỉ tiêu hiệu năng.”
- **Soát Quality Gate**: “Chạy checklist Mục 6 trên tệp vừa chỉnh; liệt kê lỗi & đề xuất sửa.”

---

## 10) Mẫu commit & branching (gợi ý)

- **Commit**: `docs(srs): add REQ-AUTH-002 + traceability`
- **Chủ đề**: `docs/<artifact>/<area>` (vd: `docs/api/auth`).
- **PR title**: ngắn gọn, kèm ID liên quan (REQ/ADR/CHG).

---

## 11) Bảo trì chỉ mục

- Cập nhật `99-Indexes/Document_Index.md` sau mỗi tài liệu mới (Owner, Version, Link).
