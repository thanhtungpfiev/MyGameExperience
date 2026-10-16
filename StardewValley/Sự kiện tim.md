# ❤️ Sự kiện tim — chọn câu nào

> Về [[00 Home]] · Kết bạn [[Mẹo#❤️ Kết bạn & hẹn hò|Mẹo — Kết bạn & hẹn hò]] · Bí mật [[Bí mật & Sự kiện ẩn]]
>
> _Note này trả lời **"trong cắt cảnh, chọn câu nào để không mất tim"**, kèm điều kiện để cắt cảnh nổ ra. Đúng cho mọi save. Save nào đã xem cảnh nào thì tích trong note Tiến độ của save đó (save Wind: [[Wind - Tiến độ#❤️ Haley|Wind - Tiến độ]])._
>
> _Độ tin: **✔️ code** — câu chữ và điểm lấy thẳng từ `Data/Events` của **bản Việt hóa đang cài** (game 1.6.15), nên câu trong note giống hệt câu hiện trên màn hình. Toạ độ đồ vật lấy từ code game dịch ngược (`Event.cs`)._

> [!info] Đọc bảng thế nào
> - Điểm cộng/trừ vào **người hỏi câu đó** (thường là chính nhân vật của sự kiện). **1 tim = 250 điểm.**
> - Sự kiện tim nổ ra khi **bước vào đúng khu**, đủ tim, đúng giờ/thời tiết, và người đó **đang đứng trong khu đó**. Mỗi cảnh **chỉ xem 1 lần**, chọn sai là mất luôn, không chơi lại được (trừ khi mở lại save).
> - Bật [[Mods#Debug Mode 1.17.4|Debug Mode]] (`Z`) khi đang xem cảnh để thấy **ID sự kiện** — đối chiếu với cột ID ở dưới.

---

## 💛 Haley

Nhà: **Nhà của Emily & Haley** (Emily & Haley's House, 2 Willow Lane). Trần **8 tim** cho tới khi tặng **Bó hoa (Bouquet)**.

| Tim | ID | Ở đâu · khi nào | Chọn câu này | Đừng chọn |
|---|---|---|---|---|
| **2** | 11 | Nhà của Emily & Haley · **cả Haley lẫn Emily ở nhà** | **"Haley, sao không coi đây là việc hàng tuần của cậu?"** **+30** | "Đừng phàn nàn nữa và dọn chúng đi!" **−50** · "Emily, hãy tỏ ra cao thượng và dọn dẹp lần này." **−30** |
| **4** | 12 | Nhà của Emily & Haley · Haley ở nhà | Hỏi *"Cậu cũng khá khỏe đấy chứ nhỉ?"* → **"Ừ"** **+30** | "Không" **−30** |
| **6** | 13 | **Bãi biển**, 10:00–16:00 · mọi thời tiết · trừ mùa Đông | **"Mình rất tiếc..."** **+50** | "Bình tĩnh nào, mình sẽ mua cho cậu một cái mới!" **−30** — Haley gắt vì vòng là của bà ngoại để lại |
| **8** | 14 | **Rừng Cindersap**, gần trại Marnie · 10:00–16:00 · **trời nắng** · trừ mùa Đông | _Không có câu hỏi_ — cứ xem hết | — |
| **10** | 15 | Nhà của Emily & Haley · Haley ở nhà · **phải đang hẹn hò** (đã tặng Bó hoa) | Hỏi *"Thế... cậu thấy sao?"* → **"Nhìn tuyệt đấy!"** **+10** | "Nó dùng để làm gì?" **0** · "Tớ từng thấy cái đẹp hơn rồi." **−50** |
| **14** | 6184643 | **Thị trấn Pelican**, 08:00–15:00 · trời nắng · **đã cưới Haley** | _Không có câu hỏi_ | — |

**🔍 Tìm vòng tay (sự kiện 6 tim):** sau đoạn hỏi, game cho tự đi tìm **Vòng tay thất lạc của Harley** (Haley's Lost Bracelet — bản dịch gõ nhầm "Harley"). Vòng nằm ở **ô (53, 8) của Bãi biển**, mép cát phía trên **gần lều của Elliott**. Cứ đi tới là nhặt được. _(✔️ code: `Event.cs`, `haleyBeach`; save Wind tìm thấy đúng chỗ này hôm Xuân 28 Năm 1.)_

**🎂 Chuỗi sau 14 tim (đã cưới):**
1. Xem xong cảnh 14 tim, Haley hỏi ở **nhà trên nông trại** (ID 8675611, 06:20–17:00): *"Đồng ý mang bánh sô-cô-la tới chứ?"* — **"Có"** hay **"Có (ngần ngừ)"** đều **không đổi điểm**. Chọn "ngần ngừ" thì chỉ bị Haley dọa cho ngủ chuồng gà.
2. Ngày nắng kế tiếp, 06:00–15:00, vào **Thị trấn Pelican** với **1 Bánh sô-cô-la (Chocolate Cake)** trong túi (ID 6184644). **Không có bánh thì cảnh không nổ ra** — nấu hoặc mua sẵn từ hôm trước.

> [!tip] Lộ trình mua sắm cho Haley
> - **8 tim** → **Bó hoa** 200g ở tiệm Pierre → mở trần 10 tim, mở cảnh 10 tim.
> - **10 tim** + nhà đã nâng cấp ít nhất 1 lần → **Dây chuyền tiên cá (Mermaid's Pendant)** 5.000g, ông lão ở **Bãi biển ngày mưa** — xem [[Mẹo#Mốc hẹn hò & cưới|Mốc hẹn hò & cưới]].

> [!note]- Sự kiện 10 tim chung của các cô (ID 195019 · 195012)
> Chỉ nổ ra khi **hẹn hò cùng lúc cả 6 cô** (Haley, Emily, Penny, Abigail, Leah, Maru) đều 10 tim. Chơi một người thì không bao giờ gặp.

---

## Người khác

_Chưa ghi — thêm khi save nào chuyển sang theo người khác. Cách tra: `strings/Data/Events/<khu>.xnb` trong thư mục mod Việt hóa, tìm `f <Tên> <điểm>`, rồi đọc các dòng `$q` / `$r <id> <điểm> …` (điểm là số thứ hai sau `$r`)._
