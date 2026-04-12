# Mercury Prompt Engineering for Codex

Tài liệu này dành cho Business Analyst team và Product Owner team khi dùng Codex agent để làm việc với dự án có tổ chức tài liệu theo `ISO_Doc_Kit`.

Mục tiêu không phải là dạy kỹ thuật AI theo kiểu hàn lâm. Mục tiêu là giúp BA và PO biết cách viết prompt sao cho Codex hiểu đúng việc cần làm, đọc đúng tài liệu cần đọc, và trả ra kết quả dễ review hơn.

Nếu nói ngắn gọn, cách dùng tốt nhất là:

1. dùng `AGENTS.md` để giữ các nguyên tắc lặp đi lặp lại của team
2. dùng prompt từng task để nói rõ việc đang cần làm
3. dùng tài liệu trong `ISO_Doc_Kit` làm ngữ cảnh đầu vào
4. luôn nói rõ “xong khi nào”, thay vì chỉ nói “làm giúp tôi”

## 1. Những nguyên tắc chính từ tài liệu OpenAI

Theo hướng dẫn chính thức của OpenAI cho Codex, một prompt tốt cho Codex thường nên có 4 phần:

- `Goal`
  Bạn muốn thay đổi, tạo mới, phân tích, hay rà soát điều gì.
- `Context`
  File nào, thư mục nào, tài liệu nào, lỗi nào, ví dụ nào là quan trọng cho task này.
- `Constraints`
  Những điều Codex phải tuân theo, ví dụ format tài liệu, quy tắc naming, phạm vi không được vượt quá, hay tiêu chuẩn review.
- `Done when`
  Điều kiện để xem task là xong, ví dụ tài liệu nào đã được cập nhật, checklist nào đã được kiểm, phần nào đã được đối chiếu.

OpenAI cũng khuyến nghị prompt nên:

- ngắn gọn nhưng rõ ràng
- đi thẳng vào việc cần làm
- chia phần bằng tiêu đề hoặc delimiter để model dễ đọc
- bắt đầu bằng zero-shot, chỉ thêm ví dụ khi thật sự cần
- tránh yêu cầu kiểu “hãy suy nghĩ từng bước” hoặc “hãy giải thích toàn bộ chain-of-thought”

Với Codex, điểm quan trọng nhất không phải là viết prompt dài. Điểm quan trọng là đưa đúng ngữ cảnh và nói rõ tiêu chuẩn hoàn thành.

## 2. BA và PO nên hiểu `AGENTS.md` như thế nào

Theo tài liệu chính thức của OpenAI, `AGENTS.md` là nơi tốt nhất để ghi cách team muốn Codex làm việc trong một repository.

Hiểu đơn giản:

- `AGENTS.md` là nơi để ghi luật chơi dùng nhiều lần
- prompt của từng task là nơi để ghi việc cụ thể của lần này

Một `AGENTS.md` tốt thường nên có:

- cấu trúc repo và thư mục quan trọng
- cách chạy project
- lệnh build, test, lint
- quy ước làm việc và review
- các điều cấm hoặc ràng buộc
- định nghĩa “xong” là gì và kiểm tra ra sao

Ngoài các phần cơ bản ở trên, với cách làm của Mercury, mọi `AGENTS.md` nên có thêm các block chuẩn sau để Codex làm việc ổn định hơn:

- `## Output Verbosity Spec (output_verbosity_spec)`
  Để cố định độ dài câu trả lời, tránh trả lời quá dài hoặc quá ngắn.
- `## Workflow Order`
  Để nhắc đúng thứ tự làm việc, ví dụ tài liệu trước, rồi backend, rồi frontend.
- `## Design And Scope Constraints (design_and_scope_constraints)`
  Để khóa phạm vi, tránh Codex tự thêm tính năng hoặc tự trang trí quá mức.
- `## Long Context Handling (long_context_handling)`
  Để xử lý các task có nhiều tài liệu dài mà không bị trả lời lan man.
- `## Uncertainty And Ambiguity (uncertainty_and_ambiguity)`
  Để buộc Codex nêu giả định hoặc hỏi lại khi bài toán chưa rõ.
- `## High Risk Self Check (high_risk_self_check)`
  Để buộc Codex tự rà lại câu trả lời trong các tình huống nhạy cảm như compliance, legal, financial hoặc safety.

Hiểu ngắn gọn, đây là các block giúp Codex:

- trả lời gọn hơn
- ít vượt scope hơn
- xử lý tài liệu dài tốt hơn
- không tự bịa khi thiếu căn cứ
- cẩn thận hơn ở các phần rủi ro cao

OpenAI cũng khuyên giữ `AGENTS.md` ngắn, thực tế và dễ dùng. Nếu file bắt đầu quá dài, nên để file chính ngắn gọn rồi tham chiếu sang các markdown chuyên biệt như planning, code review, architecture.

Điều này rất hợp với `ISO_Doc_Kit`. Bộ kit này vốn đã tách tài liệu theo lớp. Vì vậy:

- nguyên tắc chung của repo nên ở `AGENTS.md`
- nội dung nghiệp vụ, yêu cầu, kiến trúc, LLD thì nên giữ trong các file của `ISO_Doc_Kit`
- prompt chỉ cần gọi đúng tài liệu liên quan của task

### Cách hiểu nhanh về `gstack` và skill theo tech stack

Trong cách làm của Mercury, hai lớp này không thay thế nhau.

- `gstack` giúp team đi đúng workflow, đúng stage, đúng thứ tự công việc
- skill theo tech stack giúp agent làm đúng chuyên môn sâu của stack đang đụng tới

Ví dụ:

- dùng `/plan-eng-review` để khóa plan
- vào giai đoạn Build thì có thể dùng thêm `php-expert` cho backend, skill frontend riêng của dự án cho UI, hoặc skill database riêng cho schema và tối ưu truy vấn

Nói ngắn gọn, `gstack` là khung điều phối, còn skill theo stack là lớp chuyên môn để thực thi. Khi viết prompt cho Codex, BA và PO nên chỉ rõ cả hai lớp này nếu task vừa có yêu cầu về workflow, vừa có yêu cầu kỹ thuật đặc thù.

## 3. Dùng `ISO_Doc_Kit` làm ngữ cảnh cho Codex

Khi BA hoặc PO làm việc với Codex, đừng gửi một yêu cầu chung chung như:

`hãy cập nhật tài liệu này`

Thay vào đó, nên chỉ rõ:

- đang làm việc ở tầng tài liệu nào
- file nào là nguồn chính
- file nào chỉ để tham khảo
- đầu ra mong muốn là cập nhật file, rà soát logic, hay so sánh chênh lệch

### Map nhanh giữa loại việc và thư mục nên đưa vào prompt

- Nếu đang làm rõ bài toán hoặc phạm vi:
  dùng `01-Requirements/BRD/`
- Nếu đang làm rõ yêu cầu hệ thống:
  dùng `01-Requirements/SRS/`
- Nếu đang kiểm tra yêu cầu đã đi xuyên suốt hay chưa:
  dùng RTM trong `01-Requirements/`
- Nếu đang chốt cách hệ thống vận hành hoặc các kết nối:
  dùng `02-Architecture/`
- Nếu đang đi vào logic chi tiết theo module:
  dùng `05-LLD/`
- Nếu đang chuẩn bị test, release, go-live:
  dùng `03-Lifecycle/`

### Nguyên tắc chọn ngữ cảnh

Không cần ném toàn bộ bộ tài liệu vào một prompt.

OpenAI lưu ý rằng context luôn có giới hạn. Codex có thể tự gom thêm context trong lúc làm việc, nhưng prompt ban đầu vẫn nên gọn và đúng trọng tâm. Vì vậy:

- chọn 1 đến 3 tài liệu nguồn chính
- thêm 1 đến 2 tài liệu tham chiếu nếu thật sự cần
- tránh nhồi cả BRD, SRS, AD, API, LLD của mọi module vào cùng một lượt

## 4. Mẫu prompt chuẩn cho BA và PO

Đây là mẫu prompt nên dùng thường xuyên.

```md
Goal
- Cập nhật hoặc tạo tài liệu nào
- Việc chính là phân tích, viết mới, rà soát hay đối chiếu

Context
- Đọc các file sau trước:
  - <file 1>
  - <file 2>
  - <file 3>
- Nếu cần đối chiếu, xem thêm:
  - <file tham chiếu>

Constraints
- Chỉ cập nhật file được chỉ định
- Giữ đúng cấu trúc của ISO Doc Kit
- Viết bằng tiếng Việt, ngôn ngữ tự nhiên, ưu tiên BA/PO dễ hiểu
- Không tự thêm scope mới ngoài tài liệu nguồn
- Nếu có điểm mâu thuẫn giữa các file, nêu rõ giả định

Done when
- File đích đã được cập nhật
- Các điểm thay đổi chính đã được liệt kê
- Các giả định hoặc chỗ còn thiếu đã được nêu rõ
```

Mẫu này bám rất sát guidance chính thức của OpenAI cho Codex: mục tiêu rõ, ngữ cảnh rõ, ràng buộc rõ, điều kiện hoàn thành rõ.

## 5. Prompt mẫu theo nhu cầu thực tế của BA và PO

### 5.1. Khi BA muốn draft hoặc cập nhật SRS từ BRD

```md
Đọc:
- docs/01-Requirements/BRD/BRD-...
- docs/04-Supporting/Glossary.md

Mục tiêu:
- cập nhật tài liệu SRS cho module Worker Skills

Ràng buộc:
- chỉ cập nhật file SRS được chỉ định
- bám đúng business scope trong BRD
- nếu BRD chưa đủ để viết một mục nào, ghi rõ khoảng trống thay vì tự suy diễn
- viết tiếng Việt, dễ đọc cho BA, QA và PO

Xong khi:
- SRS có đủ mục chức năng chính, rule, input/output, error case, acceptance criteria
- có danh sách điểm còn thiếu cần BA xác nhận
```

### 5.2. Khi PO muốn đánh giá impact của change request

```md
Đọc:
- docs/01-Requirements/SRS/SRS-...
- docs/02-Architecture/AD/...
- docs/03-Lifecycle/Deployment/...

Mục tiêu:
- phân tích change request này ảnh hưởng tới requirement, architecture và release ở đâu

Ràng buộc:
- không sửa code
- ưu tiên chỉ ra phạm vi ảnh hưởng theo tài liệu
- nhóm kết quả theo mức độ: requirement, dữ liệu, API, test, release

Xong khi:
- có bảng impact summary
- có danh sách file cần cập nhật tiếp
- có các rủi ro chính cho BA/PO review
```

### 5.3. Khi BA muốn Codex rà logic giữa nhiều lớp tài liệu

```md
Đọc:
- docs/01-Requirements/SRS/...
- docs/02-Architecture/Data_Model/...
- docs/05-LLD/Worker-Mobile/17-Skills/...

Mục tiêu:
- rà xem logic module Skills có nhất quán giữa SRS, Data Model và LLD hay không

Ràng buộc:
- không tự sửa file trước
- liệt kê mismatch theo mức độ nghiêm trọng
- nêu rõ file nào đang nói gì

Xong khi:
- có danh sách mismatch
- có đề xuất thứ tự sửa tài liệu
```

## 6. Khi nào nên đưa yêu cầu vào prompt, khi nào nên đưa vào `AGENTS.md`

### Nên đưa vào prompt từng task

- module đang xử lý lần này
- file nguồn phải đọc trong lần này
- đầu ra mong muốn trong lần này
- phạm vi không được vượt quá của lần này

### Nên đưa vào `AGENTS.md`

- project structure
- quy tắc đặt tên file
- style viết tài liệu của team
- workflow như “docs trước, backend sau, frontend sau”
- quy tắc review, test, lint, build
- “done means” dùng lặp đi lặp lại
- output verbosity spec
- long-context rules
- ambiguity handling
- high-risk self-check

### Các block Mercury khuyến nghị mọi `AGENTS.md` nên có

Khi tạo hoặc cập nhật `AGENTS.md`, nên đảm bảo có đủ các block này:

- `## Output Verbosity Spec (output_verbosity_spec)`
- `## Workflow Order`
- `## Design And Scope Constraints (design_and_scope_constraints)`
- `## Long Context Handling (long_context_handling)`
- `## Uncertainty And Ambiguity (uncertainty_and_ambiguity)`
- `## High Risk Self Check (high_risk_self_check)`

Đây là bộ tối thiểu rất đáng giữ cố định ở mọi repo hoặc mọi thư mục làm việc chính của Mercury.

Nếu một hướng dẫn dùng lặp lại từ task này sang task khác, đừng nhắc lại thủ công mãi trong prompt. Theo guidance của OpenAI, đó là lúc nên đưa nó vào `AGENTS.md`.

## 7. Cách yêu cầu Codex tự kiểm tra chất lượng đầu ra

Theo tài liệu chính thức của OpenAI, không nên dừng ở mức “hãy làm thay đổi này”. Nên yêu cầu Codex:

- tạo hoặc cập nhật test khi cần
- chạy đúng các check liên quan
- xác nhận kết quả cuối cùng
- review diff để tìm bug, regression, hoặc pattern rủi ro

Với tài liệu BA/PO, có thể chuyển ý này thành:

- tự rà tính nhất quán giữa các file
- tự liệt kê chỗ mâu thuẫn
- tự chỉ ra giả định đang dùng
- tự kiểm tra xem đầu ra đã đúng format mong muốn chưa

Ví dụ câu thêm vào prompt:

```md
Trước khi kết thúc, hãy tự kiểm tra lại:
- đầu ra đã bám đúng file nguồn chưa
- có điểm nào đang suy diễn mà không có căn cứ trong tài liệu không
- có mục nào cần BA hoặc PO xác nhận thêm không
```

## 8. Những lỗi BA và PO hay gặp khi dùng Codex

### Lỗi 1, prompt quá ngắn nhưng không có context

Ví dụ:

`cập nhật giúp tôi tài liệu worker mobile`

Vấn đề là Codex không biết:

- file nào là nguồn thật
- file nào là đích
- đang sửa logic, wording hay cấu trúc
- xong nghĩa là gì

### Lỗi 2, đưa quá nhiều context không cần thiết

Ví dụ đưa cả bộ thư mục lớn vào một task rất nhỏ.

Vấn đề là context dài không tự động tốt hơn. OpenAI khuyên nên chính xác, không nên nhồi thêm context không cần.

### Lỗi 3, không nói rõ phạm vi cấm

Nếu bạn chỉ muốn Codex cập nhật tài liệu, hãy nói thẳng:

- không sửa code
- không tạo thêm file ngoài file đích
- không mở rộng scope

### Lỗi 4, không nói rõ điều kiện hoàn thành

Nếu không có phần `Done when`, Codex dễ trả ra thứ “có vẻ hợp lý” nhưng chưa chắc là thứ bạn cần review.

### Lỗi 5, biến `AGENTS.md` thành tài liệu dài và mơ hồ

OpenAI khuyên `AGENTS.md` nên ngắn, chính xác, thực tế. Nếu file này quá dài và chứa nhiều khẩu hiệu hơn là hướng dẫn cụ thể, hiệu quả sẽ giảm.

## 9. Cách kết hợp `ISO_Doc_Kit` với Codex theo workflow Mercury

### Bước 1, cố định luật chơi trong `AGENTS.md`

Ví dụ:

- tài liệu phải ưu tiên tiếng Việt hay song ngữ
- thứ tự ưu tiên tài liệu trong repo
- phong cách viết cho BA/PO
- quy tắc không tự mở rộng scope
- output verbosity spec
- ambiguity handling
- self-check cho các task nhạy cảm

### Bước 2, dùng prompt cho task cụ thể

Ví dụ:

- cập nhật README
- rà chênh lệch giữa SRS và LLD
- tạo draft impact analysis cho change request

### Bước 3, gọi đúng tài liệu nguồn từ `ISO_Doc_Kit`

Ví dụ:

- BRD để hiểu bài toán
- SRS để hiểu yêu cầu
- AD hoặc Data Model để hiểu hướng triển khai
- LLD để hiểu logic chi tiết

### Bước 4, yêu cầu Codex tự rà lại đầu ra

Ví dụ:

- liệt kê thay đổi chính
- nêu giả định
- nêu chỗ còn thiếu
- đối chiếu lại với file nguồn

Đây là cách làm thực tế nhất. Gọn. Dễ review. Ít lệch scope.

## 10. Prompt mẫu chuẩn Mercury cho BA/PO

```md
Đọc các tài liệu sau trước:
- <absolute path hoặc repo path 1>
- <absolute path hoặc repo path 2>

Mục tiêu:
- <mô tả việc cần làm thật cụ thể>

Ngữ cảnh:
- đây là task thuộc tầng tài liệu nào trong ISO Doc Kit
- file nào là nguồn chính
- file nào là file đích

Ràng buộc:
- chỉ cập nhật <file đích>
- viết bằng tiếng Việt, ngôn ngữ tự nhiên, BA/PO dễ hiểu
- không tự thêm scope mới ngoài tài liệu nguồn
- nếu có điểm mâu thuẫn, nêu rõ và chọn cách hiểu đơn giản nhất

Xong khi:
- file đích đã được cập nhật
- đã tóm tắt các thay đổi chính
- đã chỉ ra chỗ còn thiếu hoặc cần xác nhận thêm
- đã tự rà lại tính nhất quán với file nguồn
```

## 11. Nguồn chính thức nên đọc thêm

- OpenAI Codex best practices, phần prompt structure và review loop:
  [https://developers.openai.com/codex/learn/best-practices/](https://developers.openai.com/codex/learn/best-practices/)
- OpenAI Codex prompting, phần context:
  [https://developers.openai.com/codex/prompting/](https://developers.openai.com/codex/prompting/)
- OpenAI Codex guide cho `AGENTS.md`:
  [https://developers.openai.com/codex/guides/agents-md/](https://developers.openai.com/codex/guides/agents-md/)
- OpenAI reasoning prompt best practices:
  [https://developers.openai.com/api/docs/guides/reasoning-best-practices/](https://developers.openai.com/api/docs/guides/reasoning-best-practices/)

## 12. Kết luận

Khi BA và PO dùng Codex, điều quan trọng không phải là “viết prompt cho hay”.

Điều quan trọng là:

- đưa đúng tài liệu nguồn
- nói rõ việc cần làm
- giữ ràng buộc rõ ràng
- nói rõ điều kiện hoàn thành
- để các luật chơi lặp đi lặp lại trong `AGENTS.md`

Làm được chừng đó, `ISO_Doc_Kit` sẽ không chỉ là nơi lưu tài liệu. Nó sẽ trở thành nguồn context chuẩn để Codex làm việc ổn định và dễ review hơn cho cả team.
