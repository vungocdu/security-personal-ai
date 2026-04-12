# Software Development Lifecycle

Tài liệu này mô tả vòng đời phát triển phần mềm theo workflow của gstack, nhưng được viết lại bằng tiếng Việt để team Business Analyst, Product Owner và các team delivery của Mercury có thể dùng trực tiếp trong `ISO_Doc_Kit`.

Điểm quan trọng là: đây không phải một danh sách công cụ rời rạc. Đây là một quy trình làm phần mềm có thứ tự, có đầu ra rõ ràng ở từng giai đoạn, có bước kiểm soát chất lượng, và có cơ chế học lại sau mỗi vòng làm việc.

Trong phiên bản này, lifecycle được tích hợp từ 3 lớp làm việc:

- `gstack`
  Là workflow điều phối các stage và skill theo thứ tự đúng.
- `ISO_Doc_Kit`
  Là nơi tổ chức tài liệu theo từng tầng: yêu cầu, kiến trúc, lifecycle, LLD.
- `Mercury Prompt Engineering Standard`
  Là chuẩn viết prompt và chuẩn hóa `AGENTS.md` để Codex hoặc agent khác làm việc ổn định, ít vượt scope, và dễ review hơn.

Workflow cốt lõi là:

**Think → Plan → Build → Review → Test → Ship → Reflect**

Đây là xương sống của toàn bộ quy trình.

## 1. Vì sao cần một lifecycle rõ ràng

Nếu chỉ dùng AI agent theo kiểu “có gì làm nấy”, rất nhanh sẽ xảy ra tình trạng:

- người đang nghĩ về ý tưởng, người khác đã bắt đầu sửa code
- chưa chốt scope nhưng đã đi vào implementation
- chưa review mà đã test
- chưa test kỹ mà đã chuẩn bị ship
- không ai ghi lại bài học sau khi xong việc

Kết quả là team chạy nhanh nhưng rất dễ loạn.

Workflow của gstack giải quyết chuyện đó bằng cách buộc mỗi giai đoạn phải để lại đầu ra cho giai đoạn tiếp theo:

- giai đoạn nghĩ ra bài toán sẽ tạo design doc
- giai đoạn plan sẽ khóa hướng làm
- giai đoạn build sẽ tạo implementation có căn cứ
- giai đoạn review sẽ chỉ ra risk và lỗi
- giai đoạn test sẽ xác minh hành vi thật
- giai đoạn ship sẽ đưa thay đổi lên an toàn
- giai đoạn reflect sẽ ghi lại bài học cho vòng sau

Hiểu ngắn gọn: không để bước sau phải đoán bước trước.

## 2. Toàn cảnh lifecycle

| Giai đoạn | Mục tiêu | Skill hoặc nhóm việc chính | Đầu ra chính |
|-----------|----------|----------------------------|--------------|
| Think | Làm rõ bài toán thật sự | `/office-hours` | Design doc |
| Plan | Khóa scope, kiến trúc, design, DX | `/plan-ceo-review`, `/plan-eng-review`, `/plan-design-review`, `/plan-devex-review`, `/autoplan` | Kế hoạch đã được review |
| Build | Biến kế hoạch thành code hoặc tài liệu | coding session, `/investigate`, các skill hỗ trợ | Diff implementation |
| Review | Tìm bug, regression, assumption yếu | `/review`, `/codex`, `/cso` | Findings và fix |
| Test | Xác minh hành vi thật | `/qa`, `/qa-only`, `/browse`, `/benchmark`, `/canary` | Kết quả test và evidence |
| Ship | Đưa thay đổi lên an toàn | `/ship`, `/land-and-deploy`, `/document-release` | PR, deploy, docs cập nhật |
| Reflect | Ghi lại bài học để vòng sau tốt hơn | `/retro`, `/learn` | Retro và learnings |

## 3. Lifecycle này gắn với `ISO_Doc_Kit` như thế nào

`gstack` trả lời câu hỏi: team nên làm theo thứ tự nào.

`ISO_Doc_Kit` trả lời câu hỏi: ở mỗi bước thì tài liệu nên nằm ở đâu.

`Mercury Prompt Engineering Standard` trả lời câu hỏi: khi dùng Codex hoặc agent, nên viết prompt và `AGENTS.md` thế nào để agent đọc đúng tài liệu, làm đúng việc, và dừng đúng chỗ.

Map ngắn gọn như sau:

| Giai đoạn | Thư mục trong `ISO_Doc_Kit` thường liên quan nhất |
|-----------|----------------------------------------------------|
| Think | `00-Process/`, `01-Requirements/BRD/`, `04-Supporting/Glossary.md` |
| Plan | `01-Requirements/SRS/`, `01-Requirements/RTM`, `02-Architecture/` |
| Build | `02-Architecture/`, `05-LLD/`, và các file `AGENTS.md` hoặc prompt rules đang điều khiển agent |
| Review | `02-Architecture/`, `05-LLD/`, cộng với các tài liệu nguồn cần đối chiếu |
| Test | `03-Lifecycle/Test/`, `03-Lifecycle/Deployment/`, `03-Lifecycle/Runbook/` |
| Ship | `03-Lifecycle/Deployment/`, `03-Lifecycle/ChangeMgmt/`, `README.md`, các doc entry-point |
| Reflect | `03-Lifecycle/Runbook/`, `99-Indexes/`, learnings hoặc retrospective notes |

Hiểu đơn giản:

- gstack là quy trình chạy việc
- ISO Doc Kit là bản đồ tài liệu của quy trình đó
- Mercury Prompt Engineering Standard là cách nói chuyện với agent để nó chạy quy trình này cho đúng

## 4. Mercury Prompt Engineering Standard nằm ở đâu trong lifecycle

Mercury Prompt Engineering Standard không phải một bước riêng. Nó là lớp điều khiển xuyên suốt toàn bộ lifecycle.

Nó yêu cầu 3 thứ phải luôn rõ:

- prompt của từng task phải có `Goal`, `Context`, `Constraints`, `Done when`
- `AGENTS.md` phải giữ các luật chơi lặp đi lặp lại của repo hoặc thư mục
- agent phải đọc đúng tài liệu trong `ISO_Doc_Kit` theo đúng tầng đang làm việc

Điều đó có nghĩa là:

- ở Think, prompt phải nói rõ đang làm rõ bài toán nào và đọc tài liệu nền nào
- ở Plan, prompt phải nói rõ đang khóa scope hay kiến trúc và file nguồn nào là gốc
- ở Build, prompt phải nói rõ file đích, phạm vi cấm, và điều kiện hoàn thành
- ở Review và Test, prompt phải nói rõ đang chỉ review hay được phép sửa
- ở Ship, prompt phải nói rõ cần cập nhật docs nào để tránh drift

### Các block `AGENTS.md` nên có để lifecycle chạy ổn định

Theo Mercury Prompt Engineering Standard, mọi `AGENTS.md` nên có ít nhất:

- `Output Verbosity Spec`
- `Workflow Order`
- `Design And Scope Constraints`
- `Long Context Handling`
- `Uncertainty And Ambiguity`
- `High Risk Self Check`

Các block này giúp agent:

- trả lời gọn và đều hơn
- ưu tiên docs trước backend rồi mới frontend khi task chạm nhiều lớp
- không tự mở rộng scope
- xử lý tài liệu dài tốt hơn
- nêu giả định khi chưa đủ căn cứ
- tự rà lại ở các bài toán nhạy cảm

### Prompt chuẩn Mercury nên được dùng thế nào

Trong lifecycle này, prompt tốt không phải prompt dài nhất. Prompt tốt là prompt:

- chỉ đúng file nguồn cần đọc
- chỉ rõ file đích hoặc output mong muốn
- nói rõ điều không được làm
- nói rõ “xong khi nào”

Nếu một quy tắc được lặp lại nhiều lần, đừng nhắc lại trong từng prompt. Chuyển nó vào `AGENTS.md`.

## 5. Giai đoạn Think

Đây là bước bắt đầu khi:

- ý tưởng còn mơ hồ
- feature request nghe có vẻ hợp lý nhưng chưa chắc là đúng bài toán
- team chưa thật sự biết user đang đau ở đâu

Skill chính:

- `/office-hours`

Mục tiêu của bước này:

- ép team quay lại câu hỏi gốc: người dùng thực sự cần gì
- tìm đúng “job to be done”
- xác định phạm vi hẹp nhất có thể ship để học nhanh
- tạo ra 2 đến 3 hướng tiếp cận với effort tương đối rõ

Đầu ra mong muốn:

- có design doc
- mô tả được user là ai
- mô tả được pain point là gì
- biết điều gì chưa nên làm ở vòng đầu

Vì sao bước này quan trọng:

Nếu bài toán sai, toàn bộ phần còn lại càng làm càng đắt.

### Think dùng tài liệu gì trong `ISO_Doc_Kit`

Ở bước này, team thường nên kéo các nguồn sau vào prompt hoặc vào phần context:

- `01-Requirements/BRD/`
- `04-Supporting/Glossary.md`
- các tài liệu mô tả bối cảnh trong `00-Process/`

Output tài liệu phù hợp ở bước này thường là:

- draft BRD
- problem statement
- scope business ban đầu

## 6. Giai đoạn Plan

Khi bài toán đã đáng để làm, bước tiếp theo là khóa kế hoạch trước khi build.

Skill chính:

- `/plan-ceo-review`
- `/plan-eng-review`
- `/plan-design-review`
- `/plan-devex-review`
- `/autoplan`

Mục tiêu của bước này:

- chốt scope, không để implementation tự mở rộng lung tung
- chốt kiến trúc, data flow, edge cases, test strategy
- chốt chất lượng trải nghiệm người dùng trước khi code
- với sản phẩm cho developer, chốt luôn trải nghiệm developer

Đầu ra mong muốn:

- có plan đã được review
- các quyết định kiến trúc quan trọng đã lộ ra
- các rủi ro lớn đã được nêu trước khi build
- team biết rõ “xong là như thế nào”

Vì sao bước này quan trọng:

Nhiều lỗi đắt nhất không phải lỗi code. Chúng là lỗi plan:

- sai boundary
- thiếu edge case
- quên test strategy
- quyết định kiến trúc không rõ

### Plan dùng tài liệu gì trong `ISO_Doc_Kit`

Đây là lúc tài liệu bắt đầu chuyển từ ngôn ngữ business sang ngôn ngữ hệ thống.

Những thư mục thường liên quan nhất là:

- `01-Requirements/SRS/`
- RTM trong `01-Requirements/`
- `02-Architecture/AD/`
- `02-Architecture/ADR/`
- `02-Architecture/API/`
- `02-Architecture/Data_Model/`
- `02-Architecture/Security_Privacy/`

Output tài liệu phù hợp ở bước này thường là:

- SRS rõ hơn
- architecture decision rõ hơn
- data model hoặc API contract đã đủ để build

## 7. Giai đoạn Build

Chỉ build khi plan đã đủ rõ.

Việc chính:

- coding session bình thường với Claude Code hoặc Codex
- `/investigate` nếu bài toán thực chất là debug
- các skill thiết kế nếu task có phần UI hoặc HTML
- các skill chuyên theo tech stack nếu hệ thống có stack đặc thù

Mục tiêu của bước này:

- biến plan thành implementation
- giữ scope đúng với cái đã duyệt
- tạo code, config, test, docs theo đúng yêu cầu

Đầu ra mong muốn:

- có implementation diff
- có test mới hoặc test cập nhật nếu cần
- có docs thay đổi theo behavior mới nếu behavior đã đổi

Dấu hiệu build tốt:

- code bám đúng plan
- không tự thêm feature
- không dùng build để tự plan lại từ đầu

### Build có thể dùng thêm skill theo tech stack

Trong giai đoạn Build, team không bị giới hạn vào các skill chung của gstack.

Nếu hệ thống dùng tech stack rõ ràng và lặp đi lặp lại, team hoàn toàn có thể tạo thêm các skill chuyên biệt để coding nhanh hơn, đúng chuẩn hơn, và ít phải nhắc lại cùng một rule nhiều lần.

Ví dụ:

- `php-expert`
  dùng cho backend PHP hoặc Laravel
- `actiwell-frontend-expert`
  dùng cho frontend có guideline, component pattern và workflow riêng
- `database-expert`
  dùng cho database design, query optimization, migration review và tối ưu cấu trúc dữ liệu

Hiểu đơn giản:

- gstack skill giữ vai trò điều phối theo stage
- skill theo tech stack giữ vai trò specialist để thực thi đúng ở layer kỹ thuật cụ thể

Điều này đặc biệt hữu ích khi team phải làm trên nhiều lớp khác nhau trong cùng một sprint:

- backend cần rule riêng của PHP
- frontend cần rule riêng của framework hoặc design system
- database cần rule riêng cho schema, index, migration và performance

### Khi nào nên tạo skill riêng thay vì chỉ viết prompt dài

Nếu team gặp một pattern lặp đi lặp lại như:

- cùng một stack luôn cần cùng một coding convention
- cùng một loại review luôn cần cùng một checklist
- cùng một loại project luôn phải nhắc lại cùng một build, test, deploy rule

thì nên đóng gói pattern đó thành skill riêng.

Lợi ích là:

- giảm độ dài prompt của từng task
- giảm việc agent phải đoán lại cách làm mỗi lần
- giúp người mới vào team dùng workflow đúng nhanh hơn
- biến kinh nghiệm nội bộ thành công cụ dùng lại được

### Cách kết hợp skill riêng với gstack trong giai đoạn Build

Cách dùng hợp lý thường là:

- dùng gstack để đi đúng stage, đúng workflow
- dùng skill chuyên biệt theo stack để thực thi trong stage Build
- giữ các rule lặp lại trong `AGENTS.md`
- chỉ để prompt của task mang phần việc cụ thể của lần này

Ví dụ một flow build có thể là:

1. plan đã được khóa bằng `/plan-eng-review`
2. backend implementation dùng `php-expert`
3. frontend implementation dùng skill frontend riêng của dự án
4. database change dùng `database-expert`
5. sau đó quay lại các bước `/review`, `/qa`, `/ship` theo workflow chung của gstack

Nói ngắn gọn:

- gstack cho team cái khung
- skill theo stack cho team đúng chuyên môn sâu
- `ISO_Doc_Kit` cho team biết tài liệu nào phải cập nhật cùng với thay đổi đó

### Build dùng tài liệu gì trong `ISO_Doc_Kit`

Build không chỉ bám code. Build tốt còn phải bám tài liệu chi tiết.

Nguồn chính ở bước này thường là:

- `02-Architecture/`
- `05-LLD/`
- các file guideline hoặc prompt rules được tham chiếu từ `AGENTS.md`

Nếu task chạm nhiều lớp, Mercury Prompt Engineering Standard nhắc rất rõ:

- cập nhật tài liệu trước
- rồi mới backend
- rồi mới frontend

## 8. Giai đoạn Review

Đây là bước chặn trước khi tin rằng thay đổi đã ổn.

Skill chính:

- `/review`
- `/codex`
- `/cso`

Mục tiêu của bước này:

- tìm bug mà CI có thể không bắt được
- tìm regression
- tìm assumption yếu
- tìm risk về security, migration, contract hoặc test coverage

Đầu ra mong muốn:

- danh sách findings có mức độ ưu tiên
- các lỗi obvious được fix sớm
- các concern còn lại được nói rõ, không mơ hồ

Vì sao bước này quan trọng:

Review không phải nghi thức. Đây là nơi bắt được lỗi có thể nổ sau deploy vài tiếng.

### Review nên đối chiếu với tài liệu nào

Review trong Mercury không chỉ review code. Review tốt thường phải đối chiếu ngược lại:

- code với `SRS`
- code với `Architecture`
- code với `LLD`
- release impact với `03-Lifecycle/`

Nói cách khác, review là chỗ kiểm tra chuỗi trace còn khớp hay không.

## 9. Giai đoạn Test

Đây là lúc xác nhận sản phẩm thực sự hoạt động từ góc nhìn người dùng.

Skill chính:

- `/qa`
- `/qa-only`
- `/browse`
- `/benchmark`
- `/canary`

Mục tiêu của bước này:

- mở browser thật
- đi qua flow thật
- chụp evidence thật
- tìm bug thật
- fix rồi test lại nếu cần

Đầu ra mong muốn:

- QA findings
- screenshot hoặc evidence
- regression fix nếu có bug
- performance baseline hoặc canary result nếu task cần

Dấu hiệu test tốt:

- test đúng luồng người dùng
- không chỉ dừng ở unit test
- kết luận dựa trên hành vi thật, không chỉ dựa trên ý định implementation

### Test dùng tài liệu gì trong `ISO_Doc_Kit`

Những thư mục thường liên quan nhất:

- `03-Lifecycle/Test/`
- `03-Lifecycle/Deployment/`
- `03-Lifecycle/Runbook/`
- acceptance criteria trong `SRS`

Test tốt là lúc các file này bắt đầu nối được với nhau, không còn đứng riêng lẻ.

## 10. Giai đoạn Ship

Ở bước Ship, điểm khác biệt quan trọng của Mercury là không coi tài liệu như việc làm sau cùng nếu còn thời gian.

Tài liệu là một phần của release.

Skill chính:

- `/ship`
- `/land-and-deploy`
- `/document-release`

Mục tiêu của bước này:

- chuẩn bị branch để mở PR hoặc merge
- chạy các check cuối
- verify deploy
- cập nhật tài liệu bị drift

Đầu ra mong muốn:

- PR rõ ràng
- deploy được xác minh
- docs khớp với cái thực sự ship

Vì vậy ở bước này nên kiểm tra:

- docs entry-point như `README.md` đã khớp chưa
- tài liệu deployment hoặc change management đã cập nhật chưa
- tài liệu nào trong `ISO_Doc_Kit` đang drift so với thay đổi vừa ship

Nếu dùng Codex ở bước này, prompt nên nói rõ:

- chỉ cập nhật file nào
- release note cần nói ở mức nào
- có cần update `README`, `Directory_Overview`, `SRS`, `LLD` hay không

Vì sao bước này quan trọng:

Nhiều team coi ship là “push lên rồi cầu may”. Workflow này coi ship là một bước release có kiểm soát.

## 11. Giai đoạn Reflect

Reflect không chỉ để ghi “đã làm gì”. Nó còn là bước tối ưu hóa workflow.

Skill chính:

- `/retro`
- `/learn`

Mục tiêu của bước này:

- ghi lại điều gì đã làm tốt
- ghi lại điều gì làm chưa tốt
- lưu pattern, pitfall, preference cho project
- tránh lặp lại cùng một lỗi ở vòng sau

Đầu ra mong muốn:

- retrospective
- learnings lưu lại để các session sau dùng tiếp

Ở Mercury, bước này nên tạo ra 2 loại output:

- learnings về cách làm việc
- learnings về cấu trúc tài liệu hoặc prompt mà team nên giữ lại

Ví dụ các learning tốt:

- nên đặt rule này vào `AGENTS.md`
- tài liệu loại này nên luôn viết bằng tiếng Việt tự nhiên cho BA/PO
- module kiểu này nên tách LLD riêng thay vì gộp chung

Vì sao bước này quan trọng:

Nếu không có bước này, team sẽ phải trả lại cùng một học phí nhiều lần.

## 12. Handoff giữa các giai đoạn

Mỗi giai đoạn nên để lại một thứ cụ thể cho bước tiếp theo.

| Từ bước | Sang bước | Handoff nên có |
|---------|-----------|----------------|
| Think | Plan | Design doc |
| Plan | Build | Plan đã được duyệt, có scope và test expectation |
| Build | Review | Diff implementation có chủ đích rõ |
| Review | Test | Diff sạch hơn, có risk area rõ hơn |
| Test | Ship | Hành vi đã được xác minh |
| Ship | Reflect | Kết quả đã ship thật |
| Reflect | Think | Learnings tốt hơn cho vòng sau |

Nếu không có handoff rõ, bước sau sẽ phải tự đoán. Và đoán là lúc chất lượng bắt đầu rơi.

## 13. Quality gate của từng bước

Workflow này chỉ mạnh nếu mỗi bước có một quality gate rõ ràng.

### Think gate

- đã xác định được user và pain point thật

### Plan gate

- scope, kiến trúc, edge cases và test strategy đã rõ

### Build gate

- implementation bám đúng plan

### Review gate

- các risk chính đã được chỉ ra

### Test gate

- hành vi thật đã được kiểm tra

### Ship gate

- code, docs và release state khớp nhau

### Reflect gate

- bài học đã được lưu lại

Nếu bỏ quality gate, workflow sẽ quay lại kiểu làm việc ứng biến với một agent rất nhanh, nhưng không thật sự đáng tin.

## 14. Team BA và PO nên dùng lifecycle này như thế nào

BA và PO không nhất thiết phải chạy mọi skill bằng tay. Nhưng BA và PO nên hiểu lifecycle này để:

- biết dự án đang đứng ở giai đoạn nào
- biết đầu ra nào đáng lẽ phải có ở giai đoạn hiện tại
- biết thiếu gì trước khi cho qua bước tiếp theo
- biết khi nào nên yêu cầu review, test hay update docs

Map nhanh:

- Khi ý tưởng còn mơ hồ, quay về Think
- Khi scope hoặc architecture còn rung lắc, quay về Plan
- Khi code đã có nhưng chưa được kiểm tra kỹ, đi qua Review rồi Test
- Khi chuẩn bị release, bắt buộc đi qua Ship
- Khi vừa xong một vòng lớn, nên có Reflect

### BA và PO nên nhớ thêm điều gì về Prompt Engineering

Khi dùng Codex hoặc agent tương tự trong lifecycle này, BA và PO nên luôn kiểm tra prompt đã có đủ 4 phần chưa:

- Goal
- Context
- Constraints
- Done when

Nếu thiếu một trong bốn phần này, khả năng agent đi lệch sẽ tăng lên rất nhiều.

## 15. Ví dụ một sprint hoàn chỉnh

Ví dụ team muốn làm một tính năng mới.

Chuỗi hợp lý sẽ là:

1. `/office-hours`
   Làm rõ đây có phải bài toán đáng làm không.
2. `/plan-ceo-review`
   Xem có nên mở scope, giữ scope, hay thu scope.
3. `/plan-eng-review`
   Khóa architecture, edge cases, test strategy.
4. Build
   Implement đúng theo plan.
5. `/review`
   Tìm bug và risk.
6. `/qa`
   Test flow thật trên browser.
7. `/ship`
   Chuẩn bị PR, verify release, cập nhật docs.
8. `/retro`
   Ghi lại bài học.

Đó là một sprint gọn, rõ, và có handoff tốt.

## 16. Kết luận

Software Development Lifecycle theo gstack không cố làm một agent “thông minh hơn theo cảm giác”.

Nó cố làm việc phát triển phần mềm rõ ràng hơn:

- đúng câu hỏi ở đúng thời điểm
- đúng specialist ở đúng giai đoạn
- đúng đầu ra cho bước kế tiếp

Khi tích hợp với `ISO_Doc_Kit`, workflow này có thêm một lợi ích lớn:

- mỗi bước không chỉ có việc để làm
- mỗi bước còn biết tài liệu nên nằm ở đâu

Khi tích hợp thêm Mercury Prompt Engineering Standard, workflow này lại có thêm một lớp ổn định nữa:

- agent biết phải đọc gì
- biết bị cấm làm gì
- biết trả lời ngắn hay dài ở mức nào
- biết phải dừng ở đâu khi thông tin chưa đủ

Đó là lý do workflow này có thể scale khi chạy nhiều agent song song mà không biến thành hỗn loạn.
