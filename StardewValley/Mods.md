# 🧩 Mods đang dùng — Stardew Valley 1.6.15

> Về [[00 Home]] · Áp dụng theo [[Daily]] · Mẹo chơi [[Mẹo]] · Bản đồ [[Bản đồ khu vực]]
>
> _26 mục trong `F:\Games\StardewValley Mods` — **25 mod SMAPI** + **1 công cụ ngoài game** (Farm Foundry), nhóm theo chức năng. Bản `- VH` = Việt hóa → mình dùng bản VH vì đang chơi Việt hóa._
>
> _Khuôn mỗi mod: **Công dụng / Cách dùng / Phím / Cấu hình / Nexus**. Phím ghi "GMCM" = mặc định trống, tự gán trong Cài đặt → GMCM._

## 📑 Mục lục

1. [[#1) Bộ nền & Việt hóa (bắt buộc, cài trước)|Bộ nền & Việt hóa]] (3)
2. [[#2) Cấu hình mod trong game|Cấu hình trong game]] (2)
3. [[#3) Giao diện & thông tin (UI/Info)|Giao diện & thông tin]] (10)
4. [[#4) Kho đồ & rương|Kho đồ & rương]] (3)
5. [[#5) Tự động hóa & năng suất|Tự động hóa & năng suất]] (2)
6. [[#6) Tiện ích (QoL)|Tiện ích (QoL)]] (3)
7. [[#7) Cheat & Debug|Cheat & Debug]] (1)
8. [[#8) Hình ảnh / nhân vật|Hình ảnh / nhân vật]] (1)
9. [[#9) Ghi chú bản VH & file trùng|Ghi chú bản VH & file trùng]] · [[#10) Thứ tự cài & vận hành ổn định (1.6.15)|Thứ tự cài]]
10. [[#🧰 Công cụ ngoài game|Công cụ ngoài game]] (1)
11. [[#🛟 An toàn save (quan trọng)|🛟 An toàn save]] — serializer, Save Backup, cách khôi phục

## 🎹 Bảng phím tắt nhanh

> _Chỉ liệt kê phím có sẵn / đáng nhớ. "GMCM" = mặc định trống, tự gán. Tránh gán trùng các phím đã dùng._

| Phím | Mod | Tác dụng |
|------|-----|----------|
| `F1` | Lookup Anything | Tra cứu vật/dân làng/cây dưới con trỏ |
| `M` | NPC Map Locations | Mở bản đồ (phím gốc game) |
| `B` | Chests Anywhere | Mở mọi rương từ xa (⚠️ trùng phím Lịch của UI Info Suite 2) |
| `B` | UI Info Suite 2 | Mở Lịch (⚠️ trùng phím của Chests Anywhere) |
| `H` | UI Info Suite 2 | Mở Bảng nhiệm vụ |
| `Shift`+`F2` | All Chests Menu | Xem tất cả rương trong 1 menu |
| `U` | Automate | Bật/tắt lớp phủ sơ đồ máy–rương |
| `P` | CJB Cheats Menu | Mở menu cheat |
| `F5` / `F7` | QuickSave | Lưu nhanh giữa ngày / nạp lại bản lưu nhanh |
| `F8` | MultiSave - Continued | Tạo bản lưu mốc thủ công |
| `F10` | Stardew Dashboard | Mở bảng thống kê tổng hợp |
| GMCM | Experience Bars | Ẩn/hiện thanh XP |
| GMCM | NPC Map Locations | Bật/tắt minimap |
| GMCM | Range Highlight | Hiện tất cả vùng tác dụng |
| GMCM | Better Crafting | Mở nhanh menu chế tạo |
| GMCM | MouseMoveMode | Bật/tắt đi bằng chuột |

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
![[assets/ui-info-suite.png|600]]
- **Công dụng:** Hiện thông tin quan trọng lên màn hình (sinh nhật, thương nhân, thu hoạch, may mắn...).
- **Cách dùng:** Chủ yếu **rê chuột (hover)** vào các icon cạnh đồng hồ/tiền:
  - 🎂 sinh nhật NPC → ai sinh nhật, thích quà gì · 🍀 may mắn hôm nay · 🚂 giờ tàu chạy.
  - 💰 số tiền → thu nhập theo vụ/ngày · vật phẩm → giá bán, số đã ship, còn thiếu gói Cộng Đồng · cây trồng → còn mấy ngày thu hoạch.
- **Phím:** `B` mở **Lịch**, `H` mở **Bảng nhiệm vụ** từ bất cứ đâu (gán trong GMCM; mặc định gốc là trống).
  - ⚠️ `B` đang **trùng với Chests Anywhere** — nên đổi một trong hai (gợi ý: Lịch → `C`, hoặc rương → `K`).
- **Cấu hình:** GMCM → bật/tắt từng widget cho gọn màn hình, gán phím.
- **Nexus:** https://www.nexusmods.com/stardewvalley/mods/7098

### Experience Bars 1.4.6
![[assets/experience-bars-1.png|400]]
![[assets/experience-bars-2.png|600]]
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

### Better Friendship 1.1.3 (bản VH)
- **Công dụng:** Hiện **bong bóng suy nghĩ** trên đầu dân làng — báo món quà họ thích **đang có sẵn trong túi bạn**, và báo khi họ muốn trò chuyện. _(Không phải mod chỉnh hệ số tình cảm.)_
- **Cách dùng:** Mang sẵn vài món quà đi quanh làng; thấy bong bóng trên đầu ai thì tặng/nói chuyện với người đó — khỏi tra bảng sở thích. Bổ trợ cho [[#Lookup Anything 1.55.0|Lookup Anything]]: mod kia phải chủ động tra từng người, mod này tự nhắc khi đi ngang.
- **Phím:** — (bong bóng tự hiện).
- **Cấu hình (`config.json` / GMCM):** `DisplayTalkPrompts` bong bóng "muốn nói chuyện" · `DisplayGenericGiftPrompts` gợi ý quà · `GiftPreference` mức ưa thích tối thiểu (đang để `like`) · `BubbleDisplayRange` tầm hiện bong bóng (đang `12` ô) · `IgnoreMaxedFriendships` bỏ qua người đã đầy tim · `OnlyHighestQuality` chỉ gợi ý món chất lượng cao nhất.
- **Nexus:** https://www.nexusmods.com/stardewvalley/mods/10287

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

### Stardew Dashboard 2.1.5 — ⬆️ _có bản 2.1.6, nên cập nhật_
- **Công dụng:** Bảng thống kê tổng hợp **ngay trong game**: kỹ năng & XP, tình cảm (kèm ảnh chân dung), nhiệm vụ, Trung tâm Cộng Đồng, Bảo tàng, Full Shipment, Polyculture, thời tiết, vật nuôi, đồ thủ công, nông/ngư/mỏ/chiến đấu.
- **Cách dùng:** Bấm `F10` mở bảng; **ghim (pin)** chỉ số bất kỳ lên **Live HUD** để theo dõi liên tục; có ô tìm kiếm. Mod chỉ đọc, không can thiệp save.
- **Phím:** `F10`.
- **Nexus:** https://www.nexusmods.com/stardewvalley/mods/43158

## 4) Kho đồ & rương

### Chests Anywhere 1.30.1
- **Công dụng:** Truy cập mọi rương từ xa.
- **Cách dùng:** Bấm `B` mở kho; đặt tên rương theo nhóm (Cây trồng, Quặng, Cá, Quà) để tìm nhanh.
- **Phím:** `B` (mở mọi rương từ xa) — ⚠️ trùng phím **Mở Lịch** của UI Info Suite 2, nên đổi một trong hai.
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

## 6) Tiện ích (QoL)

### MouseMoveMode 1.4.4
- **Công dụng:** Di chuyển nhân vật bằng chuột.
- **Cách dùng:** Click chuột (nút cấu hình) vào vị trí để nhân vật tự đi tới; tạm tắt khi cần thao tác công cụ chính xác bằng WASD.
- **Phím:** GMCM/`config.json` — gán phím **bật/tắt đi bằng chuột**.
- **Cấu hình:** GMCM/`config.json` → chọn nút chuột dùng để đi, bật/tắt trong nhà/ngoài trời.
- **Nexus:** https://www.nexusmods.com/stardewvalley/mods/2614

### QuickSave 1.5.0 ⚠️ _đổi save serializer_
- **Công dụng:** Lưu game **giữa ngày** (game gốc bắt phải ngủ mới lưu được).
- **Cách dùng:** Bấm `F5` bất kỳ lúc nào → lần sau bấm `F7` vào tiếp **đúng thời điểm đó**. Dùng khi phải tắt máy giữa chừng mà chưa kịp về giường.
- **⚠️ Chỉ có 1 slot:** file `Quicksave` bị **ghi đè** mỗi lần bấm `F5` — không giữ nhiều mốc. Muốn nhiều mốc thì dùng MultiSave bên dưới.
- **Phím:** `F5` lưu · `F7` nạp (đổi trong `config.json`: `SaveButton` / `LoadButton`).
- **Nexus:** https://www.nexusmods.com/stardewvalley/mods/26194

### MultiSaveContinued 1.0.7 ⚠️ _đổi save serializer_
- **Công dụng:** Giữ **nhiều mốc lưu theo ngày trong game** để lùi lại khi lỡ tay.
- **Cách dùng:** Đang bật `AutoSaveDaily` → mỗi ngày trong game tự tạo một bản (thư mục `MultiSave_<slot>_<mùa>_<ngày>` nằm trong thư mục save). Bấm `F8` để tạo mốc thủ công.
- **Cấu hình hiện tại:** `MaxDaysOldToKeep: 7` → chỉ giữ mốc trong vòng **7 ngày game**, cũ hơn tự xóa. Tăng số này nếu muốn lùi xa hơn.
- **Phím:** `F8` (`SaveButton` trong `config.json`).
- **Nexus:** https://www.nexusmods.com/stardewvalley/mods/22953

> ⚠️ **QuickSave và MultiSave cùng đổi save serializer** — xem [[#🛟 An toàn save (quan trọng)|An toàn save]] ở mục 10 trước khi gỡ bất kỳ mod nào trong hai mod này.

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

## 🧰 Công cụ ngoài game

> _Không phải mod SMAPI — **không bỏ vào thư mục `Mods`**._

### Farm Foundry 2.0.0.42 — trình sửa file save

- **Thực chất là:** **Save editor** chạy độc lập ngoài game (Nexus xếp mục "Stardew Valley Save editor"), không phải mod nạp qua SMAPI. Để trong `Mods` thì SMAPI chỉ báo lỗi/bỏ qua.
- **Công dụng:** Mở file save để sửa trực tiếp (tiền, vật phẩm, bố cục/địa hình nông trại…).
- **Cách dùng:** **Thoát game trước**, sao lưu save (`%AppData%\StardewValley\Saves`), rồi mới mở bằng Farm Foundry.
- **⚠️ Rủi ro:** Đây là công cụ đời cũ (từ thời SDV 1.x đầu), **chưa chắc tương thích định dạng save 1.6.15** — sửa sai là hỏng save. Cân nhắc dùng [[#CJB Cheats Menu 1.42.0|CJB Cheats Menu]] ngay trong game cho hầu hết nhu cầu, an toàn hơn nhiều.
- **Nexus:** https://www.nexusmods.com/stardewvalley/mods/127

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

---

## 🛟 An toàn save (quan trọng)

### ⚠️ Hai mod đổi save serializer

SMAPI cảnh báo mỗi lần khởi động:

> _These mods change the save serializer. They may corrupt your save files, or make them unusable if you uninstall these mods._ — **MultiSave - Continued**, **QuickSave**

**Quyết định hiện tại: giữ cả hai** vì hai mod làm hai việc khác nhau (QuickSave = lưu giữa ngày, 1 slot ghi đè · MultiSave = nhiều mốc theo ngày game). Đổi lại phải nhớ:

- **Không gỡ đột ngột.** Gỡ một trong hai có thể làm save **không mở lại được**. Muốn gỡ: sao lưu trước → vào game **ngủ 1 đêm** để game ghi lại save bằng serializer gốc → mới gỡ.
- Đây là 2 mod nghi phạm đầu tiên nếu save hỏng hoặc game không load được.

### 🗄️ Ba lớp lưu — vai trò khác nhau, không thay thế nhau

| Lớp | Mốc giữ được | Đơn vị | Ghi ở đâu |
|---|---|---|---|
| **QuickSave** (`F5`/`F7`) | **1** (ghi đè) | giữa ngày game | `Quicksave` trong thư mục save |
| **MultiSave** (`F8` + tự động) | **7 ngày game** | ngày trong game | `MultiSave_*` trong thư mục save |
| **Save Backup** (tự động) | **10 bản** | **ngày thực** | thư mục game (xem dưới) |

### 💾 Save Backup — mod SMAPI tự cài kèm

Không nằm trong thư mục mod tải về, SMAPI tự nạp (`Mods\SaveBackup`). Cách hoạt động:

- Chạy **1 lần/ngày, ngay lúc khởi động game** — không phải lúc bạn lưu hay ngủ. Mở game 3 lần trong ngày thì chỉ backup ở lần đầu.
- Nén **toàn bộ** thư mục `Saves` thành 1 file `.zip` (gồm cả `Quicksave` lẫn các thư mục `MultiSave_*`).
- Giữ **10 bản gần nhất**, tự xóa bản cũ nhất. Đổi số này bằng cách tạo `Mods\SaveBackup\config.json` với `{ "BackupsToKeep": 30 }`.

**Nơi lưu:** `C:\Program Files (x86)\Steam\steamapps\common\Stardew Valley\save-backups\`

> ⚠️ Nằm **trong thư mục game**, không phải AppData → Steam _Verify integrity of game files_, gỡ/cài lại game, hay chuyển thư viện sang ổ khác đều có thể **xóa sạch backup**. Nên copy định kỳ sang ổ `F:` hoặc cloud.

> 📅 Tên file dùng **ngày UTC**. VN là UTC+7 nên mở game trước 7h sáng sẽ ra tên file **lùi 1 ngày** — không phải thiếu backup.

### 🔧 Khôi phục khi hỏng save

1. **Thoát game.**
2. Giải nén file zip cần dùng trong `save-backups`.
3. Chép đè thư mục save (`Wind_<số>`) vào `%AppData%\StardewValley\Saves\`.
4. Mở game — save quay về trạng thái buổi sáng ngày đó.
