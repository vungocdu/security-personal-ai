# Mercury Solution Document Kit

Tài liệu này giải thích cấu trúc thư mục của bộ `ISO_Doc_Kit` bằng ngôn ngữ gần với công việc hằng ngày của Business Analyst và Product Owner.

Mục tiêu không phải để nói về ISO theo kiểu kiểm tra hồ sơ cho đủ. Mục tiêu là để cả BA và PO biết:
- nên bắt đầu đọc từ đâu
- tài liệu nào nên làm trước, tài liệu nào làm sau
- mỗi thư mục giúp trả lời câu hỏi gì trong dự án
- khi triển khai một hệ thống như QuickShift thì nên đặt tài liệu vào đâu cho dễ tìm, dễ phối hợp

Có thể hiểu ngắn gọn: đây là bộ khung giúp team đi từ lúc hiểu bài toán, làm rõ yêu cầu, chốt cách hệ thống hoạt động, cho tới lúc kiểm thử, phát hành và vận hành.

Khi dùng AI agent trong quá trình này, Mercury áp dụng một nguyên tắc ngắn gọn:

- `gstack` giữ vai trò điều phối workflow theo từng stage như Think, Plan, Build, Review, Test, Ship
- các skill theo tech stack giữ vai trò chuyên gia kỹ thuật để xử lý đúng backend, frontend, database hoặc các lớp đặc thù khác

Ví dụ, team có thể đi theo stage của `gstack`, nhưng ở giai đoạn Build lại dùng thêm `php-expert`, skill frontend riêng của dự án, hoặc skill database riêng để coding và review sâu hơn. Cách kết hợp này giúp người đọc không phải chọn một trong hai, mà hiểu rằng chúng bổ sung cho nhau.

## 1. Cách đọc bộ tài liệu này

Nếu bạn là BA mới vào dự án, có thể đi theo thứ tự này:

1. `00-Process/`
   Đọc để hiểu cách team vận hành tài liệu, các bước làm việc và đầu ra cần có ở từng giai đoạn.
2. `01-Requirements/`
   Đây là nơi BA làm việc nhiều nhất. Nơi mô tả bài toán, yêu cầu và cách theo dõi yêu cầu xuyên suốt dự án.
3. `02-Architecture/`
   Khi yêu cầu đã rõ, sang đây để chốt cách hệ thống được tổ chức, các kết nối, dữ liệu và các lưu ý về quyền hoặc bảo mật.
4. `03-Lifecycle/`
   Khi sản phẩm sắp build, test hoặc release, dùng nhóm tài liệu này để quản lý kiểm thử, triển khai, vận hành và thay đổi.
5. `05-LLD/`
   Khi từng phần của hệ thống đã được chốt ở mức yêu cầu và hướng thiết kế, team đi tiếp xuống tài liệu chi tiết cho từng module hoặc từng app.

Nếu bạn là Product Owner, thường chỉ cần nhớ 3 điểm:

1. `01-Requirements/` để xem phạm vi và yêu cầu đã chốt tới đâu
2. `02-Architecture/` để hiểu hệ thống được tổ chức như thế nào ở mức đủ để ra quyết định
3. `03-Lifecycle/` để theo dõi tình trạng test, release và vận hành

Nói ngắn gọn:

- `01-Requirements` trả lời: "Sản phẩm cần làm gì?"
- `02-Architecture` trả lời: "Hệ thống được tổ chức ra sao để làm được việc đó?"
- `03-Lifecycle` trả lời: "Hệ thống được kiểm thử, triển khai và vận hành như thế nào?"
- `05-LLD` trả lời: "Từng phần nhỏ sẽ được làm chi tiết ra sao?"

## 2. Tư duy tổ chức tài liệu của Mercury

Mercury không gom tất cả mọi thứ vào một file lớn. Mỗi nhóm tài liệu có một vai trò riêng để mọi người dễ tìm, dễ trao đổi và ít hiểu sai nhau.

Có thể hình dung đơn giản như sau:

- BRD là nơi nói về bài toán kinh doanh và mục tiêu cần đạt
- SRS là nơi chuyển bài toán đó thành yêu cầu rõ ràng cho hệ thống
- Tài liệu kiến trúc, API và dữ liệu là nơi giải thích hệ thống sẽ được tổ chức như thế nào
- LLD là nơi mô tả rất chi tiết từng phần để dev và QA bám theo

Nếu trộn các tầng này vào với nhau thì team rất dễ lệch hiểu:

- business hiểu một kiểu
- dev triển khai một kiểu
- QA kiểm thử theo một kiểu khác
- tới lúc release mới lộ ra thiếu case hoặc thiếu rule

Đó là lý do bộ khung thư mục này tồn tại.

## 3. Giải thích từng thư mục

## `00-Process/`

Đây là tầng mô tả cách team làm việc với tài liệu và vòng đời phần mềm.

Thư mục này không nói về một chức năng cụ thể. Nó giúp mọi người hiểu bối cảnh chung: khi nào cần loại tài liệu nào, vì sao cần, và tài liệu đi cùng dự án ra sao từ đầu đến cuối.

### Khi nào BA cần dùng

- khi cần hiểu chuẩn tài liệu của dự án
- khi cần biết đầu ra nào là bắt buộc trước khi qua bước tiếp theo
- khi cần giải thích cho stakeholder vì sao dự án cần đủ các nhóm tài liệu chính

### Các nhóm con chính

- `AI_Development/`
  Hướng dẫn cách dùng AI trong quá trình phân tích, viết nháp, rà soát tài liệu.
- `ISO_12207/`
  Chuẩn về software lifecycle.
- `ISO_15288/`
  Chuẩn về system lifecycle.
- `ISO_27001/`
  Chuẩn về bảo mật thông tin.
- `ISO_9001/`
  Chuẩn về quản lý chất lượng.

### File BA nên biết

- `00-Process/ISO_Compliance_Overview.md`
  File nhìn toàn cảnh. Dùng khi cần hiểu kit này sinh ra để làm gì.
- `00-Process/Compliance_Matrix_ISO.md`
  Dùng khi cần đối chiếu tài liệu của dự án với các yêu cầu kiểm soát hoặc tiêu chuẩn.

## `01-Requirements/`

Đây là nơi BA làm việc nhiều nhất.

Nếu chưa biết bắt đầu từ đâu, gần như luôn bắt đầu ở đây.

### `01-Requirements/BRD/`

Nơi mô tả bài toán kinh doanh.

BRD dùng để trả lời:

- tại sao phải làm
- ai là user/stakeholder
- business flow hiện tại là gì
- pain point là gì
- kết quả nào được xem là thành công ở góc nhìn business

### `01-Requirements/SRS/`

Nơi chuyển bài toán kinh doanh thành yêu cầu rõ ràng cho hệ thống.

SRS dùng để trả lời:

- hệ thống cần có màn hình nào
- chức năng nào
- quyền nào
- rule nào
- input/output nào
- lỗi nào
- constraint nào
- ngoại lệ nào cần xử lý

### Tài liệu BA thường dùng nhất trong thư mục này

- BRD template
- SRS template
- RTM template, tức bảng giúp theo dõi một yêu cầu đã đi từ lúc mô tả cho tới lúc test và release hay chưa
- Glossary
- NFR hoặc các tài liệu giúp theo dõi yêu cầu xuyên suốt

### BA nên dùng theo thứ tự

1. BRD
2. SRS
3. RTM

Không nên đi xuống tài liệu chi tiết khi BRD hoặc SRS còn mơ hồ. Làm vậy thường khiến team sửa đi sửa lại rất tốn thời gian.

## `02-Architecture/`

Đây là tầng mô tả cách hệ thống được tổ chức và hoạt động.

Sau khi BA và stakeholder chốt yêu cầu, team kỹ thuật sẽ dùng nhóm thư mục này để chốt hướng triển khai.

### `02-Architecture/AD/`

AD là tài liệu mô tả kiến trúc tổng thể.

Nó trả lời:

- hệ thống gồm những app hay thành phần nào
- web, mobile, backend, integration tách ra sao
- boundary giữa các hệ ra sao
- đâu là core flow

### `02-Architecture/ADR/`

ADR là nơi ghi lại các quyết định kiến trúc quan trọng.

Nó trả lời:

- vì sao team chọn cách A mà không chọn cách B
- quyết định nào đủ quan trọng để cần ghi lại, tránh sau này tranh luận lại từ đầu

Ví dụ:

- chọn Firebase SSO hay nhà cung cấp đăng nhập khác
- chọn API riêng cho mobile hay dùng chung
- chọn đánh dấu ngừng sử dụng dữ liệu thay vì xóa hẳn, hay xóa hẳn ngay

### `02-Architecture/API/`

Nơi mô tả các điểm kết nối giữa frontend, mobile, backend hoặc hệ thống ngoài.

BA không phải lúc nào cũng viết phần này, nhưng BA vẫn nên đọc để kiểm tra:

- hệ thống đã cover đúng use case chưa
- tên field có khớp ngôn ngữ business không
- tình huống lỗi có được mô tả đủ để UI và QA xử lý không

### `02-Architecture/Data_Model/`

Nơi mô tả dữ liệu chính của hệ thống được tổ chức như thế nào.

BA nên đọc để hiểu:

- đối tượng nghiệp vụ được lưu thành các bảng hoặc nhóm dữ liệu như thế nào
- field nào là bắt buộc
- quan hệ nào là 1-n, n-n
- dữ liệu gốc nên được lấy từ đâu

### `02-Architecture/Security_Privacy/`

Nơi mô tả quyền truy cập, dữ liệu nhạy cảm, thời gian lưu trữ và các kiểm soát quan trọng về bảo mật hoặc riêng tư.

BA nên dùng khi có các câu hỏi như:

- dữ liệu nào là dữ liệu cá nhân nhạy cảm
- ai được xem gì
- dữ liệu lưu bao lâu
- trường hợp xóa user thì hệ thống xử lý ra sao

## `03-Lifecycle/`

Đây là nhóm tài liệu đi cùng giai đoạn thực thi, kiểm thử, release và vận hành.

BA thường không phải người viết chính ở đây, nhưng vẫn cần hiểu để phối hợp với QA, dev và devops.

### `03-Lifecycle/Test/`

Dùng cho kế hoạch kiểm thử, kết quả kiểm thử và các tài liệu xác nhận hệ thống đã được kiểm tra.

BA cần đọc khi:

- cần xác nhận phạm vi test có bám đúng yêu cầu không
- cần kiểm tra acceptance criteria đã được test chưa

### `03-Lifecycle/Deployment/`

Dùng cho kế hoạch triển khai, checklist sẵn sàng release và các bước chuyển đổi khi đưa hệ thống lên môi trường thật.

BA cần phối hợp khi:

- release có ảnh hưởng user thật
- cần xác nhận dữ liệu chuẩn bị ban đầu, thay đổi cấu trúc dữ liệu hoặc cơ chế bật tắt tính năng
- cần chốt training hoặc go-live communication

### `03-Lifecycle/Runbook/`

Dùng cho vận hành, xử lý sự cố, sao lưu và khôi phục, cùng các ghi nhận sau sự cố.

BA nên đọc để hiểu:

- nếu hệ thống thật gặp lỗi thì team xử lý ra sao
- các tình huống nghiệp vụ đặc biệt được support thế nào

### `03-Lifecycle/ChangeMgmt/`

Dùng để quản lý thay đổi của dự án.

BA cần dùng khi:

- change request phát sinh giữa sprint
- cần impact assessment
- cần ghi lại version thay đổi của requirement

## `04-Supporting/`

Đây là nhóm tài liệu hỗ trợ.

Không phải nơi mô tả yêu cầu chính, nhưng rất quan trọng vì nó giúp cả team dùng chung cách gọi và cách hiểu.

Ví dụ:

- `Glossary.md`
  Giúp BA, dev, QA, stakeholder dùng cùng một định nghĩa.
- `User_Manual.md`, `Admin_Manual.md`
  Hữu ích khi BA cần chuẩn bị kiểm thử nghiệm thu hoặc bàn giao sử dụng.
- `Naming_Repo_Conventions.md`
  Giúp naming của tài liệu, module, branch, ticket, API nhất quán.
- `Platform_Guidelines/`
  Là nơi chứa guideline kỹ thuật chung của Mercury.

## `05-LLD/`

Đây là tầng chi tiết nhất của bộ tài liệu.

BA không phải lúc nào cũng là người viết chính, nhưng nên hiểu cách thư mục này được tổ chức để review logic đúng chỗ, đúng file.

### `05-LLD/Module_Template/`

Đây là nhóm template nền:

- Module Design
- Class Diagram
- Calculation Logic
- Sequence Diagram

### Mercury dùng `05-LLD` như thế nào

QuickShift là ví dụ rất rõ cho cách chia tài liệu chi tiết theo từng app rồi từng module.

Trong QuickShift, `docs/05-LLD/` không chỉ có template. Nó còn tách theo app:

- `Worker-Mobile/`
- `Customer-Web/`
- có index file riêng cho từng app

Riêng `Worker-Mobile/` còn đi xa hơn:

- `00-Overview/`
- `01-Auth_Org/`
- `02-Dashboard/`
- `03-Assignments_Offers/`
- ...
- `17-Skills/`
- `18-Zairyu/`

Mỗi module thường có 3 đến 4 tài liệu:

- `Module_Design`
- `Class_Diagram`
- `Sequence_Diagram`
- `Calculation_Logic` nếu module có rule tính toán

Đây là cách tổ chức rất phù hợp với hệ thống lớn. Khi BA hoặc PO hỏi "logic phần skills của Worker Mobile nằm ở đâu?", team có thể chỉ đúng một thư mục thay vì phải lục trong hàng chục file khác nhau.

## `99-Indexes/`

Đây là tầng điều hướng và tổng hợp.

Khi solution lớn dần, người mới rất dễ lạc. `99-Indexes` giúp tạo:

- document index
- link entrypoint
- mapping từ domain sang file

Đây là chỗ rất hữu ích cho BA lead, PO hoặc PM khi cần onboard người mới nhanh.

## 4. Nên đi theo flow tài liệu nào

Dưới đây là flow khuyến nghị cho hầu hết hệ thống của Mercury.

### Giai đoạn 1, làm rõ bài toán

Tạo hoặc cập nhật:

- `01-Requirements/BRD/...`
- `04-Supporting/Glossary.md`

Kết quả mong muốn:

- team hiểu bài toán
- stakeholder đồng ý phạm vi ở mức business

### Giai đoạn 2, chuyển thành yêu cầu rõ ràng cho hệ thống

Tạo hoặc cập nhật:

- `01-Requirements/SRS/...`
- `01-Requirements/TEMPLATE-REQ-007-Requirements_Traceability_Matrix.md`

Kết quả mong muốn:

- có danh sách chức năng rõ
- có acceptance criteria rõ
- có thể theo dõi yêu cầu từ lúc mô tả cho tới lúc thiết kế và kiểm thử

### Giai đoạn 3, chốt hướng triển khai

Tạo hoặc cập nhật:

- `02-Architecture/AD/...`
- `02-Architecture/ADR/...`
- `02-Architecture/API/...`
- `02-Architecture/Data_Model/...`
- `02-Architecture/Security_Privacy/...`

Kết quả mong muốn:

- team biết sẽ build theo hướng nào
- dữ liệu và các kết nối đã chốt ở mức đủ để team bắt tay làm

### Giai đoạn 4, chuẩn bị kiểm thử và release

Tạo hoặc cập nhật:

- `03-Lifecycle/Test/...`
- `03-Lifecycle/Deployment/...`
- `03-Lifecycle/ChangeMgmt/...`
- `03-Lifecycle/Runbook/...`

Kết quả mong muốn:

- release không bị mù
- test và go-live có tài liệu bám theo

### Giai đoạn 5, đi xuống chi tiết từng module

Tạo hoặc cập nhật:

- `05-LLD/<App hoặc Module>/...`

Kết quả mong muốn:

- dev implement đúng
- QA test đúng nhánh
- logic tính toán và luồng xử lý phức tạp được khóa bằng tài liệu

## 5. QuickShift là ví dụ tham chiếu tốt như thế nào

Trong tài liệu QuickShift, có thể thấy rất rõ cách Mercury đang tổ chức tài liệu:

- `docs/01-Requirements/BRD/`
  chứa BRD thật và sample business material
- `docs/01-Requirements/SRS/`
  chứa SRS cho auth, RBAC, worker mobile, customer mobile
- `docs/02-Architecture/`
  chia rõ AD, ADR, API, Data_Model, Security_Privacy
- `docs/03-Lifecycle/Infrastructure/`
  chứa phần hạ tầng và hướng dẫn vận hành thực tế hơn so với bộ kit gốc
- `docs/05-LLD/Worker-Mobile/`
  chia theo module rất chi tiết, đây là mẫu tốt để BA team hiểu một system lớn được tách tài liệu như thế nào

Điểm đáng học từ QuickShift:

- mỗi tầng tài liệu có một trách nhiệm riêng
- tài liệu index được dùng để điều hướng rất rõ
- LLD không để phẳng, mà tách theo app và domain
- các module có logic tính toán riêng được tách file riêng, rất dễ review

## 6. Khi cần tìm thông tin, nên vào đâu

Nếu câu hỏi là:

- "Business muốn gì?"
  Vào `01-Requirements/BRD/`
- "Hệ thống phải làm gì?"
  Vào `01-Requirements/SRS/`
- "Requirement này đã được trace sang test hay chưa?"
  Vào `01-Requirements/...Traceability...`
- "Màn hình hoặc app này đang gọi sang đâu?"
  Vào `02-Architecture/API/`
- "Field này lưu ở đâu trong DB?"
  Vào `02-Architecture/Data_Model/`
- "Quyền này ai được phép?"
  Vào `02-Architecture/Security_Privacy/`
- "Release này cần chuẩn bị gì?"
  Vào `03-Lifecycle/Deployment/` hoặc `03-Lifecycle/GoLive/`
- "Incident xảy ra thì xử lý thế nào?"
  Vào `03-Lifecycle/Runbook/`
- "Module này được mô tả chi tiết ra sao?"
  Vào `05-LLD/`

## 7. Gợi ý đặt tên tài liệu

Nên giữ tên file có cấu trúc. Ví dụ:

- `BRD-QS-WORKER-MOBILE-2026-001.md`
- `SRS-QS-WORKER-SKILLS-2026-001.md`
- `API-QS-WORKER-MOBILE-SKILLS-2026-001.md`
- `DM-PG-QS-WORKER-MANAGEMENT-2026-001.md`
- `LLD-QS-WM-SKILLS-2026-001-Module_Design.md`

Lợi ích rất rõ:

- nhìn tên là biết tầng tài liệu
- biết module nào
- biết năm và version
- dễ tìm, dễ kiểm tra, dễ lần ngược lại khi cần

## 8. Lưu ý thực tế khi dùng bộ kit này

- Không cố nhét hết mọi thứ vào BRD.
  BRD là nơi giữ bài toán business, không phải nơi mô tả chi tiết API hay database.
- Không đi xuống tài liệu chi tiết quá sớm.
  Nếu SRS chưa chốt, phần chi tiết sẽ đổi liên tục.
- Luôn nghĩ theo chuỗi liên kết.
  Từ bài toán business tới yêu cầu, tới cách làm, tới test và vận hành, mọi thứ nên nối được với nhau.
- Với solution nhiều app, nên tách tài liệu theo app trước, rồi mới tách theo module.
  QuickShift đang làm đúng chỗ này.
- Nếu có logic tính toán, nên cân nhắc tách file `Calculation_Logic`.
  Cách này giúp BA, PO, dev và QA cùng review rule dễ hơn nhiều.

## 9. Gợi ý dùng bộ kit cho dự án mới

Nếu bắt đầu một dự án Mercury mới, có thể đi theo cách đơn giản sau:

1. Dùng nguyên khung folder này
2. Tạo `BRD` và `SRS` trước cho các domain chính
3. Tạo `AD`, `API`, `Data_Model` song song khi scope đã rõ
4. Tạo `05-LLD/<App>/00-Overview/` trước
5. Sau đó mới bẻ module chi tiết theo domain

Với dự án nhỏ, có thể ít folder con hơn.

Với dự án lớn như QuickShift, nên mạnh dạn tách sâu theo app và module. Làm sớm sẽ dễ quản lý hơn rất nhiều về sau.

## 10. Kết luận

`ISO_Doc_Kit` không chỉ là bộ template để điền cho đủ.

Nếu dùng đúng, nó là bản đồ chung để BA, PO, Dev, QA, DevOps và stakeholder nhìn cùng một solution theo cùng một cấu trúc.

Nếu cần nhớ thật nhanh, chỉ cần nhớ:

- `00-Process` để hiểu cách làm việc
- `01-Requirements` để chốt nhu cầu
- `02-Architecture` để chốt cách hệ thống sẽ hoạt động
- `03-Lifecycle` để chuẩn bị test, release và vận hành
- `05-LLD` để đi xuống chi tiết từng phần

Chừng đó là đủ để BA và PO định vị mình đang ở đâu trong bộ tài liệu và nên mở file nào trước.
