# Directory Overview

File này là bản đồ tra cứu nhanh cho `ISO_Doc_Kit`.

Nếu `README.md` là file giúp bạn hiểu bức tranh chung, thì `Directory_Overview.md` là file để mở ra khi bạn muốn biết:

- thư mục này dùng để làm gì
- BA nên viết gì ở đây
- nên đọc thư mục nào trước
- thư mục nào là phần chính, thư mục nào là phần hỗ trợ

Tài liệu này đi cùng một logic với README và cũng bám theo cách tổ chức đang thấy trong bộ tài liệu QuickShift.

## 1. Nhìn nhanh toàn bộ cấu trúc

```text
ISO_Doc_Kit/
├── 00-Process/
├── 01-Requirements/
├── 02-Architecture/
├── 03-Lifecycle/
├── 04-Supporting/
├── 05-LLD/
├── 99-Indexes/
├── README.md
└── Directory_Overview.md
```

Ý nghĩa của từng tầng:

- `00-Process`
  Nơi giải thích cách team làm việc với tài liệu và vòng đời dự án.
- `01-Requirements`
  Nơi làm rõ bài toán, yêu cầu và cách theo dõi yêu cầu.
- `02-Architecture`
  Nơi mô tả cách hệ thống được tổ chức, các kết nối, dữ liệu và quyền.
- `03-Lifecycle`
  Nơi đi cùng giai đoạn kiểm thử, triển khai, thay đổi và vận hành.
- `04-Supporting`
  Tài liệu hỗ trợ dùng chung.
- `05-LLD`
  Tài liệu chi tiết theo module hoặc theo app.
- `99-Indexes`
  Điều hướng và tra cứu.

## 2. Nên đọc theo thứ tự nào

Một BA mới vào dự án nên đi theo thứ tự này:

1. `README.md`
2. `00-Process/`
3. `01-Requirements/`
4. `02-Architecture/`
5. `03-Lifecycle/`
6. `05-LLD/`

Nếu BA đang xử lý change request, thường nên đi theo thứ tự này:

1. requirement hiện có trong `01-Requirements/`
2. solution hiện có trong `02-Architecture/`
3. impact tới release/test/runbook trong `03-Lifecycle/`
4. chi tiết module bị ảnh hưởng trong `05-LLD/`

## 3. Chi tiết từng thư mục

## `00-Process/`

Đây là thư mục để hiểu cách team Mercury làm việc với tài liệu và dự án.

Nó không mô tả một chức năng cụ thể. Nó giúp mọi người hiểu bối cảnh chung và các bước đi của dự án.

### Mục đích

- định nghĩa software lifecycle
- định nghĩa các điểm kiểm soát về chất lượng và bảo mật
- mô tả cách dự án đi từ yêu cầu tới lúc triển khai thực tế

### Khi BA cần đọc

- lúc onboard vào project
- lúc cần hiểu vì sao tài liệu phải được tách thành nhiều tầng
- lúc giải thích cho stakeholder về cách dự án đi từ yêu cầu tới release

### Các nhóm con

### `00-Process/AI_Development/`

Nơi mô tả cách dùng AI để hỗ trợ tạo tài liệu, phân tích và phát triển.

BA nên dùng khi:

- muốn dùng AI để draft BRD/SRS
- muốn review tài liệu bằng AI nhưng vẫn giữ kiểm soát chất lượng

### `00-Process/ISO_12207/`

Tập trung vào software development lifecycle.

Có thể hiểu đơn giản đây là nơi trả lời câu hỏi:
"Tài liệu nào phải có trước khi qua bước tiếp theo?"

### `00-Process/ISO_15288/`

Tập trung vào system lifecycle rộng hơn.

Hữu ích khi hệ thống không chỉ có một ứng dụng đơn lẻ, mà có nhiều phần cần kết nối với nhau.

### `00-Process/ISO_27001/`

Tập trung vào bảo mật thông tin.

BA nên xem khi requirement có:

- dữ liệu cá nhân
- phân quyền
- thời gian lưu dữ liệu
- audit trail

### `00-Process/ISO_9001/`

Tập trung vào quản lý chất lượng.

BA nên dùng để hiểu các điểm kiểm soát chất lượng và cách quản lý thay đổi.

### File đáng chú ý

- `00-Process/ISO_Compliance_Overview.md`
  File tổng quan.
- `00-Process/Compliance_Matrix_ISO.md`
  File đối chiếu tài liệu của dự án với các yêu cầu kiểm soát hoặc tiêu chuẩn.

## `01-Requirements/`

Đây là thư mục quan trọng nhất đối với BA và cũng là nơi PO thường xem nhiều nhất.

Nếu câu hỏi là "business cần gì?" hoặc "hệ thống phải làm gì?", gần như câu trả lời nằm ở đây.

### Mục đích

- ghi nhận bài toán và mục tiêu business
- chuyển bài toán đó thành yêu cầu rõ ràng cho hệ thống
- giữ liên kết giữa yêu cầu, thiết kế và kiểm thử

### Các nhóm con

### `01-Requirements/BRD/`

Nơi viết Business Requirements Document.

Nội dung nên có:

- bối cảnh business
- stakeholder
- luồng hiện tại
- pain point
- objective
- scope / out of scope
- business rules ở mức nghiệp vụ

Không nên nhét vào đây:

- chi tiết API
- bảng dữ liệu
- class diagram
- sequence kỹ thuật

### `01-Requirements/SRS/`

Nơi viết Software Requirements Specification.

Nội dung nên có:

- user role
- use case
- UI/UX expectation ở mức requirement
- field/input/output
- validation rules
- error cases
- permission rules
- acceptance criteria

### Root files ở `01-Requirements/`

- RTM template hoặc requirement traceability
  Dùng để nối yêu cầu với phần thiết kế, kiểm thử và release.

### BA nên dùng thư mục này thế nào

1. Viết BRD trước
2. Chuyển sang SRS
3. Tạo RTM
4. Chỉ khi 3 bước trên đủ rõ mới cho xuống architecture và LLD

## `02-Architecture/`

Đây là tầng mô tả cách hệ thống được tổ chức và hoạt động.

Sau khi yêu cầu đủ rõ, team dùng tầng này để chốt hướng triển khai.

### Mục đích

- mô tả kiến trúc tổng thể
- chốt quyết định kỹ thuật lớn
- chốt các kết nối giữa các thành phần
- chốt data model
- chốt security/privacy impact

### Các nhóm con

### `02-Architecture/AD/`

AD là Architecture Design.

Nơi mô tả:

- hệ thống tổng thể
- các app trong hệ thống
- boundary giữa web, mobile, backend, integration
- luồng chính

BA nên đọc khi cần hiểu:

- một use case đi qua bao nhiêu app
- module nào nằm ở app nào

### `02-Architecture/ADR/`

ADR là nơi giữ quyết định kiến trúc.

Rất hữu ích khi dự án chạy lâu và team quên vì sao ban đầu lại chọn hướng hiện tại.

Ví dụ câu hỏi phù hợp với ADR:

- vì sao chọn Firebase SSO
- vì sao worker mobile có API riêng
- vì sao dùng đánh dấu ngừng sử dụng dữ liệu thay vì xóa hẳn

### `02-Architecture/API/`

Nơi mô tả các điểm kết nối giữa frontend, mobile, backend hoặc hệ thống ngoài.

BA nên đọc để kiểm tra:

- endpoint có cover đúng use case không
- response có đủ dữ liệu cho UI không
- lỗi trả về có đủ để QA và kiểm thử nghiệm thu xử lý không

### `02-Architecture/Data_Model/`

Nơi mô tả dữ liệu chính của hệ thống và ý nghĩa của từng nhóm dữ liệu.

BA nên đọc để trả lời:

- đối tượng nghiệp vụ được lưu thành dữ liệu như thế nào
- field nào là dữ liệu gốc cần tin cậy
- relation nào có thể tạo duplicate hoặc inconsistency

### `02-Architecture/Data_Retention/`

Nơi mô tả vòng đời của dữ liệu.

BA nên dùng khi requirement có:

- xóa user
- lưu trữ lại dữ liệu cũ
- thời gian lưu dữ liệu
- cách xử lý liên quan tới quy định hoặc kiểm soát

### `02-Architecture/Security_Privacy/`

Nơi mô tả:

- phân quyền
- dữ liệu cá nhân nhạy cảm
- privacy impact
- security control

Đây là nơi BA nên phối hợp rất chặt với architect và security lead.

## `03-Lifecycle/`

Đây là thư mục dành cho giai đoạn build, test, release và vận hành.

BA không phải người phụ trách chính của mọi file ở đây, nhưng BA nên hiểu để phối hợp đúng.

### Mục đích

- kiểm soát thay đổi
- chuẩn bị test
- chuẩn bị deployment
- chuẩn bị go-live
- chuẩn bị runbook và incident handling

### Các nhóm con

### `03-Lifecycle/CICD/`

Nơi mô tả luồng build, pipeline và các điểm kiểm soát chất lượng.

BA thường không viết, nhưng nên biết để hiểu release đang phụ thuộc vào điều gì.

### `03-Lifecycle/ChangeMgmt/`

Nơi giữ đánh giá ảnh hưởng của thay đổi và ghi chú release.

BA nên dùng khi:

- có change request giữa đường
- cần đánh giá ảnh hưởng tới scope, test và timeline

### `03-Lifecycle/Config_Env/`

Nơi mô tả cấu hình và các môi trường chạy hệ thống.

BA nên đọc khi:

- một tính năng chỉ bật ở dev, staging hoặc production khác nhau
- cần hiểu cấu hình nào đang làm thay đổi hành vi của hệ thống

### `03-Lifecycle/Deployment/`

Nơi giữ kế hoạch triển khai và checklist sẵn sàng release.

BA nên phối hợp ở đây khi:

- release có ảnh hưởng tới thay đổi dữ liệu
- có thay đổi user flow lúc go-live
- cần training hoặc communication

### `03-Lifecycle/GoLive/`

Nơi tập trung checklist trước khi đưa hệ thống lên môi trường thật.

### `03-Lifecycle/Observability/`

Nơi mô tả log, monitoring và các chỉ số theo dõi hệ thống.

BA nên biết thư mục này tồn tại, vì có những acceptance criteria thực tế không chỉ nằm ở UI mà còn nằm ở khả năng theo dõi vận hành.

### `03-Lifecycle/Runbook/`

Nơi mô tả cách xử lý tình huống vận hành.

BA nên đọc để hiểu:

- production lỗi thì xử lý ra sao
- incident nào là business-critical
- backup/restore ảnh hưởng nghiệp vụ thế nào

### `03-Lifecycle/Test/`

Nơi mô tả test plan, test report, V&V.

Đây là chỗ BA rất hay cần phối hợp với QA.

## `04-Supporting/`

Đây là thư mục tài liệu hỗ trợ dùng chung.

Không phải chỗ chốt requirement chính, nhưng nếu thiếu nó thì team rất dễ nói lệch nhau.

### Mục đích

- chuẩn hóa ngôn ngữ
- chuẩn hóa naming
- chuẩn hóa tài liệu hướng dẫn sử dụng
- giữ guideline hỗ trợ dùng chung

### File thường có giá trị cao

- `Glossary.md`
  Giúp business và technical dùng cùng một cách gọi.
- `User_Manual.md`
  Hữu ích khi chuẩn bị kiểm thử nghiệm thu hoặc bàn giao.
- `Admin_Manual.md`
  Hữu ích cho team vận hành nội bộ.
- `DR_Backup_Plan.md`
  Quan trọng khi nghiệp vụ nhạy với mất dữ liệu.
- `Naming_Repo_Conventions.md`
  Giữ naming thống nhất.

### `04-Supporting/Platform_Guidelines/`

Đây là nhóm guideline kỹ thuật dùng chung cho Mercury.

BA không cần đọc hết, nhưng nên biết nó tồn tại để khi dev nói:

- Better Auth
- Supabase
- NextJS Standard
- React
- Shadcn UI

thì có nơi để tra chuẩn nền tảng.

## `05-LLD/`

Đây là tầng tài liệu chi tiết nhất.

BA không phải người viết chính duy nhất, nhưng BA cần vào đây để review logic ở mức module.

### Mục đích

- khóa luồng chi tiết của module
- khóa cách các thành phần chính tương tác với nhau
- tách riêng calculation logic phức tạp
- mô tả sequence xử lý happy path và error path

### `05-LLD/Module_Template/`

Đây là bộ template chuẩn:

- `TEMPLATE-LLD-001-Module_Design.md`
- `TEMPLATE-LLD-002-Class_Diagram.md`
- `TEMPLATE-LLD-003-Calculation_Logic.md`
- `TEMPLATE-LLD-004-Sequence_Diagram.md`

### Cách dùng thực tế

Trong dự án nhỏ:

- có thể dùng template này trực tiếp cho từng module

Trong dự án lớn:

- nên tạo subfolder theo app
- trong mỗi app, tách tiếp theo domain/module

QuickShift là ví dụ rất rõ:

- `05-LLD/Worker-Mobile/00-Overview/`
- `05-LLD/Worker-Mobile/01-Auth_Org/`
- `05-LLD/Worker-Mobile/02-Dashboard/`
- ...
- `05-LLD/Worker-Mobile/17-Skills/`

Mỗi module thường gồm:

- module design
- class diagram
- sequence diagram
- calculation logic nếu cần

Đây là cấu trúc tốt vì rõ ràng, dễ tìm và dễ lần lại khi cần review.

## `99-Indexes/`

Đây là thư mục điều hướng.

Khi hệ thống lớn lên, người mới rất dễ bị lạc. Index giúp:

- biết tài liệu nào là entrypoint
- biết module nào nằm ở đâu
- biết search theo từ khóa nào

Nó không tạo giá trị business trực tiếp, nhưng giúp tiết kiệm rất nhiều thời gian khi onboard người mới.

## 4. Khi cần tạo tài liệu mới, nên đặt vào đâu

Nếu BA đang có nhu cầu sau, đặt tài liệu vào đây:

- mô tả bài toán business mới
  -> `01-Requirements/BRD/`
- mô tả chi tiết chức năng hệ thống
  -> `01-Requirements/SRS/`
- ghi trace giữa requirement và test
  -> `01-Requirements/` hoặc RTM file
- mô tả kiến trúc tổng thể
  -> `02-Architecture/AD/`
- ghi quyết định kỹ thuật
  -> `02-Architecture/ADR/`
- mô tả API contract
  -> `02-Architecture/API/`
- mô tả dữ liệu hoặc entity
  -> `02-Architecture/Data_Model/`
- mô tả retention / privacy / permission
  -> `02-Architecture/Security_Privacy/` hoặc `Data_Retention/`
- mô tả test strategy
  -> `03-Lifecycle/Test/`
- mô tả deployment plan
  -> `03-Lifecycle/Deployment/`
- mô tả incident handling / restore
  -> `03-Lifecycle/Runbook/`
- mô tả chi tiết một module
  -> `05-LLD/`

## 5. Cấu trúc tối thiểu cho một dự án mới

Nếu bắt đầu một dự án Mercury mới, cấu trúc tối thiểu nên có là:

```text
00-Process/
01-Requirements/
  BRD/
  SRS/
02-Architecture/
  AD/
  API/
  Data_Model/
03-Lifecycle/
  Test/
  Deployment/
05-LLD/
  Module_Template/
99-Indexes/
```

Các thư mục khác có thể thêm sau khi hệ thống phức tạp hơn.

## 6. Kết luận

`Directory_Overview.md` nên được dùng như bản đồ thư mục, không phải như một danh sách template khô cứng.

Cách nhớ ngắn nhất:

- `00` để hiểu cách làm
- `01` để chốt yêu cầu
- `02` để chốt cách hệ thống sẽ hoạt động
- `03` để chuẩn bị test, release và vận hành
- `04` để hỗ trợ team làm cùng một cách
- `05` để đi xuống chi tiết
- `99` để tìm đường

Nếu BA team giữ đúng trật tự đó, tài liệu sẽ ít rối hơn rất nhiều.
