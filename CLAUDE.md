# Quy ước commit

Khung chung (Problem → Solution → Implications, cách tách commit, các bước, cách viết lại
message đã push) nằm ở skill `commit`. Đây chỉ là phần riêng của repo này.

- **Ngôn ngữ:** **cả subject lẫn thân bài đều viết bằng tiếng Anh**, đúng như các commit
  gần nhất. Đây là điểm khác biệt lớn nhất so với vault `MyLifeExperience` bên cạnh — đừng
  bê quy ước tiếng Việt từ đó sang.
- **Subject: Conventional Commits.**

  ```
  <type>(<Scope>): <Câu mô tả, viết hoa chữ đầu, không dấu chấm cuối>
  ```

  - **type** — dùng đúng năm loại đã có: `feat` (thêm mảng nội dung mới), `fix` (sửa thông
    tin sai), `docs` (bổ sung, mở rộng nội dung đã đúng), `refactor` (sắp xếp lại, không
    đổi thông tin), `chore` (cấu hình vault, .gitignore, việc ngoài nội dung).
    Ranh giới `fix` và `docs` là chỗ hay lẫn: **`fix` khi thông tin cũ sai**, `docs` khi
    thông tin cũ đúng nhưng thiếu.
  - **Scope** — tên note **bỏ dấu**, viết hoa như tên note: `Meo` (Mẹo.md), `Ban do`
    (Bản đồ khu vực.md), `Quy hoach` (Quy hoạch nông trại.md), `Daily`, `Mods`. Cấu hình
    vault dùng `Obsidian`, cấu hình Claude Code dùng `Claude`. Chạm nhiều note cùng lúc thì
    bỏ scope hẳn, đừng liệt kê.
- **Scope chính là cái chuông báo tách commit.** Phải bỏ scope đi vì commit chạm cả `Daily`
  lẫn `Mods` mà hai thứ chẳng liên quan gì nhau, thì đó không phải lý do để bỏ scope — đó
  là dấu hiệu phải tách thành hai commit. Chỉ bỏ scope khi một ý duy nhất thật sự trải ra
  nhiều note.
- **"Vì sao" ở đây thường là một chi tiết game đã kiểm chứng lại:** mở khoá theo điều kiện
  gì, thư đến theo ngày hay theo level, bundle nào chặn bundle nào. Diff chỉ cho thấy con
  số đã đổi từ 5 thành 6; message mới nói được là vì cái tháp bị khoá.
- **Ghi nguồn đã kiểm chứng vào Implications.** Nội dung ở đây là chi tiết game, sai một
  chỗ là kéo hỏng cả chuỗi ngày phía sau, mà đọc note thì không thể biết chi tiết đó lấy
  từ đâu: đoán, đọc wiki, hay mở file game ra soi. Câu như *"Verified against the installed
  game files: Forest_WizardTower_Locked, the wizardJunimoNote mail entry"* nói cho người
  đọc biết độ tin của thông tin — thứ mà diff hoàn toàn không cho thấy. **Ghi cả phiên bản
  game khi chi tiết phụ thuộc phiên bản.**
- **Link gãy là hỏng thật.** Link đi theo `[[tên file]]` nên đổi tên note là gãy hàng loạt
  mà không có gì báo. Khi thay đổi có đổi tên hay di chuyển note, để kết quả kiểm chứng
  vào Implications.
- **Lịch sử:** phần lớn commit đã theo `type(Scope):` tiếng Anh; vài cái sớm nhất thì chưa
  (`Initial commit`, và hai commit tiếng Việt). Thân bài cũ phần lớn đã lập luận đúng tinh
  thần Problem → Solution → Implications nhưng ở dạng văn xuôi không nhãn. **Nhãn là quy
  ước kể từ đây**, không viết lại commit cũ.
