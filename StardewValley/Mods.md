# 🧩 Mods đang dùng — Stardew Valley 1.6.15

> Về [[00 Home]] · Áp dụng theo [[Daily]] · Mẹo chơi [[Mẹo]]
>
> _26 mod trong `F:\Games\StardewValley Mods`, nhóm theo chức năng. Bản `- VH` = Việt hóa → mình dùng bản VH vì đang chơi Việt hóa._
>
> _Khuôn mỗi mod: **Công dụng / Cách dùng / Phím / Cấu hình / Nexus**. Phím ghi "GMCM" = mặc định trống, tự gán trong Cài đặt → GMCM._

## 📑 Mục lục

1. [Bộ nền & Việt hóa](#1-bộ-nền--việt-hóa-bắt-buộc-cài-trước) (3)
2. [Cấu hình trong game](#2-cấu-hình-mod-trong-game) (2)
3. [Giao diện & thông tin](#3-giao-diện--thông-tin-uiinfo) (9)
4. [Kho đồ & rương](#4-kho-đồ--rương) (3)
5. [Tự động hóa & năng suất](#5-tự-động-hóa--năng-suất) (3)
6. [Tiện ích (QoL)](#6-tiện-ích-qol) (4)
7. [Cheat & Debug](#7-cheat--debug) (1)
8. [Hình ảnh / nhân vật](#8-hình-ảnh--nhân-vật) (1)
9. [Ghi chú bản VH & thứ tự cài](#9-ghi-chú-bản-vh--file-trùng) · [Thứ tự cài](#10-thứ-tự-cài--vận-hành-ổn-định-1615)

## 🎹 Bảng phím tắt nhanh

> _Chỉ liệt kê phím có sẵn / đáng nhớ. "GMCM" = mặc định trống, tự gán. Tránh gán trùng các phím đã dùng._

| Phím | Mod | Tác dụng |
|------|-----|----------|
| `F1` | Lookup Anything | Tra cứu vật/dân làng/cây dưới con trỏ |
| `M` | NPC Map Locations | Mở bản đồ (phím gốc game) |
| `B` | Chests Anywhere | Mở mọi rương từ xa |
| `Shift`+`F2` | All Chests Menu | Xem tất cả rương trong 1 menu |
| `U` | Automate | Bật/tắt lớp phủ sơ đồ máy–rương |
| `P` | CJB Cheats Menu | Mở menu cheat |
| GMCM | UI Info Suite 2 | Mở Lịch / Bảng nhiệm vụ |
| GMCM | Experience Bars | Ẩn/hiện thanh XP |
| GMCM | NPC Map Locations | Bật/tắt minimap |
| GMCM | Range Highlight | Hiện tất cả vùng tác dụng |
| GMCM | Better Crafting | Mở nhanh menu chế tạo |
| GMCM | MouseMoveMode | Bật/tắt đi bằng chuột |
| GMCM | QuickSave | Lưu nhanh giữa ngày |

---

## 1) Bộ nền & Việt hóa (bắt buộc, cài trước)

### SMAPI 4.5.2
- **Công dụng:** Loader để game chạy mod — thiếu nó thì mọi mod vô dụng.
- **Cách dùng:** Chạy `SMAPI 4.5.2 installer`, luôn mở game bằng `StardewModdingAPI`.
- **Phím:** —
- **Nexus:** https://www.nexusmods.com/stardewvalley/mods/2400

### Content Patcher 2.9.1
- **Công dụng:** Framework nạp nội dung (ảnh, data, dialogue) cho nhiều mod, gồm bản VH & Seasonal Cute Characters.
- **Cách dùng:** Để trong `Mods`, không thao tác trong game. Nạp lại bằng `patch reload` ở console SMAPI.
- **Phím:** —
- **Nexus:** https://www.nexusmods.com/stardewvalley/mods/1915

### Stardew Valley - Vietnamese
- **Công dụng:** Việt hóa toàn bộ game.
- **Cách dùng:** Chọn tiếng Việt trong phần Ngôn ngữ của game (lý do các mod nên dùng bản `- VH`).
- **Phím:** —
- **Phụ thuộc:** Content Patcher.
- **Nexus:** https://www.nexusmods.com/stardewvalley/mods/24371

## 2) Cấu hình mod trong game

### Generic Mod Config Menu (GMCM) 1.16.0
- **Công dụng:** Chỉnh cấu hình mọi mod trong game, khỏi sửa file JSON.
- **Cách dùng:** Cài đặt → menu GMCM → chọn mod để bật/tắt tính năng, đổi phím.
- **Phím:** — (mở qua nút Cài đặt trong menu game).
- **Nexus:** https://www.nexusmods.com/stardewvalley/mods/5098

### GMCMOptions 2.1.0
- **Công dụng:** Mở rộng GMCM (thêm widget như bảng chọn màu); là phụ thuộc cho vài mod.
- **Cách dùng:** Để trong `Mods`, chạy ngầm.
- **Phím:** —
- **Nexus:** https://www.nexusmods.com/stardewvalley/mods/10505

## 3) Giao diện & thông tin (UI/Info)

### UI Info Suite 2 (v2.3.7, bản VH)
![[ui-info-suite.png]]
- **Công dụng:** Hiện thông tin quan trọng lên màn hình (sinh nhật, thương nhân, thu hoạch, may mắn...).
- **Cách dùng:** Chủ yếu **rê chuột (hover)** vào các icon cạnh đồng hồ/tiền:
  - 🎂 sinh nhật NPC → ai sinh nhật, thích quà gì · 🍀 may mắn hôm nay · 🚂 giờ tàu chạy.
  - 💰 số tiền → thu nhập theo vụ/ngày · vật phẩm → giá bán, số đã ship, còn thiếu gói Cộng Đồng · cây trồng → còn mấy ngày thu hoạch.
- **Phím:** GMCM — gán **Mở Lịch** và **Mở Bảng nhiệm vụ** từ bất cứ đâu (mặc định trống).
- **Cấu hình:** GMCM → bật/tắt từng widget cho gọn màn hình, gán phím.
- **Nexus:** https://www.nexusmods.com/stardewvalley/mods/7098

### Experience Bars 1.4.6
![[experience-bars-1.png]]
![[experience-bars-2.png]]
- **Công dụng:** Hiện thanh kinh nghiệm (XP) và cấp của từng kỹ năng.
- **Cách dùng:** Thanh XP tự nổi khi nhận kinh nghiệm rồi mờ dần; xem để biết còn bao nhiêu là lên cấp.
- **Phím:** GMCM — gán phím **ẩn/hiện thanh XP** (mặc định trống).
- **Cấu hình:** GMCM → vị trí thanh, luôn hiện hay chỉ hiện khi nhận XP, cỡ chữ.
- **Nexus:** https://www.nexusmods.com/stardewvalley/mods/509

### NPC Map Locations 3.5.2
- **Công dụng:** Hiện vị trí dân làng trên bản đồ theo thời gian thực.
- **Cách dùng:** `M` mở bản đồ để tìm người tặng quà/kích hoạt sự kiện; bật minimap để theo dõi khi đi lại.
- **Phím:** `M` (phím gốc game); **bật/tắt minimap** gán trong GMCM.
- **Cấu hình:** GMCM → bật/tắt minimap, lọc NPC, hiện cả quái/thú nuôi.
- **Nexus:** https://www.nexusmods.com/stardewvalley/mods/239

### Lookup Anything 1.55.0
- **Công dụng:** Xem chi tiết vật phẩm/dân làng/cây trồng (sở thích quà, thời gian lớn, gói còn thiếu).
- **Cách dùng:** Đưa con trỏ vào mục tiêu → bấm `F1`.
- **Phím:** `F1` (tra cứu vật dưới con trỏ).
- **Nexus:** https://www.nexusmods.com/stardewvalley/mods/541

### Range Highlight 4.2.1
- **Công dụng:** Tô sáng vùng tác dụng của Vòi phun nước, Bù nhìn, Nhà ong...
- **Cách dùng:** Cầm vật lên (hoặc hover vật đã đặt) để xem vùng phủ — xếp Vòi phun nước phủ kín mà không chồng lấn.
- **Phím:** GMCM — gán phím **hiện tất cả vùng cùng lúc**.
- **Cấu hình:** GMCM → chọn vật được tô sáng, đổi màu vùng, bật/tắt hiện khi hover.
- **Nexus:** https://www.nexusmods.com/stardewvalley/mods/6752

### Show Missing Collection Entries 0.2.0
- **Công dụng:** Hiện mục còn thiếu trong bộ sưu tập (Collections).
- **Cách dùng:** Mở tab Collections để biết còn thiếu cá/khoáng sản/vật phẩm nào.
- **Phím:** — (hiện trong tab Collections).
- **Nexus:** https://www.nexusmods.com/stardewvalley/mods/47916

### Perfection Stats 1.6.7
- **Công dụng:** Theo dõi tiến độ hoàn hảo (Perfection %).
- **Cách dùng:** Mở bảng thống kê để biết còn thiếu gì để đạt 100%.
- **Phím:** — (gán trong GMCM nếu muốn).
- **Nexus:** https://www.nexusmods.com/stardewvalley/mods/41495

### Visible Fish 0.4.2
- **Công dụng:** Hiện cá bơi dưới nước để biết chỗ nào có cá.
- **Cách dùng:** Quan sát mặt nước trước khi quăng cần.
- **Phím:** — (tự động).
- **Nexus:** https://www.nexusmods.com/stardewvalley/mods/8897

### Stardew Dashboard 2.1.6
- **Công dụng:** Bảng thống kê nông trại (xem qua trình duyệt/cửa sổ riêng).
- **Cách dùng:** Mở dashboard xem tổng quan tài sản, sản xuất, tiến độ.
- **Phím:** — (xem qua trình duyệt).
- **Nexus:** https://www.nexusmods.com/stardewvalley/mods/43158

## 4) Kho đồ & rương

### Chests Anywhere 1.30.1
- **Công dụng:** Truy cập mọi rương từ xa.
- **Cách dùng:** Bấm `B` mở kho; đặt tên rương theo nhóm (Cây trồng, Quặng, Cá, Quà) để tìm nhanh.
- **Phím:** `B` (mở mọi rương từ xa).
- **Nexus:** https://www.nexusmods.com/stardewvalley/mods/518

### All Chests Menu 0.4.2
- **Công dụng:** Xem tất cả rương trong một menu tổng hợp.
- **Cách dùng:** Mở menu để nhìn nhanh toàn bộ kho, phối hợp với Chests Anywhere.
- **Phím:** `Shift` + `F2`.
- **Nexus:** https://www.nexusmods.com/stardewvalley/mods/14494

### Carry Chests 1.3.0
- **Công dụng:** Nhấc rương mà không cần dỡ hết đồ bên trong.
- **Cách dùng:** Tay không, đứng cạnh rương → bấm nút hành động để nhấc cả rương lẫn đồ, đi tới chỗ mới đặt lại.
- **Phím:** — (thao tác tay không).
- **Nexus:** https://www.nexusmods.com/stardewvalley/mods/30321

## 5) Tự động hóa & năng suất

### Automate 2.6.1
- **Công dụng:** Tự động chạy máy khi máy nối với rương.
- **Cách dùng:** Đặt 1 rương **chạm** cụm máy (Thùng ủ/Hũ ngâm/Lò luyện...); đổ nguyên liệu vào rương, thành phẩm tự trả về.
- **Phím:** `U` — bật/tắt lớp phủ sơ đồ máy–rương (đổi được trong GMCM).
- **Cấu hình:** GMCM → chọn loại máy tự động, tốc độ xử lý, lấy từ nhiều rương.
- **Nexus:** https://www.nexusmods.com/stardewvalley/mods/1063

### Better Crafting 2.18.0 (bản VH)
- **Công dụng:** Menu chế tạo gọn hơn — phân loại, tìm kiếm, yêu thích, chế từ rương gần.
- **Cách dùng:** Mở menu chế tạo như thường (thay giao diện gốc); bật **"chế từ rương gần"** để khỏi mang nguyên liệu.
- **Phím:** GMCM — gán phím **mở nhanh menu chế tạo** (mặc định dùng chung menu gốc).
- **Cấu hình:** GMCM → bán kính lấy nguyên liệu từ rương gần, gộp/ẩn công thức, yêu thích.
- **Nexus:** https://www.nexusmods.com/stardewvalley/mods/11115

### Better Friendship 1.1.3 (bản VH)
- **Công dụng:** Điều chỉnh mức tăng/giảm tình cảm với dân làng & vật nuôi.
- **Cách dùng:** GMCM chỉnh hệ số cho hợp lối chơi (vd giảm tốc độ tụt tình cảm).
- **Phím:** — (chỉ chỉnh hệ số).
- **Nexus:** https://www.nexusmods.com/stardewvalley/mods/10287

## 6) Tiện ích (QoL)

### MouseMoveMode 1.4.4
- **Công dụng:** Di chuyển nhân vật bằng chuột.
- **Cách dùng:** Click chuột (nút cấu hình) vào vị trí để nhân vật tự đi tới; tạm tắt khi cần thao tác công cụ chính xác bằng WASD.
- **Phím:** GMCM/`config.json` — gán phím **bật/tắt đi bằng chuột**.
- **Cấu hình:** GMCM/`config.json` → chọn nút chuột dùng để đi, bật/tắt trong nhà/ngoài trời.
- **Nexus:** https://www.nexusmods.com/stardewvalley/mods/2614

### QuickSave 1.5.0
- **Công dụng:** Lưu game giữa ngày (không cần ngủ).
- **Cách dùng:** Bấm phím lưu bất kỳ lúc nào → lần sau vào tiếp đúng thời điểm đó; có thể bật tự lưu định kỳ.
- **Phím:** GMCM/`config.json` — gán phím **lưu nhanh**.
- **Cấu hình:** GMCM/`config.json` → bật auto-save, đặt chu kỳ lưu.
- **Nexus:** https://www.nexusmods.com/stardewvalley/mods/26194

### MultiSaveContinued 1.0.7
- **Công dụng:** Quản lý nhiều bản lưu / sao lưu save an toàn.
- **Cách dùng:** Giữ nhiều điểm lưu, phòng hỏng save.
- **Phím:** — (qua menu lưu).
- **Nexus:** https://www.nexusmods.com/stardewvalley/mods/22953

### Farm Foundry 2.0.0.42
- **Công dụng:** Tùy biến bố cục nông trại (đặt nền, địa hình linh hoạt).
- **Cách dùng:** Dùng công cụ của mod để chỉnh layout ruộng theo ý.
- **Phím:** — (dùng công cụ của mod).
- **Nexus:** https://www.nexusmods.com/stardewvalley/mods/127

## 7) Cheat & Debug

### CJB Cheats Menu 1.42.0
- **Công dụng:** Menu cheat (thời tiết, thời gian, tiền, item, tình cảm...).
- **Cách dùng:** Bấm `P` mở menu. Dùng cẩn thận — dễ mất cảm giác cày cuốc nếu lạm dụng.
- **Phím:** `P` (mở menu cheat).
- **Nexus:** https://www.nexusmods.com/stardewvalley/mods/4

## 8) Hình ảnh / nhân vật

### Seasonal Cute Characters
- **Công dụng:** Thay hình nhân vật dễ thương, đổi theo mùa.
- **Cách dùng:** Để trong `Mods` cùng Content Patcher; chỉnh trong GMCM nếu mod hỗ trợ.
- **Phím:** — (content pack).
- **Phụ thuộc:** Content Patcher.
- **Nexus:** https://www.nexusmods.com/stardewvalley/search/?gsearch=Seasonal+Cute+Characters

---

## 9) Ghi chú bản VH & file trùng

- **Bản `- VH` (.rar)** = Việt hóa → **dùng bản này**. Bản gốc `.zip` cùng version chỉ giữ backup, **không cài cả hai cùng lúc** cho một mod (trùng UniqueID → lỗi).
  - Áp dụng cho: Better Crafting, Better Friendship, UI Info Suite 2.
- **SMAPI:** giữ `installer` để cài; file `.zip` chỉ là backup.

## 10) Thứ tự cài & vận hành ổn định (1.6.15)

1. **SMAPI** → **Content Patcher / GMCM / GMCMOptions** → **bản VH** → **UI/Info** → **kho & tự động hóa** → **tiện ích/cheat/hình ảnh**.
2. Mỗi mod chỉ giữ **1 bản** trong `Mods` (ưu tiên bản VH).
3. Thêm mod mới → vào game ngủ 1 đêm để chắc không lỗi sự kiện/máy móc.
4. Khi game/mod cập nhật, kiểm tra tương thích tại `smapi.io/mods`.
5. Lỗi → đọc log SMAPI để biết mod nào thiếu phụ thuộc hoặc sai version.
