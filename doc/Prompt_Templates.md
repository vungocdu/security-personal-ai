# Prompt Templates for BA and PO

File này là bộ prompt mẫu copy-paste nhanh cho Business Analyst team và Product Owner team khi làm việc với Codex agent.

Nếu [`Mercury-Prompt-Engineering.md`](/Users/steve/development/devops/ISO_Doc_Kit/Mercury-Prompt-Engineering.md) là tài liệu giải thích cách làm, thì file này chỉ tập trung vào mẫu prompt thực dụng để dùng hằng ngày.

## 1. Mẫu `AGENTS.md` tối thiểu cho Mercury

Mẫu dưới đây dùng khi cần tạo mới hoặc chuẩn hóa `AGENTS.md`. Với Mercury, mọi `AGENTS.md` nên có các block ở dưới.

```md
## Output Verbosity Spec (output_verbosity_spec)

- Default: 3–6 sentences or ≤5 bullets for typical answers.
- For simple “yes/no + short explanation” questions: ≤2 sentences.
- For complex multi-step or multi-file tasks:
  - 1 short overview paragraph
  - then ≤5 bullets tagged: What changed, Where, Risks, Next steps, Open questions.
- Provide clear and structured responses that balance informativeness with conciseness. Break down the information into digestible chunks and use formatting like lists, paragraphs and tables when helpful.
- Avoid long narrative paragraphs; prefer compact bullets and short sections.
- Do not rephrase the user’s request unless it changes semantics.
- When a compact response is requested, use `POST https://api.openai.com/v1/responses/compact`.

## Workflow Order

- For feature changes that touch docs, backend, and frontend: update documentation first, then backend, then frontend.

## Design And Scope Constraints (design_and_scope_constraints)

- Explore any existing design systems and understand it deeply.
- Implement EXACTLY and ONLY what the user requests.
- No extra features, no added components, no UX embellishments.
- Style aligned to the design system at hand.
- Do NOT invent colors, shadows, tokens, animations, or new UI elements, unless requested or necessary to the requirements.
- If any instruction is ambiguous, choose the simplest valid interpretation.

## Long Context Handling (long_context_handling)

- For inputs longer than ~10k tokens (multi-chapter docs, long threads, multiple PDFs):
  - First, produce a short internal outline of the key sections relevant to the user’s request.
  - Re-state the user’s constraints explicitly (e.g., jurisdiction, date range, product, team) before answering.
  - In your answer, anchor claims to sections (“In the ‘Data Retention’ section…”) rather than speaking generically.
- If the answer depends on fine details (dates, thresholds, clauses), quote or paraphrase them.

## Uncertainty And Ambiguity (uncertainty_and_ambiguity)

- If the question is ambiguous or underspecified, explicitly call this out and:
  - Ask up to 1–3 precise clarifying questions, OR
  - Present 2–3 plausible interpretations with clearly labeled assumptions.
- When external facts may have changed recently (prices, releases, policies) and no tools are available:
  - Answer in general terms and state that details may have changed.
- Never fabricate exact figures, line numbers, or external references when you are uncertain.
- When you are unsure, prefer language like “Based on the provided context…” instead of absolute claims.

## High Risk Self Check (high_risk_self_check)

- Before finalizing an answer in legal, financial, compliance, or safety-sensitive contexts:
  - Briefly re-scan your own answer for:
    - Unstated assumptions,
    - Specific numbers or claims not grounded in context,
    - Overly strong language (“always,” “guaranteed,” etc.).
  - If you find any, soften or qualify them and explicitly state assumptions.
```

## 2. Mẫu chung, dùng cho hầu hết task

```md
Đọc các tài liệu sau trước:
- <file 1>
- <file 2>
- <file 3>

Mục tiêu:
- <mô tả thật rõ việc cần làm>

Ngữ cảnh:
- đây là task thuộc tầng tài liệu nào trong ISO Doc Kit
- file nào là nguồn chính
- file nào là file đích

Ràng buộc:
- chỉ cập nhật <file đích>
- viết bằng tiếng Việt, ngôn ngữ tự nhiên, BA/PO dễ hiểu
- không tự thêm scope mới ngoài tài liệu nguồn
- nếu có điểm mâu thuẫn giữa các file, nêu rõ giả định

Xong khi:
- file đích đã được cập nhật
- các thay đổi chính đã được tóm tắt
- các điểm còn thiếu hoặc cần xác nhận thêm đã được nêu rõ
- đã tự rà lại tính nhất quán với file nguồn
```

## 3. Mẫu cập nhật README hoặc overview tài liệu

```md
Đọc các file sau trước:
- <README hiện tại>
- <Directory_Overview hoặc tài liệu liên quan>
- <sample docs nếu có>

Mục tiêu:
- cập nhật tài liệu để BA và PO dễ hiểu hơn

Ràng buộc:
- chỉ cập nhật file được chỉ định
- giữ nguyên cấu trúc chính nếu chưa cần đổi
- ưu tiên tiếng Việt tự nhiên, ít thuật ngữ kỹ thuật
- giải thích theo hướng “file này giúp làm gì”
- không thêm nội dung ngoài phạm vi tài liệu nguồn

Xong khi:
- file đã được cập nhật
- giọng văn dễ đọc hơn cho BA/PO
- các điểm thay đổi chính đã được tóm tắt
```

## 4. Mẫu draft SRS từ BRD

```md
Đọc các file sau trước:
- <BRD nguồn>
- <Glossary nếu có>
- <SRS hiện tại hoặc template SRS>

Mục tiêu:
- tạo hoặc cập nhật SRS cho module <tên module>

Ràng buộc:
- bám đúng scope trong BRD
- nếu BRD chưa đủ thông tin, ghi rõ khoảng trống thay vì tự suy diễn
- viết tiếng Việt, rõ cho BA, QA và PO
- không chèn chi tiết kỹ thuật quá mức của API hoặc DB nếu chưa có nguồn

Xong khi:
- SRS có đủ phần chức năng chính, rule, input/output, lỗi và acceptance criteria
- có danh sách điểm còn thiếu cần BA xác nhận
```

## 5. Mẫu rà chênh lệch giữa BRD, SRS và LLD

```md
Đọc các file sau trước:
- <BRD>
- <SRS>
- <LLD hoặc Module Design>

Mục tiêu:
- rà xem các tài liệu này có chênh nhau ở đâu

Ràng buộc:
- không sửa file trước
- liệt kê mismatch theo mức độ nghiêm trọng
- với mỗi mismatch, nêu rõ file nào đang nói gì
- không tự kết luận nếu tài liệu chưa đủ căn cứ

Xong khi:
- có danh sách mismatch rõ ràng
- có đề xuất thứ tự sửa tài liệu
- có ghi rõ điểm nào cần BA hoặc PO xác nhận
```

## 6. Mẫu impact analysis cho change request

```md
Đọc các file sau trước:
- <SRS hiện tại>
- <Architecture hoặc AD>
- <Deployment hoặc Test plan nếu có>

Mục tiêu:
- phân tích change request này ảnh hưởng tới requirement, dữ liệu, test và release ở đâu

Ràng buộc:
- không sửa code
- ưu tiên phân tích theo tài liệu hiện có
- nhóm kết quả theo các phần: requirement, data, API, test, release
- nếu chưa đủ dữ liệu để kết luận, nêu rõ phần thiếu

Xong khi:
- có bảng impact summary
- có danh sách file cần cập nhật tiếp
- có các rủi ro chính để BA/PO review
```

## 7. Mẫu rà logic data model với requirement

```md
Đọc các file sau trước:
- <SRS>
- <Data_Model>
- <LLD nếu có>

Mục tiêu:
- kiểm tra logic dữ liệu có bám đúng yêu cầu hay không

Ràng buộc:
- tập trung vào entity, field bắt buộc, quan hệ và các rủi ro duplicate hoặc inconsistency
- không sửa file trước
- nêu rõ điểm nào chỉ là nghi ngờ, điểm nào là mismatch rõ ràng

Xong khi:
- có danh sách các điểm chưa khớp
- có đề xuất phần nào nên sửa ở SRS, Data Model hoặc LLD
```

## 8. Mẫu tạo tài liệu mô tả cấu trúc thư mục

```md
Đọc các file sau trước:
- <README của bộ docs>
- <Directory_Overview hiện tại nếu có>
- <sample docs structure>

Mục tiêu:
- tạo tài liệu giải thích cấu trúc thư mục cho BA và PO

Ràng buộc:
- viết bằng tiếng Việt, ngôn ngữ tự nhiên
- ưu tiên giải thích thư mục này dùng để làm gì, khi nào nên mở
- giảm thuật ngữ kỹ thuật nếu không thật sự cần
- giữ cách gọi nhất quán với README hiện tại

Xong khi:
- tài liệu mới hoặc bản cập nhật đã hoàn chỉnh
- các thư mục chính đã được giải thích rõ
- BA hoặc PO mới vào có thể dùng làm bản đồ đọc nhanh
```

## 9. Mẫu chuẩn hóa giọng văn tài liệu

```md
Đọc file sau:
- <file đích>

Nếu cần đối chiếu, đọc thêm:
- <README hoặc tài liệu chuẩn giọng văn>

Mục tiêu:
- chỉnh lại giọng văn để BA và PO đọc dễ hơn

Ràng buộc:
- giữ nguyên ý chính
- không thêm scope mới
- ưu tiên tiếng Việt tự nhiên, câu ngắn, dễ hiểu
- giảm các cụm quá kỹ thuật hoặc quá “nội bộ team”

Xong khi:
- file đã được viết mượt hơn
- giọng văn đồng bộ với tài liệu chuẩn
- các thuật ngữ khó đã được giảm bớt hoặc giải thích lại
```

## 10. Mẫu chỉ review, chưa sửa

```md
Đọc các file sau trước:
- <file 1>
- <file 2>
- <file 3>

Mục tiêu:
- chỉ review và nêu vấn đề, chưa sửa file

Ràng buộc:
- tập trung vào logic, mismatch, risk và điểm thiếu
- không tự sửa file
- ưu tiên xếp findings theo mức độ nghiêm trọng
- với mỗi finding, nêu rõ file nào, phần nào, và vì sao có rủi ro

Xong khi:
- có danh sách findings rõ ràng
- có câu hỏi mở hoặc giả định cần xác nhận thêm
```

## 11. Mẫu yêu cầu Codex tự kiểm tra đầu ra trước khi kết thúc

Đoạn này có thể thêm vào cuối gần như mọi prompt:

```md
Trước khi kết thúc, hãy tự kiểm tra lại:
- đầu ra đã bám đúng file nguồn chưa
- có chỗ nào đang suy diễn mà không có căn cứ trong tài liệu không
- có chỗ nào mâu thuẫn giữa các file chưa được nêu ra không
- có mục nào cần BA hoặc PO xác nhận thêm không

Khi trả kết quả, hãy gồm:
- tóm tắt ngắn những gì đã làm
- các điểm thay đổi chính
- các điểm còn thiếu hoặc cần xác nhận
```

## 12. Mẫu ngắn, dùng khi cần hỏi nhanh

### 11.1. Hỏi Codex nên đọc file nào trước

```md
Tôi đang xử lý <mô tả task>. Dựa trên cấu trúc ISO Doc Kit, hãy chỉ ra tôi nên đọc file hoặc thư mục nào trước, theo thứ tự, và giải thích ngắn vì sao.
```

### 11.2. Hỏi Codex file này nên đặt ở đâu

```md
Tôi cần tạo một tài liệu về <mô tả nội dung>. Dựa trên ISO Doc Kit, hãy cho biết tài liệu này nên đặt ở thư mục nào và vì sao.
```

### 11.3. Hỏi Codex còn thiếu tài liệu gì

```md
Đọc các tài liệu sau:
- <file 1>
- <file 2>
- <file 3>

Hãy cho biết bộ tài liệu này còn thiếu những gì nếu mục tiêu là chuẩn bị cho BA, QA và release review.
```

## 13. Cách dùng nhanh mỗi ngày

Nếu chỉ cần nhớ một công thức, hãy dùng:

1. nói Codex phải đọc file nào
2. nói rõ việc cần làm
3. nói rõ điều không được làm
4. nói rõ “xong khi nào”
