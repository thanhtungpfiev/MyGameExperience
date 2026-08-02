# 🧩 Mods đang dùng — Stardew Valley 1.6.15

> Về [[00 Home]] · Áp dụng theo [[Daily]] · Mẹo chơi [[Mẹo]] · Bản đồ [[Bản đồ khu vực]] · 🛟 [[An toàn save]] · 📦 [[Bản XNB và bản CP]]
>
> _26 mục trong `F:\Games\StardewValley Mods` — **25 mod SMAPI** + **1 công cụ ngoài game** (Farm Foundry), nhóm theo chức năng. Bản `- VH` = Việt hóa → mình dùng bản VH vì đang chơi Việt hóa._
>
> _Mỗi mục mod: dòng đầu là **công dụng**, rồi các dòng **Cách dùng / Phím / Cấu hình / Nexus**. Cảnh báo và chi tiết dài nằm trong **khối callout** — khối có dấu `-` là mặc định gấp lại, bấm để mở. Phím ghi "GMCM" = mặc định trống, tự gán trong Cài đặt → GMCM._

## 📑 Mục lục

1. [[#1) Bộ nền & Việt hóa (bắt buộc, cài trước)|Bộ nền & Việt hóa]] (3)
2. [[#2) Cấu hình mod trong game|Cấu hình trong game]] (2)
3. [[#3) Giao diện & thông tin (UI/Info)|Giao diện & thông tin]] (10)
4. [[#4) Kho đồ & rương|Kho đồ & rương]] (3)
5. [[#5) Tự động hóa & năng suất|Tự động hóa & năng suất]] (2)
6. [[#6) Tiện ích (QoL)|Tiện ích (QoL)]] (3)
7. [[#7) Cheat & Debug|Cheat & Debug]] (1)
8. [[#8) Hình ảnh / nhân vật|Hình ảnh / nhân vật]] (1)
9. [[#9) Ghi chú bản VH & file trùng|Ghi chú bản VH & file trùng]]
10. [[#10) Thứ tự cài & vận hành ổn định (1.6.15)|Thứ tự cài & vận hành ổn định]]
11. [[#🧰 Công cụ ngoài game|Công cụ ngoài game]] (1) — Farm Foundry ❌ _chưa hỗ trợ 1.6_

**Đã tách ra note riêng:** [[An toàn save]] — serializer, 3 lớp lưu, cách khôi phục · [[Bản XNB và bản CP]] — tải bản nào cho mod đồ họa

## 🎹 Bảng phím tắt nhanh

| Phím | Mod | Tác dụng |
|------|-----|----------|
| `F1` | Lookup Anything | Tra cứu vật/dân làng/cây dưới con trỏ (laptop: `Fn`+`F1`) |
| `Shift trái`+`F1` | Lookup Anything | Mở ô tìm kiếm để tra bất kỳ thứ gì |
| `M` | NPC Map Locations | Mở bản đồ (phím gốc game) |
| `\` | NPC Map Locations | Bật/tắt minimap |
| `Space` | NPC Map Locations | Đổi vị trí chú thích (khi đang mở bản đồ) |
| `Tab` | NPC Map Locations | Mở menu tùy chọn mod (khi đang mở bản đồ) |
| `B` | Chests Anywhere | Mở mọi rương từ xa |
| `Ctrl trái`+`F` | Chests Anywhere | Mở ô tìm kiếm vật phẩm trong các rương |
| `C` | UI Info Suite 2 | Mở Lịch (đã đổi từ `B` để hết trùng phím) |
| `Q` | UI Info Suite 2 | Mở Bảng nhiệm vụ (đã đổi từ `H` để hết trùng phím) |
| `F2` | All Chests Menu | Xem tất cả rương trong 1 menu (đang tắt yêu cầu giữ `Shift`) |
| `U` | Automate | Bật/tắt lớp phủ sơ đồ máy–rương |
| `X` | Experience Bars | Ẩn/hiện thanh XP (`Shift`+`X` để di chuyển vị trí) |
| `P` | CJB Cheats Menu | Mở menu cheat |
| `NumPad1` | CJB Cheats Menu | Cây ăn quả / cây gỗ lớn ngay lập tức |
| `NumPad2` | CJB Cheats Menu | Cây trồng chín ngay (bán kính 1 ô) |
| `F5` / `F7` | QuickSave | Lưu nhanh giữa ngày / nạp lại bản lưu nhanh |
| `F8` | MultiSave - Continued | Tạo bản lưu mốc thủ công |
| `F10` | Stardew Dashboard | Mở bảng thống kê tổng hợp |
| `Shift trái` (giữ) | Range Highlight | Hiện **tất cả** vùng tác dụng |
| `J` / `H` / `R` / `O` (giữ) | Range Highlight | Vùng Chòi Junimo / Nhà ong / Vòi phun nước / Bù nhìn |
| `F` | Better Crafting | Đánh dấu ⭐ yêu thích công thức đang rê chuột |
| `Shift trái` (giữ lúc mở) | Better Crafting | Mở **menu chế tạo gốc** thay vì menu mod |
| `F6` | MouseMoveMode | Bật/tắt đi bằng chuột phải |
| `Space` | MouseMoveMode | Ép đi tới vị trí chuột (không tương tác) |
| `Ctrl` + lăn chuột | MouseMoveMode | Phóng to / thu nhỏ khung nhìn |
| `RightAlt`+`Enter` | MouseMoveMode | Đổi toàn màn hình ↔ cửa sổ |
| Nút giữa chuột | MouseMoveMode | Đòn đặc biệt của vũ khí (đã dời khỏi chuột phải) |

> [!phim] Đối chiếu phím gốc của game trước khi gán
> Bảng phím gốc đầy đủ ở [[Mẹo#⌨️ Phím tắt gốc của game (để tránh gán trùng khi cài mod)|Mẹo]].
>
> **Trùng thật, dùng chung một ngữ cảnh:**
>
> | Phím | Đụng nhau ở đâu |
> |---|---|
> | `C` | Phím phụ **"dùng công cụ"** của game ↔ **UI Info Suite 2** mở Lịch |
> | `X` | Phím phụ **"kiểm tra"** của game ↔ **Experience Bars** ẩn/hiện thanh XP |
> | **Chuột phải** | **"Kiểm tra / tương tác"** của game ↔ **MouseMoveMode** dùng để đi — mod xử lý sẵn (bấm gần vẫn tương tác), `F6` tắt tạm là hết |
>
> **Trùng ký tự nhưng khác ngữ cảnh → không đụng nhau:**
>
> | Phím | Ai dùng |
> |---|---|
> | `Shift trái` | Đi bộ chậm (gốc) · Range Highlight (giữ) · Lookup Anything (`Shift`+`F1`) · All Chests Menu (chuyển đồ) · Better Crafting (mở menu gốc) |
> | `Space` | NPC Map Locations (chỉ khi **đang mở bản đồ**) · MouseMoveMode (ép đi) |
> | `F` | Nhật ký nhiệm vụ (gốc) · Better Crafting (chỉ **trong menu chế tạo**) |
> | `Tab` | Đổi hàng thanh công cụ (gốc) · NPC Map Locations (chỉ khi đang mở bản đồ) |
>
> ✅ `H` đã hết trùng: Bảng nhiệm vụ đổi sang `Q`, giờ `H` chỉ còn **Range Highlight** dùng.
>
> **Có cần đổi `C` và `X` không?** Hai phím đó chỉ là **phím phụ** của chuột trái/phải — chơi bằng chuột thì để mod dùng cũng không sao. Hay thao tác bằng bàn phím thì đổi mod sang phím còn trống (`G`, `K`, `L`, `N`, `V`, `Z`) trong GMCM.
>
> `M` là **phím gốc**: NPC Map Locations chỉ mở rộng chức năng bản đồ chứ không chiếm thêm phím.

---

## 1) Bộ nền & Việt hóa (bắt buộc, cài trước)

### SMAPI 4.5.2

Loader để game chạy mod — thiếu nó thì mọi mod vô dụng. **Hầu hết mod Stardew Valley đều cần SMAPI**.

**Cách dùng** — chạy `SMAPI 4.5.2 installer`, rồi luôn mở game bằng `StardewModdingAPI`. Mở file game gốc là chạy bản không mod.

**Nexus** — https://www.nexusmods.com/stardewvalley/mods/2400

> [!info] Cửa sổ console SMAPI
> Mở game xong sẽ có thêm một cửa sổ console chạy song song: đây là chỗ xem mod nào nạp lỗi, mod nào có bản mới, và gõ lệnh (`patch reload`, `help`...). **Gặp lỗi thì đọc cửa sổ này trước tiên.**

> [!success]- Yên tâm khi cài SMAPI
> **Không mất thành tựu** — chạy tốt với thành tựu của cả **GOG lẫn Steam**.
> Chạy được trên **Windows / macOS / Linux**.
> **Gỡ lúc nào cũng được**, quay lại bản game gốc bình thường (chạy lại installer rồi chọn gỡ cài đặt).
> Cộng đồng hỗ trợ đông, dễ hỏi khi kẹt — xem thêm [[An toàn save]] trước khi thêm/bớt mod giữa chừng.

### Content Patcher 2.9.1

Framework nạp **content pack** — thứ sửa **dữ liệu, hình ảnh và bản đồ** của game mà **không cần thay file XNB gốc**. Trong bộ mod này, bản **VH** và **Seasonal Cute Characters** đều là content pack của nó.

**Cách dùng** — để trong `Mods`, không thao tác trong game. Sửa file content pack xong nạp lại bằng `patch reload` ở console SMAPI, khỏi thoát game.

**Nexus** — https://www.nexusmods.com/stardewvalley/mods/1915

> [!warning] Tự nó không làm gì cả
> Phải cài content pack riêng thì mới có tác dụng.

> [!tip]- Vì sao hơn hẳn mod XNB kiểu cũ
> Tự kiểm tra bản cập nhật & tương thích · **cài/gỡ dễ**, chỉ là thêm/xóa thư mục · **tự hỗ trợ đa ngôn ngữ** (lý do bản Việt hóa chạy mượt) · ít xung đột với mod khác · ít vỡ khi game lên phiên bản mới.
>
> Content pack còn sửa được **theo điều kiện động**: đang ở khu nào, thời tiết, ngày/mùa, đang có lễ hội hay sự kiện, đã cưới ai, mức quan hệ với dân làng, có thẻ thành viên Joja hay không...
>
> Chi tiết đầy đủ ở [[Bản XNB và bản CP]] cuối ghi chú.

### Stardew Valley - Vietnamese

![[assets/vietnamese-mod.png|600]]

Việt hóa toàn bộ game (Stardew Valley 1.6). Dịch & mod: **ILoveFish – Kou – Luxanna**.

**Cách dùng** — cài **SMAPI** → **Content Patcher** → giải nén thư mục Việt hóa vào `Mods` → vào **Tùy chọn → Ngôn ngữ** chọn **Tiếng Việt**.

**Phụ thuộc** — Content Patcher (bắt buộc) · GMCM (để chỉnh tùy chọn).

**Cấu hình** — trong **GMCM** có 3 mục: **Phông chữ** (font hội thoại, tên vật phẩm) · **Thời gian** (định dạng 12h/24h, ký hiệu sáng/tối) · **Mod đồ họa khác** (không nạp những hình đã vẽ lại sang tiếng Việt như biển báo, bảng hiệu — bật khi thấy mod ảnh bị bản VH đè mất). Sửa `config.json` bằng tay thì không khuyến nghị.

**Nexus** — https://www.nexusmods.com/stardewvalley/mods/24371

> [!warning] Đổi cấu hình xong phải khởi động lại
> Nhớ bấm **Save** trong GMCM, và **hầu hết thay đổi chỉ có hiệu lực sau khi mở lại game**.

> [!vh] Điểm hay nhất — tiếng Việt là ngôn ngữ riêng
> Không đè lên tiếng Tây Ban Nha như các bản Việt hóa kiểu cũ, nên game chạy ổn định hơn. Mod nào chưa có bản dịch sẽ hiện **tiếng Anh** chứ không lẫn tiếng Tây Ban Nha → đây chính là lý do mấy mod trong bộ này để bản `- VH` thì ra tiếng Việt, còn lại ra tiếng Anh đọc vẫn hiểu.

## 2) Cấu hình mod trong game

### Generic Mod Config Menu (GMCM) 1.16.0

Giao diện chỉnh cấu hình mod **ngay trong game**, khỏi sửa `config.json` bằng tay. Mọi dòng "Cấu hình — GMCM" trong ghi chú này đều đi qua mod này.

**Cách dùng** — 2 đường vào: nút **bánh răng ⚙️** ở **màn hình tiêu đề**, hoặc **cuối menu Tùy chọn** (`Esc`) khi đang chơi.

**Trong menu mỗi mod** — bật/tắt tính năng · đổi số · **gán phím** (bấm ô phím rồi nhấn phím muốn dùng) · **Reset to Default** khi chỉnh lộn.

**Nexus** — https://www.nexusmods.com/stardewvalley/mods/5098

> [!success] Lưu là ăn ngay
> Bấm **Save** trước khi thoát; thay đổi **có hiệu lực liền, không cần khởi động lại game**. Ngoại lệ là [[#Stardew Valley - Vietnamese|bản Việt hóa]] (đổi font, định dạng giờ) phải restart.

> [!warning] Hai giới hạn cần biết
> **Chỉ chạy với mod được viết để hỗ trợ GMCM.** Mod không hỗ trợ vẫn phải sửa `config.json` — như màu thanh [[#Experience Bars 1.4.6|Experience Bars]]. (QuickSave & MultiSave **có** hỗ trợ GMCM, đổi phím `F5`/`F7`/`F8` ngay trong menu được.)
>
> **Vài mod chỉ chỉnh được từ màn hình tiêu đề** (ví dụ [[#Range Highlight 4.2.1|Range Highlight]] phần màu). Vào trong game không thấy mục cần tìm → thoát về tiêu đề rồi mở lại bằng nút bánh răng.

### GMCMOptions 2.1.0

Thêm widget nâng cao cho GMCM, vốn chỉ có bật/tắt, ô số, ô chữ, ô phím: 🎨 **bảng chọn màu** · 🖼️ **bảng chọn ảnh** · ➖ **đường kẻ chia nhóm** · 📄 **đoạn mô tả tự đổi theo lựa chọn**.

**Cách dùng** — để trong `Mods` cạnh GMCM, chạy ngầm, cài rồi thì quên đi. **Không có menu riêng** — widget hiện thẳng trong menu GMCM của mod cần nó.

**Nexus** — https://www.nexusmods.com/stardewvalley/mods/10505

> [!info] Trong bộ này có 2 mod dùng tới — đều để chọn màu
> Thiếu GMCMOptions thì menu [[#Range Highlight 4.2.1|Range Highlight]] và [[#Show Missing Collection Entries 0.2.0|Show Missing Collection Entries]] vẫn mở được nhưng **mất phần chỉnh màu**, muốn đổi phải sửa `config.json`.

## 3) Giao diện & thông tin (UI/Info)

### UI Info Suite 2 (v2.3.7, bản VH)

![[assets/ui-info-suite.png|600]]

Đưa thông tin **vốn đã có trong game** lên thẳng màn hình — thứ bình thường phải tự nhớ hoặc đi tra bảng. Không cho thêm lợi thế nào nên **không có cảm giác cheat**.

**Cách dùng** — icon xếp thành cột cạnh đồng hồ/tiền, **rê chuột** vào icon (hoặc vào vật phẩm) để xem chi tiết.

**Phím** — `C` mở **Lịch** · `Q` mở **Bảng nhiệm vụ**, từ bất cứ đâu (mặc định trống, đã tự gán) · `Esc` **bỏ qua intro** lúc mở game. Lịch đã đổi `B` → `C` để nhường `B` cho Chests Anywhere; Bảng nhiệm vụ đổi `H` → `Q` để nhường `H` cho Range Highlight.

**Cấu hình** — bật/tắt **từng tính năng một** cho gọn màn hình, ở **tab riêng của mod** trong menu Tùy chọn hoặc trong **GMCM** (kèm gán phím).

**Nexus** — https://www.nexusmods.com/stardewvalley/mods/7098

| Nhóm | Thấy được gì |
|---|---|
| 🎂 **Dân làng** | Hôm nay sinh nhật ai, thích quà gì · mức **tim chính xác** (game gốc làm tròn nên không rõ còn thiếu bao nhiêu) |
| 🍀 **Hôm nay / mai** | May mắn hôm nay · **thời tiết ngày mai** · giờ tàu chạy |
| 🍳 **Đừng bỏ lỡ** | Queen of Sauce đang chiếu **công thức mình chưa biết** · Clint đang nâng **công cụ nào, còn mấy ngày** |
| 💰 **Vật phẩm** | Giá bán · thu nhập theo vụ/ngày · còn thiếu **gói Cộng Đồng** · chưa donate **Bảo tàng** · chưa ship lần nào (**Full Shipment**) |
| 🌱 **Cây trồng** | Loại cây + **còn mấy ngày thu hoạch** |
| 🐮 **Nông trại** | Con nào **chưa vuốt** hôm nay · con nào **đã có sữa/lông** để lấy |
| ➕ **Kỹ năng** | Điểm XP vừa nhận nổi lên tại chỗ |

> [!warning] Trùng tính năng với 3 mod chuyên dụng đang cài
> Nên vào cấu hình **tắt 3 nhóm này ở UI Info Suite 2** cho khỏi vẽ đè:
>
> | Tính năng trùng | Mod chuyên dụng | Vì sao giữ mod kia |
> |---|---|---|
> | Vùng Vòi phun nước / Bù nhìn / Nhà ong / Chòi Junimo | [[#Range Highlight 4.2.1\|Range Highlight]] | Có thêm bom (3 vòng), khúc gỗ nấm, đổi màu, phím giữ/toggle |
> | Vị trí dân làng trên bản đồ | [[#NPC Map Locations 3.5.2\|NPC Map Locations]] | Có minimap, lọc NPC, hiện quái/thú nuôi |
> | Thanh XP | [[#Experience Bars 1.4.6\|Experience Bars]] | **Tùy ý:** Experience Bars hiện **cả 5 kỹ năng cùng lúc**; UI Info Suite 2 chỉ hiện thanh liên quan tới việc đang làm → gọn hơn |

### Experience Bars 1.4.6

![[assets/experience-bars-1.png|400]]
![[assets/experience-bars-2.png|600]]

Hiện thanh kinh nghiệm (XP) cho 5 kỹ năng — Trồng trọt, Câu cá, Hái lượm, Khai mỏ, Chiến đấu — thấy ngay còn bao xa mới lên cấp.

**Cách dùng** — thanh nằm cố định ở góc trên–trái, hiện suốt khi đang chơi và tự ẩn lúc mở menu hoặc cắt cảnh. Kỹ năng đã max cấp 10 thì thanh không còn chạy.

**Phím** — `X` ẩn/hiện thanh · `Shift`+`X` **dời thanh tới vị trí con trỏ chuột** (đưa chuột tới chỗ muốn đặt rồi bấm, vị trí lưu ngay vào `config.json`).

**Cấu hình** — GMCM (nút bánh răng ở màn hình tiêu đề) để đổi phím và toạ độ thanh.

**Nexus** — https://www.nexusmods.com/stardewvalley/mods/509

> [!info] Màu thanh không chỉnh được trong GMCM
> Phải sửa `BaseColors` và `SkillColors` trong `config.json`.

### NPC Map Locations 3.5.2

Hiện vị trí dân làng trên bản đồ theo thời gian thực.

**Cách dùng** — `M` mở bản đồ để tìm người tặng quà / kích hoạt sự kiện; bật minimap để theo dõi khi đi lại. Di chuyển minimap bằng cách giữ `Ctrl` + **chuột phải** rồi kéo.

**Phím** — `M` mở bản đồ (phím gốc game) · `\` bật/tắt **minimap** · khi đang mở bản đồ: `Space` đổi vị trí **chú thích**, `Tab` (hoặc `Y` trên tay cầm) mở **menu tùy chọn mod**.

**Cấu hình** — GMCM để bật/tắt minimap, đổi 3 phím trên, lọc NPC (chỉ hiện người đã nói chuyện, cùng khu vực, có nhiệm vụ/sinh nhật), hiện cả quái và thú nuôi.

**Nexus** — https://www.nexusmods.com/stardewvalley/mods/239

### Lookup Anything 1.55.0

Xem chi tiết vật phẩm / dân làng / cây trồng — sở thích quà, thời gian lớn, gói còn thiếu.

**Cách dùng** — đưa con trỏ vào mục tiêu rồi bấm `F1`. Bấm `Shift trái`+`F1` để mở ô **tìm kiếm**, tra thứ không có sẵn trước mặt.

**Phím** — `F1` tra vật dưới con trỏ · `Shift trái`+`F1` tìm kiếm.

**Cấu hình** — GMCM để đổi phím tắt, và bật thêm các **trường dữ liệu nâng cao (data mining)** nếu muốn xem số liệu gốc của game.

**Nexus** — https://www.nexusmods.com/stardewvalley/mods/541 · **Showcase:** https://mods.smapi.io/lookup-anything (nhiều ví dụ minh họa mod hiện được những gì)

> [!info]- Chơi bằng tay cầm, hoặc `F1` không ăn trên laptop
> Không có con trỏ → mod tự chọn **mục tiêu liên quan nhất**: vật/người đứng trước mặt, chính nhân vật khi đang mở bảng Kỹ năng, NPC khi đang mở trang hồ sơ của họ...
>
> 💻 Trên laptop (và macOS) có thể phải bấm `Fn`+`F1` — hoặc đổi hẳn sang phím khác trong GMCM.

### Better Friendship 1.1.3 (bản VH)

![[assets/better-friendship.png|600]]

Hiện **bong bóng suy nghĩ** trên đầu dân làng — báo món quà họ thích **đang có sẵn trong túi bạn**, và báo khi họ muốn trò chuyện. _Không phải mod chỉnh hệ số tình cảm._

**Cách dùng** — mang sẵn vài món quà đi quanh làng, thấy bong bóng trên đầu ai thì tặng hoặc nói chuyện với người đó, khỏi tra bảng sở thích.

**Phím** — không có, bong bóng tự hiện.

**Cấu hình** (`config.json` / GMCM) — `DisplayTalkPrompts` bong bóng "muốn nói chuyện" · `DisplayGenericGiftPrompts` gợi ý quà · `GiftPreference` mức ưa thích tối thiểu (đang để `like`) · `BubbleDisplayRange` tầm hiện bong bóng (đang `12` ô) · `IgnoreMaxedFriendships` bỏ qua người đã đầy tim · `OnlyHighestQuality` chỉ gợi ý món chất lượng cao nhất.

**Nexus** — https://www.nexusmods.com/stardewvalley/mods/10287

> [!tip] Bổ trợ cho Lookup Anything
> [[#Lookup Anything 1.55.0|Lookup Anything]] phải chủ động tra từng người; mod này tự nhắc khi mình đi ngang.

### Range Highlight 4.2.1

![[assets/range-highlight.png|600]]

Tô sáng vùng tác dụng của Vòi phun nước, Bù nhìn, Nhà ong, Chòi Junimo, Khúc gỗ nấm, bom...

**Cách dùng** — vùng **tự hiện** khi **cầm vật đó lên tay**, hoặc khi **rê chuột vào Chòi Junimo**. Muốn xem mà không cần cầm gì thì **giữ phím tắt**. Dùng để xếp Vòi phun nước phủ kín mà không chồng lấn.

**Phím (giữ để hiện)** — `Shift trái` **tất cả** · `J` Chòi Junimo · `H` Nhà ong · `R` Vòi phun nước · `O` Bù nhìn. Đổi được sang kiểu **bấm bật/tắt (toggle)** thay vì phải giữ.

**Cấu hình** — GMCM, cần cả **GMCMOptions** mới chỉnh được màu, và phải chỉnh từ **màn hình tiêu đề**. Không có GMCM thì sửa `config.json` trong thư mục mod.

**Nexus** — https://www.nexusmods.com/stardewvalley/mods/6752

> [!phim] Trùng phím
> `Shift trái` là phím đi bộ chậm của game, đồng thời là phần của `Shift trái`+`F1` (Lookup Anything). Đổi trong GMCM nếu thấy vướng.
>
> ✅ `H` (Nhà ong) giờ đã độc quyền cho mod này — UI Info Suite 2 đã đổi Bảng nhiệm vụ sang `Q`.

> [!bom]+ Bom có tận 3 vòng, không phải 1
> | Vòng | Tác dụng trong vòng đó | Mặc định |
> |---|---|---|
> | **Trong cùng** | Đất thường bị **cày thành đất trồng** | ❌ Tắt (bật được) |
> | **Giữa ("thường")** | Phá **đá** và phần lớn vật phẩm | ✅ Hiện |
> | **Ngoài cùng** | **Phá cây trồng**, làm hỏng nền lát, và **gây sát thương cho bạn** | ✅ Hiện (tắt được) |
>
> Vòng **ngoài cùng** mới là vòng đáng sợ — đứng ra ngoài nó trước khi bom nổ, và đừng để cây trồng nằm trong đó. Rất hợp khi phá đá quanh nông trại mà không muốn cháy luống.
>
> Mod tô vùng cho **từng quả bom đã đặt xuống đất mà chưa nổ**, không chỉ vùng quanh con trỏ lúc đang cầm bom — tắt được trong cấu hình.

> [!tip]- Mấy tùy chọn đáng chỉnh
> `ShowTHINGRange` — **tắt hẳn** việc tô sáng từng loại vật, phòng khi rối mắt hoặc mod khác đã làm việc đó.
>
> Vùng **trong/ngoài của bom**, và có tô vùng bom **đang đếm giờ dưới đất** hay không.
>
> Khi đang **cầm** vòi/bù nhìn/nhà ong, có tô luôn vùng của những cái **đã đặt sẵn** cùng loại không — mặc định **bật** cho Vòi phun nước & Bù nhìn, **tắt** cho Nhà ong và Khúc gỗ nấm.

### Show Missing Collection Entries 0.2.0

![[assets/show-missing-collection.png|600]]

Hiện **icon + tên** của những mục **còn thiếu** trong Bộ sưu tập — game gốc chỉ để ô đen trống nên không biết đang thiếu đúng món nào. Bao trùm cả 4 loại: **vật phẩm** (đã ship / cá / cổ vật / khoáng sản), **công thức** (nấu ăn & chế tạo), **thành tựu**, và **sức mạnh (Powers)** của 1.6. Tác giả **aedenthorn**.

**Cách dùng** — mở Bộ sưu tập (`Esc` → tab Collections) trước khi đi câu / đào mỏ để biết còn thiếu gì. Bổ trợ cho [[#Perfection Stats 1.6.7|Perfection Stats]]: mod kia cho biết **còn bao nhiêu %**, mod này chỉ ra **đúng món nào**.

**Phím** — không có, hiện thẳng trong Bộ sưu tập.

**Cấu hình** — **GMCM**, 9 tùy chọn (bảng dưới). Riêng **màu tint công thức** phải có thêm [[#GMCMOptions 2.1.0|GMCMOptions]] mới hiện bảng chọn màu; không có thì sửa `MissingRecipeTint` trong `config.json`.

**Nexus** — https://www.nexusmods.com/stardewvalley/mods/47916

| Nhóm | Tùy chọn | Mặc định (= đang để) |
|---|---|---|
| 📦 **Vật phẩm** | Icon món còn thiếu | ✅ Bật |
| | Tên món còn thiếu | ✅ Bật |
| | Chi tiết món còn thiếu | ❌ Tắt |
| 🏆 **Thành tựu** | Tên thành tựu còn thiếu | ✅ Bật |
| | Chi tiết thành tựu còn thiếu | ❌ Tắt |
| 🍳 **Công thức** | Màu tint công thức chưa học | 🟥 Đỏ sẫm (R100 G50 B50) |
| ⚡ **Sức mạnh** | Icon sức mạnh còn thiếu | ✅ Bật |
| | Tên sức mạnh còn thiếu | ✅ Bật |
| | Mô tả sức mạnh còn thiếu | ❌ Tắt |

> [!info] Công thức tô màu chứ không hiện tên — có lý do
> Trong tab Nấu ăn / Chế tạo, công thức **đã học nhưng chưa làm lần nào** vốn đã hiện sẵn icon + tên. Nếu mod cũng hiện y hệt cho công thức **chưa học** thì không phân biệt được hai loại — nên phần này dùng **màu tint** thay vì tên.

> [!tip]- Muốn giữ bất ngờ thì tắt phần thành tựu
> Tên & chi tiết thành tựu **chỉ ảnh hưởng những thành tựu ẩn** — đúng mấy cái game cố tình để `???`. Tắt `ShowMissingAchievementNames` nếu không muốn bị lộ trước.
>
> Ba tùy chọn **chi tiết / mô tả** mặc định tắt vì làm tooltip dài thêm; bật khi cần biết món đó là gì, kiếm ở đâu.

### Perfection Stats 1.6.7

![[assets/perfection-stats-2.png|600]]
![[assets/perfection-stats-1.png|600]]

Bảng theo dõi **tiến độ Hoàn hảo (Perfection)** — mỗi hạng mục một thanh %, kèm nút **xem danh sách còn thiếu**. Tác giả **ReichelHz**. Tự nhận diện nội dung của các mod mở rộng lớn (**SVE**, **Ridgeside Village**) nếu có cài.

**Cách dùng** — mở menu game (`Esc`) → **tab hình cúp 🏆 "Perfection Stats"** (tab cuối cùng, sau tab Tùy chọn). Cuộn để xem hết các thanh; bấm **kính lúp 🔍** cạnh thanh nào để bung ra **đúng những món / NPC / quái còn thiếu** của mục đó. Thanh **PERFECTION** ở dưới cùng là tổng.

**Phím** — mặc định **trống** (`OpenMenuKey: "None"`), gán trong GMCM để mở thẳng bảng khỏi phải qua menu.

**Cấu hình** — **GMCM**: `ShowTab` ẩn/hiện tab cúp · phím mở · mục **Colors & Accessibility** đổi 6 màu (đã hoàn thành / còn thiếu / ruột thanh / nền thanh / tiêu đề / chữ). Trong `config.json` còn phần **tổng số từng hạng mục** (vanilla + SVE + Ridgeside).

**Nexus** — https://www.nexusmods.com/stardewvalley/mods/41495

| Nhóm | Thanh trong bảng |
|---|---|
| 🐟 **Sưu tầm** | Fish Species (loài cá) · Museum Items (Bảo tàng) |
| 🍳 **Công thức** | Cooking Recipes (**đã biết**) · Chef Gourmet (**đã nấu**) · Crafting Recipes (đã chế) |
| 🌾 **Nông & hái lượm** | Crops Grown · Forageables · Monoculture (ship đủ số mỗi loại cây) |
| 💜 **Xã hội & việc vặt** | Friendship (**8+ tim**) · Help Wanted Requests |
| ⚔️ **Chiến đấu** | Monster Eradication (Monster Hunter) |
| 🏛️ **Công trình & Stardrop** | Arcane Infrastructure (4 Obelisk + Đồng hồ vàng) · Stardrops (7 nguồn: Gói Pantry, Rương kho báu khi câu, Mỏ tầng 120, Thưởng Bảo tàng, Công thức của Bếp trưởng, Đền Sao Mùa Đông, Krobus) |

> [!tip] Chọn màu cho dễ nhìn — điểm mạnh riêng của mod
> Màu **"đã hoàn thành" vs "còn thiếu"** chỉnh được rời nhau (mặc định xanh lá `G180` / đỏ `R255`), làm riêng cho người **mù màu**. Ruột thanh mặc định là **tím** (`R150 G80 B255`) như trong ảnh. Đổi ngay trong GMCM, không cần GMCMOptions.

> [!info] Phân vai với 2 mod cùng hướng đang cài
> [[#Show Missing Collection Entries 0.2.0|Show Missing Collection Entries]] chỉ ra món thiếu **ngay trong tab Bộ sưu tập gốc**; mod này gom thành **bảng % riêng có nút xem danh sách thiếu**; **Stardew Dashboard** rộng hơn (thời tiết, vật nuôi, nhiệm vụ...) và **ghim được lên HUD**. Ba mod chồng số liệu nhưng không xung đột.

> [!warning]- Cài mod thêm nội dung thì phải sửa tổng số, không thì % sai
> `config.json` giữ **tổng số cứng** cho từng hạng mục: cá `62`, công thức nấu `82`, chế tạo `104`, Bảo tàng `95`, dân làng `25`, cây trồng `26`, hái lượm `20`. Cài mod thêm cá/cây/NPC mà không sửa mấy số này → thanh % lệch (đây là lý do trang Nexus khuyên "nhiều mod thì nên chỉnh config").
>
> Hai mục `SVECategories` và `RidgesideCategories` **chưa dùng tới** — bộ mod hiện tại không có SVE lẫn Ridgeside Village.

> [!vh] Menu ra tiếng Anh
> Mod có 10 bản dịch (de/es/fr/it/ja/ko/pt-BR/ru/zh) nhưng **chưa có tiếng Việt**, nên các thanh giữ nguyên tên tiếng Anh như bảng trên.

### Visible Fish 0.4.2

![[assets/visible-fish-1.png|600]]
![[assets/visible-fish-2.png|600]]

Vẽ **đúng những con đang câu được ngay lúc này** bơi lượn dưới mặt nước — nhìn là biết khu này, mùa này, giờ này có con gì, khỏi tra bảng. Kèm cả **rác** và **điểm có rương kho báu**. Tác giả **shekurika**, chạy được với **khu vực và cá do mod khác thêm**.

**Cách dùng** — liếc mặt nước trước khi quăng cần; đàn cá đổi theo **mùa / giờ / thời tiết** đúng như bảng cá của khu đó. Thấy nhiều rác nổi ở ao nào thì biết chỗ đó câu tốn công.

**Phím** — không có, tự động.

**Cấu hình** — GMCM (bảng dưới). Máy giật thì hạ **Maximum fish** và **Fish Density** trước tiên.

**Nexus** — https://www.nexusmods.com/stardewvalley/mods/8897

| Tùy chọn (GMCM) | Đang để | Tác dụng |
|---|---|---|
| Maximum fish | `500` | Trần số cá vẽ cùng lúc — **hạ xuống nếu máy yếu** |
| Fish Density | `0.2` | Mật độ cá trên mặt nước |
| Show Treasure in the water | ✅ | Hiện chỗ có rương kho báu |
| Enable trash outside Farm | ✅ | Vẽ rác ở hồ/sông/biển ngoài nông trại |
| Enable trash on Farm | ✅ | Vẽ rác ở ao trong nông trại |
| Disable trash on Fishing 10 | ✅ | Câu cá **cấp 10** thì thôi vẽ rác cho đỡ rối |
| Draw shadows under trash / fish | ✅ / ✅ | Bóng đổ dưới vật & cá, nhìn nổi hơn |
| Rotate algae | ❌ | Xoay sprite rong/tảo |
| Filter Eels | ❌ | Lọc bớt lươn |

> [!warning] Chỉ là hình vẽ, **không** đổi cơ chế câu
> Thấy cá không có nghĩa dễ cắn câu hơn — tỉ lệ ra cá vẫn y như game gốc, mod chỉ **hiển thị**.
>
> Mod mượn **sprite bể cá (fish tank)** để vẽ, nên **con nào không có sprite bể cá thì không hiện** dù vẫn câu được. Cá vanilla thì đủ; cá do mod thêm thì tùy mod (Ridgeside Village, More New Fish, SVE có đủ sprite).

> [!tip]- Cá huyền thoại và vật hiếm hiện đúng ô đứng câu — chưa lấy mới hiện
> File `assets\LocationData.json` cắm sẵn vị trí cố định cho mấy thứ chỉ lấy được **một lần**, và chỉ vẽ khi **mình chưa bắt/chưa lấy** — bắt xong là biến mất, nên coi nó như dấu "còn thiếu":
>
> | Khu | Hiện gì |
> |---|---|
> | Bãi biển | **Crimsonfish** (+ Son of Crimsonfish khi đang làm Extended Family) |
> | Thị trấn | **Angler** (+ Ms. Angler) |
> | Núi | **Legend** (+ Legend II) |
> | Rừng (Forest) | **Glacierfish** (+ Glacierfish Jr) · tượng **Krobus Iridium** |
> | Cống ngầm | **Mutant Carp** |
> | Rừng bí mật | **Giỏ treo tường** (Wall Basket) |
> | Đảo Ginger | Bắc: Fossilized Spine, Foliage Print, Squirrel Figurine · Tây: Snake Skull · hang Đông Nam: tượng **Gourmand** |
>
> Rất hợp để đối chiếu với [[#Show Missing Collection Entries 0.2.0|Show Missing Collection Entries]]: mod kia bảo còn thiếu con gì, mod này chỉ luôn nó nằm ở ô nào.

### Stardew Dashboard 2.1.6 — ✅ _đã cài (manifest bên trong vẫn ghi 2.1.5)_

![[assets/stardew-dashboard-1.png|600]]
![[assets/stardew-dashboard-2.png|600]]

Bảng thống kê tổng hợp **ngay trong game** — gom thứ vốn nằm rải rác qua cả chục menu về **một phím**: kỹ năng & XP, tình cảm (kèm chân dung + sở thích quà), nhiệm vụ, Trung tâm Cộng Đồng, Bảo tàng, Full Shipment, Polyculture, thời tiết, vật nuôi, đồ thủ công, nông/ngư/mỏ/chiến đấu. Tác giả **RuthlessTex**. **Chỉ đọc, không đụng vào file save**, an toàn cho co-op.

**Cách dùng** — `F10` mở bảng → gõ vào **ô tìm kiếm** để lọc nhanh, **bấm tiêu đề mục** để gấp/mở, **chuột phải vào dòng bất kỳ để ghim (pin)** dòng đó lên **Live HUD** theo dõi liên tục khi đang làm việc. Bảo tàng / Shipping / Polyculture ghim chung vào **một thẻ** cho gọn màn hình.

**Phím** — `F10` (đổi được trong GMCM).

**Cấu hình** — GMCM 5 mục (ảnh 2): phím mở · hiện nút HUD · hiện lớp phủ Live HUD · hiện sở thích quà NPC trên HUD · **số món mỗi mức thích** (3–7). Riêng **thứ tự sắp xếp danh sách tình cảm** phải sửa `FriendshipSort` trong `config.json`: `Alphabetical` (đang để) · `LowestHearts` · `HighestHearts` · `GiftsThisWeek` · `GiftedTodayFirst`.

**Nexus** — https://www.nexusmods.com/stardewvalley/mods/43158

| Mục trong bảng | Xem được gì |
|---|---|
| ⚡ **Quick Summary** | Ảnh chụp nhanh cả nông trại: ngày + thời tiết, tiền, vợ/chồng, nhiệm vụ, vật nuôi, kỹ năng, tầng mỏ sâu nhất, cá huyền thoại, Bảo tàng, Full Shipment, Polyculture, Óc chó vàng — mỗi thứ một dòng có thanh tiến độ |
| 💜 **Friendships** | Số tim + điểm chính xác, đã tặng quà tuần này chưa, **sinh nhật trong 3 ngày tới**, và **top 3 món Loved / Likes / Disliked / Hated** của từng người |
| 📊 **Skills** | 5 kỹ năng + XP còn thiếu để lên cấp; max cấp 10 hết thì đổi thành **thanh Mastery XP** vàng |
| 🎣 **Fishing** | Thống kê số cá, **checklist cá huyền thoại chưa bắt**, và **bảng tra cá đầy đủ**: khu nào, mùa nào, giờ nào, thời tiết nào |
| 🍳 **Craft Master / Gourmet Chef** | Công thức **chưa chế / chưa nấu bao giờ**, tự nhận cả công thức do mod thêm |
| 📚 **Books of Power** | Sách buff vĩnh viễn **chưa đọc**, đọc xong tự rớt khỏi danh sách |
| 🏺 **Museum / Full Shipment / Polyculture** | Danh sách **còn thiếu** từng món kèm thanh tiến độ |
| 🥚 **Ready to Collect** | Máy, đồ thủ công, cây **đã tới lúc thu**, nhóm theo khu + đếm ngược thời gian; có cả Ao cá và nhiệm vụ tăng đàn |
| 🐄 **Animals & Buildings** | Từng thú cưng (tên, mức thân, tâm trạng), gia súc kèm **nhắc vuốt ve**, **kho cỏ khô + mức tiêu thụ mỗi ngày**, danh sách công trình đang xây |
| 🌱 **Agriculture** | Cây đang trồng, tách riêng Nông trại / Nhà kính / Đảo Ginger |
| 👕 **Equipment** | Mũ, nhẫn, giày, quần áo đang mặc |

> [!tip] Phân vai với UI Info Suite 2 — tác giả nói thẳng
> **UI Info Suite 2 lo "vi mô"** (thông tin tức thời quanh con trỏ, hôm nay ai sinh nhật, cây còn mấy ngày); **Dashboard lo "vĩ mô"** (còn thiếu gì để về đích). Hai mod **tương thích 100%**, cứ để cả hai.

> [!info]- Xuất file & lệnh console
> **Export** — bảng có nút lưu một bản **tóm tắt dạng text** vào `Mods\Stardew Dashboard\exports\` (đang có sẵn `Wind_Spring2_Y1.txt`), tiện để lên kế hoạch ngoài game.
>
> Bộ đếm nội bộ (số cây đã trồng, số quà đã tặng...) nằm ở `data\state.json` — **tách theo từng save**, không nằm trong file save.
>
> Gõ ở console SMAPI: `dashboard_status` khi thấy số liệu lạ · `dashboard_reset confirm` để xóa sạch bộ đếm nội bộ.

> [!vh] Menu ra tiếng Anh
> Mod dịch sẵn 11 thứ tiếng (DE, ES, FR, IT, JA, KO, PT-BR, RU, TR, ZH) nhưng **không có tiếng Việt**.

> [!warning]- Nút HUD đang tắt, và vài lưu ý nhỏ
> `ShowHudButton` trong `config.json` đang để `false` → **không có icon trên màn hình**, mở bảng bằng `F10`. Ảnh GMCM ở trên chụp lúc đang tick thử, chưa bấm **Save**.
>
> Tác giả ghi rõ phần **đồng bộ dữ liệu vật nuôi** vẫn đang tinh chỉnh — lớp phủ đôi khi chậm cập nhật một nhịp.

> [!warning] Đã là 2.1.6 rồi — SMAPI báo "có bản mới" là báo nhầm
> File tải về tên **2.1.6** nhưng bên trong tác giả **quên nâng số phiên bản**: `manifest.json` và `README.txt` vẫn ghi **2.1.5**. Đã đối chiếu **mã băm SHA-256 của `StardewDashboard.dll`** trong `Mods` với file trong `.rar` 2.1.6 → **trùng khít**, tức bản đang chạy chính là bản 2.1.6 mới nhất.
>
> Hệ quả: SMAPI (và `smapi.io/mods`) so `2.1.5` trong manifest với `2.1.6` trên Nexus nên sẽ **nhắc cập nhật hoài** dù không thiếu gì. **Bỏ qua lời nhắc này** cho tới khi Nexus lên 2.1.7.
>
> Muốn hết bị nhắc thì tự sửa dòng `"Version": "2.1.5"` trong `Mods\Stardew Dashboard\manifest.json` thành `2.1.6` — sửa xong sẽ bị ghi đè ở lần cập nhật sau, và **chỉ nên làm khi chắc mình đã cài đúng file 2.1.6**.

## 4) Kho đồ & rương

### Chests Anywhere 1.30.1

![[assets/chests-anywhere-1.png|600]]
![[assets/chests-anywhere-2.png|600]]

Mở **mọi rương, tủ quần áo, tủ lạnh, thùng ship và Chòi Junimo từ bất cứ đâu** — từ trên giường tới tầng mỏ sâu nhất, khỏi chạy về nhà. Tác giả **Pathoschild** (cùng nhà với Content Patcher, Lookup Anything, Automate). Đang cài **bản unlimited** (`Range: Unlimited` — với tay tới mọi rương, mọi nơi).

**Cách dùng** — bấm `B` → hai ô chọn ở trên: **nhóm (category)** và **rương** trong nhóm đó. Bấm **icon bút chì** khi đang mở một rương để **đặt tên · gán nhóm · đổi thứ tự · ẩn rương** khỏi danh sách. Rê chuột vào rương ngoài đời thật cũng hiện tên của nó.

**Phím** — `B` mở/đóng (không còn trùng vì Lịch của UI Info Suite 2 đã đổi sang `C`) · `←` `→` đổi rương · `↑` `↓` đổi nhóm · `Ctrl trái`+`F` **ô tìm kiếm** (trong đó `Tab` xem trước rương) · giữ `Ctrl trái` + lăn chuột đổi rương, giữ `Alt trái` + lăn chuột đổi nhóm.

**Cấu hình** — GMCM (hoặc `config.json`). Xem bảng dưới.

**Nexus** — https://www.nexusmods.com/stardewvalley/mods/518

| Tùy chọn | Đang để | Ý nghĩa |
|---|---|---|
| `Range` | `Unlimited` | Tầm với tới rương — xem callout "chế độ cân bằng" |
| `EnableShippingBin` | ✅ | Mở **thùng ship** như một cái rương |
| `ReopenLastChest` | ✅ | Lần sau bấm `B` mở lại đúng rương vừa dùng |
| `ShowHoverTooltips` | ✅ | Rê chuột vào rương ngoài map thì hiện tên |
| `AddOrganizePlayerInventoryButton` | ✅ | Thêm nút sắp xếp túi đồ vào menu rương |
| `EnableSprinklerAttachments` | ❌ | Cho gắn vật vào Vòi phun nước qua menu (tính năng phụ, đang tắt) |
| `DisabledInLocations` | trống | Danh sách khu **cấm** dùng mod, ví dụ `["UndergroundMine"]` để không xài được trong mỏ |
| `EditChest` / `SortItems` | chưa gán | Hai phím phụ dùng khi đang mở rương, gán thêm trong GMCM nếu hay dùng |

> [!tip] Thùng ship dùng như rương — cứu đồ lỡ tay
> Bỏ nhầm món quý vào thùng ship? Mở thùng ship qua menu này và **lấy ra lại**, miễn là **chưa qua đêm**. Đây là công dụng đáng giá nhất mà nhiều người không biết.

> [!info]- Đặt tên & nhóm rương — bộ nhóm đang dùng
> Ảnh trên là các nhóm đã tự tạo: **Main · Crafting · Food (crops / fruit & animal / prepared / forage / sea) · Fridge · Sea items · Seeds · Gifts · Gifts (flowers) · Storage (farm) · Storage (items)**.
>
> Nhóm mặc định là **tên khu vực** đặt rương; đổi thành nhóm theo công dụng như trên thì tìm nhanh hơn nhiều. Rương phụ ít dùng thì **ẩn** đi cho danh sách gọn.

> [!info]- Chế độ cân bằng (balanced) nếu thấy quá lợi
> `Range` đổi được sang: `CurrentWorldArea` (chỉ rương **cùng vùng đang đứng** — đây là "bản balanced" trên trang Nexus) · `CurrentLocation` (chỉ rương **cùng màn hình**) · `None`. Hoặc giữ Unlimited nhưng thêm `"UndergroundMine"` vào `DisabledInLocations` để **cấm xài trong mỏ** — chặn kiểu vét quặng vô hạn mà vẫn tiện lúc ở nhà.

> [!warning] Xung đột & giới hạn đã biết
> **Joys of Efficiency** có thể lỗi khi mở thùng ship — bộ mod này **không cài** mod đó nên không sao.
>
> **Co-op:** mod chạy riêng cho từng máy (chỉ ai cài mới có). Người chơi phụ (farmhand) chỉ thấy rương ở **khu đã đồng bộ** — chủ yếu là nông trại, nhà kho trong trại và khu đang đứng; đây là giới hạn của game chứ không phải lỗi mod.

> [!vh] Menu ra tiếng Anh
> Mod dịch sẵn 14 thứ tiếng ngay trong bản gốc (kể cả Thái, Ba Lan, Ukraina) nhưng **chưa có tiếng Việt**.

### All Chests Menu 0.4.2

![[assets/all-chests-menu-2.png|600]]
![[assets/all-chests-menu-1.png|600]]

Bày **ruột của tất cả rương lên cùng một màn hình**, kèm túi đồ nhân vật ở khung dưới — để **dồn, đổi chỗ, lọc, đổi tên** hàng loạt thay vì mở từng rương một. Tác giả **aedenthorn**, phần cập nhật cho 1.6 do **mouahrara** làm.

**Cách dùng** — bấm `F2`. Rương chưa đặt tên hiện dạng **`Farm 70,11`** (khu + tọa độ ô), đặt tên rồi thì thành **`Fish (Farm 72,11)`**. Gõ vào ô **Filter** để lọc theo **tên rương và khu vực**.

**Thao tác trong menu**

- Giữ `Shift trái` + **chuột trái vào món** → chuyển món đó về túi.
- **Bấm tiêu đề rương** để nhấc khung rương lên, bấm sang rương khác để **đổi chỗ hai khung**. Đang nhấc mà giữ `Shift trái` → **đổ toàn bộ đồ** sang rương đích; giữ thêm `Ctrl trái` → **chỉ đổ những loại rương đích đã có sẵn**.
- **6 nút bên phải mỗi rương**: `Open` mở kiểu menu thường · `Organize` sắp xếp · `Put` đẩy cả túi vào rương · `Take` lấy cả rương về túi · `Rename` đổi tên · `Target` bật đích, sau đó bấm món ở bất kỳ đâu là món đó bay thẳng vào rương này.
- **Khung dưới**: `Organize` sắp túi · **`Store Similar`** — quét mọi rương, món nào đã có sẵn ở rương nào thì tự cất về đúng rương đó · `Trash` xóa vĩnh viễn.
- **8 nút Sort By** đổi thứ tự hiện rương: `LA`/`LD` theo khu · `NA`/`ND` theo tên · `CA`/`CD` theo sức chứa · `IA`/`ID` theo số ô đã dùng (A = tăng, D = giảm).

**Phím** — `F2` mở menu · `Shift trái` = Mod Key · `Ctrl trái` = Mod Key 2 · nút **Back** trên tay cầm để nhảy giữa lưới rương và khung dưới.

**Cấu hình** — GMCM hoặc `config.json`. Xem bảng.

**Nexus** — https://www.nexusmods.com/stardewvalley/mods/14494

| Tùy chọn | Đang để | Ý nghĩa |
|---|---|---|
| `ModToOpen` | ❌ | **Tắt** nên chỉ cần `F2`, không phải giữ `Shift` |
| `LimitToCurrentLocation` | ❌ | Bật thì chỉ hiện rương ở khu đang đứng |
| `IncludeFridge` / `IncludeMiniFridges` | ✅ / ✅ | Gom cả tủ lạnh và tủ lạnh mini |
| `IncludeShippingBin` / `IncludeMiniShippingBins` | ✅ / ✅ | Gom cả thùng ship |
| `UnrestrictedShippingBin` | ❌ | Bật thì lấy lại được **mọi món đã bỏ vào thùng ship**, không chỉ món cuối cùng |
| `IncludeJunimoChests` / `IncludeAutoGrabbers` | ✅ / ✅ | Gom rương Junimo và máy tự nhặt |
| `FilterItems` / `Category` / `Description` | ❌ | Bật để ô Filter tìm **theo vật phẩm bên trong** (tên / nhóm / mô tả), không chỉ theo tên rương |
| `SecondarySortingPriority` | `Y` | Cùng hạng thì xếp tiếp theo tọa độ `Y` (đổi được sang `X`) |

> [!tip] Hai nút đáng dùng nhất sau một ngày cày
> **`Store Similar`** ở khung dưới — về nhà, mở menu, bấm một cái là cả túi tự chui về đúng rương đã có sẵn loại đó. Món nào chưa có nhà thì ở lại túi để mình xếp tay.
>
> **`Target`** — bật ở rương muốn dồn vào, rồi bấm lần lượt các món nằm rải rác ở rương khác; khỏi kéo thả qua lại.

> [!info] Tên rương dùng chung với Chests Anywhere
> Mod cố tình ghi tên vào **cùng chỗ dữ liệu** (`modData`) như [[#Chests Anywhere 1.30.1|Chests Anywhere]] → đặt tên ở mod nào cũng hiện ở mod kia, không phải làm hai lần.
>
> Phân vai: **Chests Anywhere** để với tay lấy **một** rương từ xa lúc đang ở ngoài; **All Chests Menu** để nhìn **toàn bộ** cùng lúc mà dọn kho.

> [!phim] Ghi chú phím — không cần `Shift` nữa
> Trang Nexus ghi mặc định là giữ `Shift trái` + `F2`, nhưng `config.json` hiện tại để `ModToOpen: false` → **bấm mỗi `F2` là mở**. `Shift`/`Ctrl` giờ chỉ dùng cho các thao tác chuyển đồ bên trong menu.

> [!warning]- Vài điểm bản 0.4.2 khác với mô tả trên Nexus
> Mục "đổi **số hàng** của mọi rương" trên trang Nexus **không còn khóa tương ứng** trong `config.json` bản này — coi như không dùng được. (Kể cả có thì cũng nên tránh: menu rương gốc của game chỉ vẽ **3 hàng**, tăng lên là phải phụ thuộc hẳn vào menu của mod mới thấy phần dư.)
>
> Ô Filter mặc định **chỉ lọc theo tên rương / khu vực**; muốn tìm "rương nào đang chứa Vàng" thì phải bật `FilterItems`.

> [!vh] Menu ra tiếng Anh
> Mod chỉ có sẵn tiếng Pháp và tiếng Nga ngoài tiếng Anh — **không có tiếng Việt**.

### Carry Chests 1.3.0

![[assets/carry-chests-1.png|600]]
![[assets/carry-chests-2.png|600]]
![[assets/carry-chests-3.png|600]]

Nhấc **cả rương lẫn đồ bên trong** mang đi chỗ khác, khỏi phải dỡ ra rồi xếp lại. Tác giả **LeFauxMatt**. Cần game **1.6.14** trở lên; GMCM là phụ thuộc **tùy chọn** (thiếu vẫn chạy, chỉ là khó chỉnh).

**Cách dùng** — **tay không**, quay mặt vào rương rồi **bấm nút hành động** là nhấc lên (ảnh 1). Đang cầm rương mà **chuột phải** thì **mở xem/lấy đồ ngay trong rương đang cầm** (ảnh 2). Đặt lại như đặt vật phẩm thường.

**Phím** — không có phím mặc định. Gán được **một phím bật/tắt nhanh cả mod** (`Toggle Enabled`) trong GMCM, tiện khi đang xây nông trại mà không muốn lỡ tay nhấc rương.

**Cấu hình** — GMCM. Mod **chưa có `config.json`** trong thư mục → đang chạy **toàn bộ mặc định**; mở GMCM bấm **Save** một lần là file được tạo.

**Nexus** — https://www.nexusmods.com/stardewvalley/mods/30321

| Tùy chọn (GMCM) | Tác dụng |
|---|---|
| `Enabled` · `Toggle Enabled` | Bật/tắt cả mod, và phím để bật/tắt nhanh |
| `Maximum Reach` | Đứng xa **mấy ô** vẫn nhấc được rương |
| `Carry Chest Limit` | Cầm tối đa mấy rương cùng lúc |
| `Slowness Limit` · `Slowness Amount` | Cầm quá **mấy** rương thì bị chậm, và **chậm mức nào** |
| `Open Held Chests` | Cho chuột phải mở rương đang cầm |
| `Grab Empty as Item` | Rương **rỗng** nhấc lên thành vật phẩm thường để **xếp chồng** trong túi |
| `Override Tool` | Dùng công cụ lên rương thành **nhấc rương** thay vì đập |
| `Swap Chests` | Cầm rương "dùng" lên một rương đã đặt → **gộp đồ và tráo chỗ** hai rương |

> [!warning] Cầm nhiều quá thì bị "Overburdened"
> Vượt `Slowness Limit` là dính hiệu ứng **Overburdened −1 Speed** (ảnh 3), đi chậm hẳn. Không phải lỗi — đây là cách mod giữ cân bằng. Đặt bớt rương xuống là hết.

> [!save] Gỡ mod thì phải đặt hết rương xuống trước
> Tác giả nói rõ: **thêm mod lúc nào cũng an toàn**, nhưng trước khi **gỡ** phải đặt xuống mọi rương đang cầm — không thì **đồ trong đó có thể mất**. Kiểm tra túi đồ trước khi xóa thư mục mod.

> [!tip]- Có sẵn bản sao lưu rương đã cầm — lệnh console cứu hộ
> Mod tự giữ **backup ruột của các rương từng cầm**. Gõ ở console SMAPI:
>
> - `carry_chests help` — liệt kê lệnh
> - `carry_chests backups` — mở menu xem các **bản sao lưu** của rương đã cầm (phải đang trong game mới chạy được)
>
> Đây là phao cứu sinh nếu lỡ mất một rương đầy đồ.

> [!vh]- Có file `vi.json` nhưng chưa dịch
> Thư mục `i18n` có sẵn `vi.json`, tuy nhiên **nội dung y hệt tiếng Anh** — người dịch mới tạo file chứ chưa dịch chữ nào, nên trong game vẫn ra tiếng Anh.

## 5) Tự động hóa & năng suất

### Automate 2.6.1

![[assets/automate-1.png|300]]
![[assets/automate-2.png|400]]
![[assets/automate-3.png|450]]

Đặt rương **cạnh máy** thì máy **tự rút nguyên liệu từ rương và đẩy thành phẩm trở lại rương** — khỏi chạy từng cái để đút vào lấy ra. Tác giả **Pathoschild** (cùng nhà với [[#Content Patcher 2.9.1|Content Patcher]], [[#Lookup Anything 1.55.0|Lookup Anything]], [[#Chests Anywhere 1.30.1|Chests Anywhere]]).

**Cách dùng** — đặt 1 rương **chạm** cụm máy (Thùng ủ / Hũ ngâm / Lò luyện / Bể pha lê...), **mọi hướng kể cả chéo góc**. Đổ nguyên liệu vào rương → máy tự chạy → thành phẩm tự về rương.

**Phím** — `U` bật/tắt **lớp phủ sơ đồ** máy–rương (nhìn được cụm nào đang nối với cụm nào), đổi được trong GMCM.

**Cấu hình** — GMCM: tắt thùng ship · bật **đường lát làm dây nối** · bật/tắt và chỉnh **từng loại máy** riêng.

**Nexus** — https://www.nexusmods.com/stardewvalley/mods/1063 · **Sơ đồ mẫu:** https://smapi.io/automate (nhiều bố cục máy–rương dựng sẵn)

> [!warning] Thùng ship **bán đồ tự động** — bẫy dễ dính nhất
> Mặc định thùng ship cũng là một "rương" của mod → rương nào chạm thùng ship là **đồ bị bán khi qua đêm**. Hoặc dời rương ra xa thùng ship, hoặc vào GMCM → **Shipping Bin settings** tắt hẳn.

> [!info] Nguyên liệu của một công thức phải nằm **chung một rương**
> Nối nhiều rương vào cùng cụm máy thì máy vẫn **lấy đầu vào từ tất cả các rương**, nhưng **một mẻ** phải đủ nguyên liệu trong **cùng một rương** — than ở rương A, quặng ở rương B thì Lò luyện đứng im.
>
> Thành phẩm đẩy ra theo thứ tự: rương đã bật **"prefer this chest for output"** ([[#Chests Anywhere 1.30.1|Chests Anywhere]] → icon bút chì) → rương **đã có sẵn món cùng loại** → rương bất kỳ.

> [!success] Vẫn ăn đủ XP và thành tựu
> Máy chạy tự động cho **y hệt XP, thành tựu và vật phẩm** như tự tay thao tác — không bị "lách" mất phần thưởng.

> [!tip]- Cụm máy (machine group) & đường lát làm dây nối
> Cứ mỗi rương/máy **chạm** một cái khác là chúng gộp thành **một cụm** — nối bao nhiêu máy cũng được, bấm `U` để nhìn ranh giới cụm.
>
> Bật **Enabled connectors** trong GMCM để **đường lát (wooden path...) dẫn tín hiệu** thay cho việc phải xếp máy dính sát nhau → rải đường nối một cụm máy trải khắp nông trại vẫn được.
>
> **Rương Junimo** đưa cả cụm lên phạm vi **toàn cầu**: mọi máy/rương nối với rương Junimo (dù ở khu khác) chung một cụm. Ví dụ Chòi Junimo trên trại thu hoạch → Thùng ủ trong nhà kho lên men → Hũ ủ dưới hầm ủ lâu → thùng ship gom thành phẩm.

> [!tip]- Danh sách thứ tự động được — có cả thứ không ngờ tới
> | Nhóm | Gồm những gì |
> |---|---|
> | 🏭 **Máy chế biến** | Đe · Máy tự nhặt · Máy làm mồi · Nhà ong · Máy nghiền xương · Hũ ủ (cask) · Lò than · Máy ép phô mai · Máy pha cà phê · **Lồng cua** · Bể pha lê · Máy tháo dỡ · Máy sấy khô · Máy xông khói cá · **Lò luyện & Lò luyện lớn** (nhớ nạp than) · **Máy nghiền địa chất** (cũng cần than) · Máng cỏ khô · Lồng ấp trứng · Thùng ủ (keg) · Cột thu lôi · Khung dệt · Máy làm mayonnaise · Thùng ship mini · Hộp nấm · Khúc gỗ nấm · Máy ép dầu · Hũ ngâm · Máy tái chế · Máy làm hạt giống · Máy ép trứng slime · Lồng ấp slime · Máy làm soda · Pin mặt trời · Tượng Vô Tận / Hoàn Hảo / Chân Hoàn Hảo · Máy băm gỗ · Thùng trùn (cả loại deluxe) |
> | 🏚️ **Công trình** | Ao cá (**chỉ lấy ra**) · Chòi Junimo · Cối xay · Kho cỏ khô |
> | 🌳 **Thứ vốn không phải máy** | Bụi cây (mâm xôi đen, dâu rừng, **bụi trà**) · Cây ăn quả · **Thùng rác** · Thùng ship (chỉnh được) · Vòi hứng nhựa (tapper) · Cây thường |
> | 📦 **Vật chứa** | Rương (kể cả rương lớn & rương đá) · Tủ lạnh nhà/cabin · **Hopper** (y như rương nhưng **chỉ đẩy ra**) · Rương Junimo · Tủ lạnh mini · Thùng ship mini |
>
> Còn hỗ trợ **máy do mod khác thêm** nếu mod đó viết theo định dạng máy chuẩn của bản 1.6+.
>
> 🦀 **Lồng cua** — ảnh 3 là bố cục ở bãi biển: Thùng trùn tự sinh mồi → rương đẩy mồi vào lồng cua → lồng cua trả hải sản về rương → Máy tái chế xử lý luôn đống rác câu được.

> [!info]- Machine pipelines — dành cho lúc muốn nghịch sâu
> Bản mới có **machine pipelines**: chuyển đồ giữa **nhiều cụm máy** khác nhau, đặt **luật lọc vật phẩm**, xử lý **tràn rương**. Đọc mục _machine pipelines_ trong readme trên trang Nexus khi cần.

### Better Crafting 2.18.0 (bản VH)

![[assets/better-crafting-1.png|600]]
![[assets/better-crafting-2.png|500]]

Thay **cả menu Chế tạo lẫn menu Nấu ăn** bằng giao diện mới: **cột phân loại** bên trái, **đánh dấu yêu thích**, **chế hàng loạt** một phát, và **Bàn thợ (Workbench) với xa hơn** — không chỉ những rương dính sát bên. Tác giả **KhloeLeclair**.

**Cách dùng** — cứ mở menu chế tạo/nấu ăn như thường, mod tự thay giao diện. **Chuột phải vào công thức** → menu **Bulk Crafting**: gõ số lượng muốn làm, mod hiện luôn tốn bao nhiêu nguyên liệu. Ảnh 1 là menu Bàn thợ với cột phân loại bên trái.

**Phím** — `F` (rê chuột vào công thức) **đánh dấu ⭐ yêu thích** — tay cầm bấm **Back** · giữ `Shift trái` **trong lúc mở** menu chế tạo → ra **menu gốc của game**, không bị thay. Cả hai đổi được.

**Cấu hình** — nút **bánh răng ngay trong menu chế tạo** (`Show Settings Button`), hoặc **GMCM**. Bảng dưới là các mục trong ảnh 2.

**Nexus** — https://www.nexusmods.com/stardewvalley/mods/11115

| Nhóm | Tùy chọn | Đang để | Ý nghĩa |
|---|---|---|---|
| ⚙️ **General** | `Show Settings Button` | ✅ | Hiện nút mở cài đặt ngay trong menu chế tạo |
| | `Disable Key` | `LeftShift` | Giữ phím này lúc mở menu → dùng **menu gốc** |
| | `Replace Crafting Menu` | ✅ | Thay menu **Chế tạo** |
| | `Replace Cooking Menu` | ✅ | Thay menu **Nấu ăn** (tắt riêng được) |
| | `Enable Categories` | ✅ | Bật **cột phân loại** bên trái |
| 🔨 **Crafting** | `Force Uniform Sizes` | ❌ | Ép mọi ô về **cùng một cỡ** cho lưới đều tăm tắp |
| | `Sort Big Craftables Last` | ❌ | Đẩy đồ **cỡ lớn** (lò, thùng ủ...) xuống cuối danh sách |
| 🍳 **Cooking** | `Use Seasoning` | `Never` | Có tự dùng **Gia vị Qi** để nâng phẩm chất món ăn không |
| | `Hide Unknown Recipes` | ❌ | Ẩn hẳn công thức **chưa học** |
| ⭐ **Quality** | `Enable Quality Limit` | ✅ | Giới hạn phẩm chất nguyên liệu được đem ra dùng |
| | `Use Low Quality First` | ✅ | **Xài đồ phẩm chất thấp trước**, để dành đồ vàng/iridi đem bán hoặc tặng |

> [!tip] Ba thứ đáng dùng nhất
> **Bulk Crafting** (chuột phải) — làm 50 Vòi phun nước một lần thay vì bấm 50 cái, lại thấy trước đủ nguyên liệu hay không.
>
> **⭐ Yêu thích** (`F`) — công thức hay dùng có **ngôi sao bạc** và nổi lên đầu, khỏi cuộn tìm.
>
> **`Use Low Quality First`** — đang bật, nên chế tạo tự ăn đồ thường trước; đồ **vàng / iridi** ở lại trong rương để bán hoặc tặng quà.

> [!phim] `Shift trái` lại là phím bận
> `Shift trái` đang gánh: đi bộ chậm (game gốc) · [[#Range Highlight 4.2.1|Range Highlight]] hiện tất cả vùng · [[#All Chests Menu 0.4.2|All Chests Menu]] chuyển đồ · và giờ là **Disable Key** của mod này. Không đụng nhau vì khác ngữ cảnh, nhưng nhớ: **đang giữ `Shift` mà mở bàn chế tạo là ra menu gốc**, không phải mod hỏng.

> [!info]- Phân loại (categories) — tự sắp cho vừa cách chơi
> Cột trái có sẵn nhóm mặc định; bấm **nút chỉnh** bên phải để **tự tạo nhóm**, kéo công thức vào. **Chuột phải vào một món** khi đang chỉnh → lấy món đó làm **icon của nhóm**.
>
> Từ 1.3.0 nhóm còn nhận **luật tự động** (công thức nào khớp thì tự vào nhóm), và từ 2.5.0 thì **trộn được** danh sách chọn tay với luật tự động.
>
> Trong save co-op, phân loại là **riêng của từng người**, không đè lên nhau.

> [!success] Bàn thợ (Workbench) — phần cải thiện âm thầm mà đáng giá
> Bàn thợ gốc chỉ lấy nguyên liệu từ **rương dính sát ngay bên**; mod nới rộng phạm vi này ra **nhiều rương hơn** — dựng bàn thợ giữa dãy rương kho là chế được mọi thứ mà khỏi bốc nguyên liệu ra.
>
> Chơi co-op: bàn thợ gốc **khóa rương** khiến người khác không mở được trong lúc mình đang chế; mod bỏ hẳn cái khóa đó.

> [!warning] Công thức do mod khác thêm có thể không nghe phần Quality
> Chính mod ghi rõ trong menu: công thức đến từ nguồn khác (**SpaceCore**...) **có thể bỏ qua** hai tùy chọn `Enable Quality Limit` / `Use Low Quality First` do giới hạn API. Bộ mod hiện tại không cài SpaceCore nên chưa gặp.

> [!tip]- Không thích kiểu chia tab thì tắt đi
> Tắt `Enable Categories` là menu trở về **y hệt giao diện gốc**, nhưng vẫn giữ được chế hàng loạt, yêu thích và phần bàn thợ mở rộng.

## 6) Tiện ích (QoL)

### MouseMoveMode 1.4.4

Đi bằng **chuột phải** thay cho `WASD`, có **tìm đường** tự né chướng ngại vật. Kèm hai thứ game gốc không có: **`Ctrl` + lăn chuột để phóng to/thu nhỏ** và **`RightAlt`+`Enter` đổi toàn màn hình / cửa sổ**. Tác giả **nghiango1**.

**Cách dùng** — **chuột phải** vào chỗ muốn tới (hoặc **giữ** chuột phải để đi liên tục, thả là dừng). Bấm vào chỗ **xa** thì nhân vật tự tìm đường tới nơi rồi **mới thực hiện thao tác** lên vật được trỏ — bấm vào cây là đi tới rồi chặt, khỏi canh khoảng cách. Có **dấu chỉ điểm đến** hiện tại vị trí chuột.

**Phím** — `F6` bật/tắt chế độ đi bằng chuột phải · `Space` **ép đi** (`ForceMoveButton`) · `Ctrl` + lăn chuột **zoom** · `RightAlt`+`Enter` **toàn màn hình / cửa sổ** · giữ `Shift` **khi đang cưỡi ngựa** → chuột phải chỉ để đi, không làm gì khác.

**Cấu hình** — **GMCM** (mod có hỗ trợ đầy đủ: bật/tắt, ô số, gán phím) hoặc sửa `config.json`. Bảng dưới là **giá trị đang chạy thật** trong `Mods\MouseMoveMode\config.json`.

**Nexus** — https://www.nexusmods.com/stardewvalley/mods/2614 · **GitHub:** https://github.com/nghiango1/RightClickMoveMode

| Khóa | Đang để | Ý nghĩa |
|---|---|---|
| `RightClickMoveModeDefault` | `true` | **Tự bật** chế độ đi bằng chuột ngay khi vào game |
| `RightClickMoveModeToggleButton` | `F6` | Phím bật/tắt mod giữa chừng |
| `ForceMoveButton` | `Space` | Phím **ép đi** tới vị trí chuột, kể cả khi đang trỏ vào vật |
| `HoldingMoveOnly` | `false` | `false` = **bấm một cái cũng đi**; đổi `true` thì **chỉ giữ chuột mới đi** |
| `HoldTickCount` | `15` | Giữ chuột bao nhiêu tick thì tính là "đang giữ" (hạ xuống nếu thấy nhạy chậm) |
| `EnablePathFinding` | `true` | Bật **tìm đường** vòng qua chướng ngại vật |
| `PathFindLimit` | `500` | Trần số ô được dò khi tìm đường — xa quá thì mod chịu, không đi |
| `ShowMousePositionHint` | `true` | Hiện **dấu chỉ điểm đến** dưới con trỏ |
| `WeaponsSpecticalInteractionType` | `2` | Cách xử lý **đòn đặc biệt của vũ khí** — xem callout |
| `ExtendedModeDefault` | `true` | Bật cụm mở rộng: **`Ctrl`+lăn zoom** và **`RightAlt`+`Enter`**. Để `false` là tắt cả hai |
| `FullScreenKeybindShortcut` | `RightAlt + Enter` | Phím đổi toàn màn hình (đổi sang `F11` được) |
| `MouseWhellingZoomStep` | `0.25` | Mỗi nấc lăn chuột zoom bao nhiêu — tăng cho nhanh, giảm cho mượt |
| `MouseWhellingMinZoom` / `MaxZoom` | `0.75` / `2.0` | Trần dưới/trên của mức zoom |

> [!phim] Chuột phải vốn là phím "Kiểm tra / tương tác" của game
> Đây là mod đụng vào thao tác cơ bản nhất, nên nếu thấy lạ tay thì **`F6` tắt tạm** là game trở lại y như cũ ngay.
>
> Bấm **gần** thì vẫn tương tác bình thường; bấm **xa** mới thành "đi tới rồi tương tác". Muốn **chỉ đi chứ đừng làm gì** thì dùng `Space` (`ForceMoveButton`).
>
> `F6` **không trùng** với phím gốc hay mod nào ([[Mẹo#⌨️ Phím tắt gốc của game (để tránh gán trùng khi cài mod)|bảng phím gốc]]), lại nằm gọn giữa `F5`/`F7` của **QuickSave** và `F8` của **MultiSave** — cả cụm `F` giờ đều có việc.
>
> ⚠️ `Space` thì **có trùng**: [[#NPC Map Locations 3.5.2|NPC Map Locations]] cũng dùng `Space` để đổi vị trí chú thích — nhưng **chỉ khi đang mở bản đồ**, lúc đó nhân vật không đi được, nên thực tế không đụng nhau.

> [!warning]- Đòn đặc biệt của vũ khí — vì sao đang để mode `2`
> Chuột phải khi cầm kiếm vốn là **đỡ đòn / đòn đặc biệt**, đúng nút mà mod dùng để đi → phải chọn cách xử lý:
>
> | Mode | Cách xử lý |
> |---|---|
> | `0` | Bỏ hẳn phần xử lý riêng — chuột phải chỉ ra đòn đặc biệt **trong bán kính 2 ô** quanh nhân vật |
> | `1` | Giữ y như game gốc, nhưng ra đòn đặc biệt sẽ **cắt ngang** việc đang đi |
> | **`2`** ✅ | **Đang dùng.** Chuột phải **không** ra đòn nữa; thay vào đó bấm **nút giữa / nút phụ X1**, hoặc **chuột trái vào chính nhân vật** |
> | `3` | Như `2` nhưng bỏ luôn cách chuột-trái-vào-nhân-vật, **chỉ còn nút giữa / X1** |
>
> Nói ngắn: **đang đánh nhau trong mỏ mà muốn đỡ đòn thì bấm nút giữa chuột**, đừng bấm chuột phải.

> [!tip] `Ctrl` + lăn chuột để zoom — tiện nhất lúc quy hoạch nông trại
> Kéo ra `0.75` để nhìn bao quát cả trại khi xếp Vòi phun nước (rất hợp dùng chung với [[#Range Highlight 4.2.1|Range Highlight]] và [[Quy hoạch nông trại]]), phóng vào `2.0` khi cần đặt chính xác từng ô.

> [!info]- Vài chỗ trang Nexus ghi khác với bản 1.4.4 đang cài
> Trang Nexus viết phím bật/tắt là `G`, nhưng `config.json` bản này để **`F6`** — lấy file trên máy làm chuẩn.
>
> Bản này **có thêm** `ForceMoveButton` (Nexus chưa liệt kê) và **bỏ** khóa `WeaponsSpecticalInteraction` kiểu bật/tắt, chỉ còn `WeaponsSpecticalInteractionType`.
>
> `HoldingMoveOnly` trên Nexus mặc định `true`, máy này đang `false`.
>
> 🐛 Tên khóa `MouseWhelling…` là **tác giả viết sai chính tả** (đúng phải là _Wheeling_) — cứ giữ nguyên, sửa lại là mod không đọc được.

> [!save] Tác giả nói thẳng là mod chưa "xong"
> Phần mô tả trên Nexus ghi mod **gần ổn định chứ chưa hoàn chỉnh**. Không đụng vào file save nên không có rủi ro hỏng save, chỉ là thỉnh thoảng có thể tìm đường hụt hoặc kẹt góc — `F6` tắt rồi đi bằng `WASD` là qua.

### QuickSave 1.5.0 ⚠️ _đổi save serializer_

![[assets/quicksave.png|600]]

Lưu game **giữa ngày** kiểu RPG — game gốc bắt phải **ngủ** mới lưu được, tức là lỡ phải tắt máy lúc 2 giờ chiều là mất cả ngày cày. Tác giả **DeLiXx**.

**Cách dùng** — bấm `F5` bất kỳ lúc nào, hiện dòng _"Your progress has been saved."_ là xong. Lần sau bấm `F7` để vào tiếp **đúng thời điểm đó** — đúng giờ, đúng chỗ đang đứng, đúng số năng lượng còn lại.

**Phím** — `F5` lưu · `F7` nạp. Đổi trong **GMCM** (mục `Save Button` / `Load Button`) hoặc `config.json`.

**Nexus** — https://www.nexusmods.com/stardewvalley/mods/26194

> [!warning] Chỉ có 1 slot
> File `Quicksave` bị **ghi đè** mỗi lần bấm `F5`, không giữ nhiều mốc. Muốn nhiều mốc thì dùng MultiSave bên dưới.

> [!info] Lưu ở đâu
> `Quicksave` và `Quicksave_SaveGameInfo` nằm **bên trong thư mục save**, cạnh file save chính:
>
> `%AppData%\StardewValley\Saves\Wind_444616523\`
>
> Xóa hai file này thì mất bản quicksave, file save chính không sao. Chúng cũng được [[An toàn save#💾 Save Backup — mod SMAPI tự cài kèm|Save Backup]] nén chung vào bản `.zip` hằng ngày.

> [!warning] Có lúc bấm `F5` không ăn — mod báo _"You cannot save right now"_
> Game đang ở trạng thái không cho lưu (cắt cảnh, sự kiện, menu đặc biệt...). Không phải mod hỏng, qua đoạn đó rồi bấm lại.

> [!tip] Dùng như "nút thử lại", không chỉ để tắt máy giữa chừng
> Bấm `F5` **trước** khi làm việc dễ hỏng ăn — xuống tầng mỏ mới, đào Skull Cavern, mở rương kho báu, hay trước khi tặng món quà chưa chắc người ta thích. Sai thì `F7` làm lại.
>
> Đây cũng là lý do giữ song song với MultiSave: **QuickSave lo trong ngày, MultiSave lo giữa các ngày**.

> [!info]- 15 công tắc tương thích mod khác — bộ này không dùng tới cái nào
> `config.json` còn 15 khóa `…CompatibilityEnabled` (Fishing Trawler, Custom Companions, Combat Drone, DeepWoods, SpaceCore, Stardio, Little NPCs, Love of Cooking, Junimatic, Custom Spouse Patio, Deluxe Journal, Weapons on Display, Star Control, Bee Paths) — đều đang `true` nhưng **không cài mod nào trong số đó**, nên bật hay tắt cũng không khác gì.
>
> Manifest ghi thêm 3 phụ thuộc **tùy chọn** (DLX.Bundles, DLX.PIF, Farm Type Manager) — cũng không cài, mod vẫn chạy bình thường.
>
> Mod mở sẵn `IQuickSaveAPI` cho mod khác móc vào lúc lưu/nạp — chỉ có ý nghĩa nếu sau này cài thêm mod dùng API này.

> [!save] Đây là 1 trong 2 mod đổi save serializer
> Đừng gỡ đột ngột — đọc [[An toàn save]] trước khi bỏ mod này.

### MultiSaveContinued 1.0.7 ⚠️ _đổi save serializer_

![[assets/multisave-1.png|380]]
![[assets/multisave-3.png|450]]
![[assets/multisave-4.png|450]]
![[assets/multisave-2.png|400]]

Giữ **nhiều mốc lưu theo ngày trong game** để lùi lại khi lỡ tay, **chọn mốc ngay trong menu Load** của game. Mod gốc là **Multi Save** của **aedenthorn**; ông này bỏ làm mod Stardew nên **recon88** nhận về nuôi tiếp — bản `- Continued` này chính là bản còn được cập nhật.

**Cách dùng** — mốc tự tạo sẵn mỗi đêm, không phải làm gì. Khi cần lùi: ở **màn hình Load**, bấm **icon bút lông & lọ mực** ở góc slot save (ảnh 2, chỗ badge _"3 Saves"_) → hiện danh sách các mốc (ảnh 3) → bấm để **đổi sang mốc đó**, hoặc bấm **❌ đỏ** để xóa mốc.

**Phím** — `F8` tạo mốc thủ công cho ngày hiện tại.

**Cấu hình** — **GMCM** hoặc `config.json`. Bảng dưới là giá trị đang chạy thật.

**Nexus** — https://www.nexusmods.com/stardewvalley/mods/22953

| Khóa | Đang để | Ý nghĩa |
|---|---|---|
| `EnableMod` | `true` | Bật/tắt cả mod |
| `AutoSaveDaily` | `true` | **Tự lưu mỗi cuối ngày** — nguồn mốc chính đang dùng |
| `AutoSaveOnDayOfWeek` | `0` | Lưu vào **thứ mấy trong tuần** (1–7), `0` = tắt |
| `AutoSaveOnDayOfMonth` | `0` | Lưu vào **ngày mấy trong tháng** (1–28), `0` = tắt |
| `MaxDaysOldToKeep` | `7` | Chỉ giữ mốc trong vòng **7 ngày game**, sáng hôm sau tự dọn bản cũ hơn. Tăng nếu muốn lùi xa hơn |
| `SaveButton` | `F8` | Phím tạo mốc thủ công |

> [!warning] Mốc lưu là **đầu ngày**, không phải lúc bạn bấm `F8`
> Stardew về bản chất **chỉ lưu được ở thời điểm bắt đầu một ngày** — nên mọi mốc của mod đều là trạng thái **sáng sớm hôm đó**, mọi việc đã làm trong ngày **không** nằm trong mốc.
>
> Đây là chỗ khác nhau căn bản với **QuickSave**:
>
> | | Lưu được gì | Số mốc |
> |---|---|---|
> | **QuickSave** `F5` | **Đúng khoảnh khắc** đang chơi (giờ, vị trí, năng lượng) | 1, ghi đè |
> | **MultiSave** `F8` | **Sáng sớm** của ngày hiện tại | Nhiều, giữ 7 ngày |
>
> Lỡ tay giữa ngày → `F7` (QuickSave). Muốn chơi lại nguyên một ngày → chọn mốc MultiSave.

> [!info] Đổi mốc thì mốc cũ không mất
> Chuyển sang một mốc khác thì mốc đó thành **bản mặc định** hiện ở danh sách Load chính, còn bản mặc định cũ **lùi vào danh sách mốc phụ** — đổi qua đổi lại thoải mái, không bản nào bị nuốt.

> [!info]- Tên thư mục mốc, và vì sao có thể trùng ngày
> Mốc nằm trong thư mục con của save, dạng `MultiSave_<năm>_<mùa>_<ngày>` — máy này đang có `MultiSave_1_spring_1` trong `%AppData%\StardewValley\Saves\Wind_444616523\`.
>
> Trùng tên thì mod thêm đuôi `_1`, `_2`… → **có nhiều mốc cùng một ngày trong game** là chuyện bình thường: khi bạn lùi về mốc cũ rồi chơi tiếp mà chưa xóa các mốc ngày sau. Ảnh 3 là ví dụ, Day 1/2/3 kèm **ngày giờ thực** để phân biệt.

> [!save] Có sẵn lưới an toàn `_tmp` khi đổi mốc
> Trước mỗi lần chuyển mốc, mod **sao lưu nguyên thư mục save** thành `<tên save>_tmp` trong `%AppData%\StardewValley\Saves\`. Đổi mốc mà hỏng thì thay thư mục save hỏng bằng thư mục `_tmp` này.

> [!warning]- Ảnh GMCM là ảnh trên Nexus, không phải cấu hình máy này
> Ảnh 4 chụp `Save Button = F5`, `Day of Week = 7`, `Day of Month = 28`. Máy này đang để **`F8`**, và hai mục tuần/tháng đều **`0` (tắt)** vì đã có lưu hằng ngày rồi. Lấy bảng ở trên làm chuẩn.

> [!save] QuickSave và MultiSave cùng đổi save serializer
> Đọc [[An toàn save]] trước khi gỡ bất kỳ mod nào trong hai mod này.
>
> Riêng mod này còn một lưu ý khi **nâng cấp từ bản cũ** (kể cả bản của aedenthorn): tác giả yêu cầu **dọn sạch thư mục `save-backups`** trong thư mục game **trước khi** nâng cấp. Bản aedenthorn cũ vẫn tương thích — mod tự nhận diện và sửa lại cấu trúc thư mục nếu cần.

## 7) Cheat & Debug

### CJB Cheats Menu 1.42.0

![[assets/cjb-cheats-menu.png|600]]

Menu cheat đầy đủ trong game, chia **9 tab**: người chơi & công cụ, nông trại & câu cá, kỹ năng, thời tiết, mối quan hệ, dịch chuyển, thời gian, mở rộng, điều khiển. Tác giả **CJBok** và **Pathoschild**.

**Cách dùng** — bấm `P` khi **không có menu nào đang mở**. Bật/tắt từng ô, có hiệu lực ngay. Vào tab **Điều khiển** để đổi phím — khỏi sửa `config.json`.

**Phím** — `P` mở menu · `NumPad1` **cây ăn quả / cây gỗ lớn ngay** · `NumPad2` **cây trồng chín ngay** (bán kính `1` ô quanh chỗ đứng). Hai phím NumPad dùng **thẳng ngoài game**, không cần mở menu.

**Cấu hình** — tab **Điều khiển** trong menu, hoặc `config.json`. Mod **không** dùng GMCM.

**Nexus** — https://www.nexusmods.com/stardewvalley/mods/4

> [!warning] Đang bật 6 cheat — hầu hết là cheat câu cá
> `config.json` hiện tại (mọi thứ không liệt kê ở đây đều **tắt**):
>
> | Cheat | Tác dụng |
> |---|---|
> | `InfiniteStamina` | **Vô hạn năng lượng** — không bao giờ kiệt sức, không phải ăn |
> | `InstantBite` | Cá **cắn câu ngay** khi vừa quăng |
> | `InstantCatch` | **Câu được luôn**, bỏ qua minigame kéo cá |
> | `ThrowBobberMax` | Luôn quăng cần **xa tối đa**, khỏi giữ nút canh lực |
> | `AlwaysTreasure` | **Lần nào cũng có rương kho báu** |
> | `DurableTackles` | **Phao/mồi không hao**, dùng mãi |
>
> 5 trong 6 cái là câu cá — tức là **phần câu cá đang được tự động gần như hoàn toàn**. Đáng biết khi nhìn số liệu ở [[#Perfection Stats 1.6.7|Perfection Stats]] hay [[#Visible Fish 0.4.2|Visible Fish]]: cá đủ loại vẫn vào bộ sưu tập bình thường, nhưng không còn là thành tích tay nghề.
>
> Muốn lấy lại cảm giác câu cá thật thì tắt `InstantCatch` trước tiên, giữ `ThrowBobberMax` cũng đã đỡ mỏi tay rồi.

> [!vh] Menu ra **tiếng Việt** — một trong số ít mod có bản dịch thật
> Thư mục `i18n` có `vi.json` **dịch đầy đủ** (không phải file rỗng như [[#Carry Chests 1.3.0|Carry Chests]]): "Vô hạn năng lượng", "Cắn câu ngay lập tức", "1 đập bể đá & chặt cây", "Hàng rào không bị hỏng"... Còn sót vài dòng mới của bản 1.6 chưa dịch (Green Rain, Auto-Water Pet Bowls) nên chỗ đó vẫn ra tiếng Anh.

> [!info]- 9 tab có những gì
> | Tab | Nội dung chính |
> |---|---|
> | **Người chơi & công cụ** | Vô hạn năng lượng/HP · giảm hồi chiêu · tăng tốc chạy · 1 phát chết · may mắn tối đa · vô hạn nước bình tưới · 1 đập bể đá & chặt cây · thu hoạch bằng lưỡi hái |
> | **Nông trại & Câu cá** | Tự tưới · tự cho ăn · tự vuốt ve (vật nuôi & thú cưng) · hàng rào không hỏng · xây nhanh · vô hạn cỏ khô · **cụm cheat câu cá** ở bảng trên |
> | **Kỹ năng** | Chỉnh thẳng cấp & nghề của 5 kỹ năng (**không** hỗ trợ kỹ năng do mod khác thêm) |
> | **Thời tiết** | Đặt **thời tiết ngày mai** (chỉ ngày mai, không đổi được hôm nay) |
> | **Mối quan hệ** | Chỉnh tim từng người · **tặng quà mọi lúc** (bỏ giới hạn 2 quà/tuần) · tình bạn không tụt |
> | **Dịch chuyển** | Nhảy thẳng tới mọi khu; thêm/ẩn điểm đến qua `AddWarps` / `HideWarps` |
> | **Thời gian** | Đóng băng thời gian (mọi nơi / trong nhà / trong hang) · chỉnh giờ · đổi ngày |
> | **Mở rộng** | Tiền, vật phẩm, mở khoá công thức, hoàn thành Trung tâm Cộng Đồng... |
> | **Điều khiển** | Gán lại toàn bộ phím, kể cả phím tay cầm |

> [!tip] `NumPad2` + Vòi phun nước — cặp đôi lợi hại
> `GrowRadius: 1` nghĩa là bấm `NumPad2` làm chín cây trong ô **3×3** quanh chỗ đứng. Tăng số này trong `config.json` nếu muốn quét cả luống một lần.

> [!info]- Chơi mạng (co-op) — cheat nào ảnh hưởng người khác
> Mod chạy **cục bộ**, chỉ ai cài mới có, và người khác **thường không thấy** mình đang cheat.
>
> **Ảnh hưởng cả server:** đổi ngày/giờ, thời tiết ngày mai, hoàn thành Trung tâm Cộng Đồng, xây nhanh, máy chạy nhanh, thu hoạch bằng lưỡi hái, thêm tiền (nếu chung ví), hàng rào bền, tự cho ăn, tự vuốt ve, vô hạn cỏ khô.
>
> **Ảnh hưởng ai đứng cùng khu:** 1 phát chết, 1 đập bể.
>
> Farmhand **không** đổi được thời gian. Tác giả ghi **không có xung đột mod nào đã biết**.

> [!warning] Ảnh trên là ảnh Nexus, không phải máy này
> Ảnh chụp `Infinite Health`, `Increased Movement Speed`, `One Hit Kill`, `Max Daily Luck`, `One Hit Break` đang **bật** — máy này **tắt hết** mấy cái đó. Lấy bảng "Đang bật 6 cheat" ở trên làm chuẩn.

> [!success] Mã nguồn mở, có bằng chứng dựng bản
> Toàn bộ mã công khai, và **mỗi bản phát hành kèm một attestation** — bản ghi không giả mạo được, chứng minh file tải về đúng là dựng từ mã nguồn công khai chứ không bị nhét thêm gì. Hiếm mod nào làm tới mức này.

## 8) Hình ảnh / nhân vật

### Seasonal Cute Characters 6.1.2

Tên trên Nexus là **Seasonal Outfits - Slightly Cuter Aesthetic**. Vẽ lại **toàn bộ sprite lẫn chân dung** của dân làng theo phong cách dễ thương hơn, và cho **mỗi người một bộ đồ riêng theo từng mùa** — cộng thêm đồ **ấm khi ra ngoài trời mùa đông**, đồ **Vũ hội Hoa** và đồ **Đêm Linh Hồn**. Vợ/chồng còn có đồ riêng cho mọi lễ hội khác. Tác giả **Poltergeister**.

**Cách dùng** — để trong `Mods` cùng [[#Content Patcher 2.9.1|Content Patcher]], không thao tác gì trong game. Ý tưởng lấy cảm hứng từ hệ thống quần áo động của **Longevity** và **Seasonal Villager Outfits**.

**Phím** — không có, đây là content pack.

**Phụ thuộc** — Content Patcher (bắt buộc) · GMCM (rất nên có, xem callout).

**Nexus** — https://www.nexusmods.com/stardewvalley/mods/5450

> [!info] Cấu hình nên làm qua GMCM
> Pack này có tới **~70 tuỳ chọn**. Từ bản 6.1.0, **mỗi mục trong GMCM đều có dòng mô tả** ghi rõ tác dụng, các lựa chọn và giá trị mặc định — dễ hơn hẳn so với sửa `config.json` (dễ gõ sai chuỗi là hỏng).

> [!success]- Đang bật gần như toàn bộ — 45+ nhân vật đều dùng bản dễ thương
> Tất cả `SlightlyCuter…` đều `true`, gồm cả **NPC của bản 1.6** (Bear, Birdie, Fizz, Mr. Qi, Professor Snail) lẫn phần **chân dung vợ/chồng**, **biểu tượng cảm xúc (emoji)** và **hình gói Trung tâm Cộng Đồng**.
>
> | Mục | Đang để | Ý nghĩa |
> |---|---|---|
> | `WinterClothing` | `IndoorAndOutdoor` | Dân làng **mặc ấm khi ra ngoài** mùa đông. Chơi mạng mà lỗi hình mùa đông thì đổi sang `IndoorOnly` / `OutdoorOnly` |
> | `BeachOutfitsEnabled` | ✅ | Đồ đi biển |
> | `FestivalOutfitsEnabled` | ✅ | Đồ Vũ hội Hoa & Đêm Linh Hồn |
> | `ExtraOutfitsEnabled` | ✅ | Các bộ phụ thêm |
> | `HideNoses` | ❌ | Giấu mũi dân làng |
> | `SlightlyCuterBundles` / `Emojis` / `SpousePortraits` | ✅ | Vẽ lại gói Cộng Đồng, emoji, chân dung vợ/chồng |

> [!tip]- Mấy chi tiết nhỏ riêng cho từng người
> | Mục | Đang để | Nghĩa là |
> |---|---|---|
> | `GilSeasonalChairs` | ✅ | Ghế của Gil đổi theo mùa |
> | `HarveyFacialHair` | ✅ | Harvey **giữ ria** |
> | `MaruGlasses` | ❌ | Maru **không** đeo kính |
> | `WizardSeasonalHair` | ✅ | Tóc Pháp sư đổi theo mùa |
> | `PennyFreckles` | `OnlySummer` | Penny **chỉ có tàn nhang vào mùa hè** |
> | `LeoIslandClothes` | `Seasonal` | Đồ của Leo trên Đảo cũng đổi theo mùa |

> [!warning] Nhân vật của mình đang **không** đổi đồ theo mùa
> `SeasonalFarmerAppearance` đang để **`false`** → cả cụm `ShirtSpring` / `ShoesSpring` / `ShirtSummer`… (đang có sẵn giá trị `Warm` / `Cold` / `Vanilla`) **hoàn toàn không có tác dụng**. Muốn nhân vật cũng thay đồ theo mùa thì bật mục này lên trước, rồi mới chỉnh áo/giày từng mùa.
>
> `LocalClimateOverride` cũng đang `false` — bật lên thì đồ đổi theo **khí hậu nơi đang đứng** (ví dụ ra Đảo Gừng giữa mùa đông vẫn mặc đồ hè).
>
> Hiện `SlightlyCuterFarmer` = ✅ (nhân vật vẫn được vẽ lại cho hợp phong cách), `HideFarmerNose` = ❌, `FemaleShoeStyle` = `Flat`.

> [!warning]- Cài thêm mod đổi hình thì phải tắt bớt ở đây
> Mod nào cũng sửa **chân dung / sprite của cùng một NPC** thì sẽ đè nhau — tắt đúng `SlightlyCuter<Tên>` của người đó.
>
> Riêng mod sửa **hình nhân vật của mình** (Get Glam, Soft Farmer...) thì phải tắt `SlightlyCuterFarmer`.
>
> Manifest có sẵn 6 phụ thuộc **tùy chọn** (Rustic Countryside, Vanilla Interiors, Starblue Valley, SVE, Cute Sprites) — **không cài cái nào**, nên phần tương thích đó đang nằm im.

---

## 9) Ghi chú bản VH & file trùng

**Bản `- VH` (.rar)** = Việt hóa → **dùng bản này**. Bản gốc `.zip` cùng version chỉ giữ backup, **không cài cả hai cùng lúc** cho một mod vì trùng UniqueID sẽ lỗi. Áp dụng cho Better Crafting, Better Friendship, UI Info Suite 2.

**SMAPI** — giữ `installer` để cài; file `.zip` chỉ là backup.

## 10) Thứ tự cài & vận hành ổn định (1.6.15)

1. **SMAPI** → **Content Patcher / GMCM / GMCMOptions** → **bản VH** → **UI/Info** → **kho & tự động hóa** → **tiện ích/cheat/hình ảnh**.
2. Mỗi mod chỉ giữ **1 bản** trong `Mods`, ưu tiên bản VH.
3. Thêm mod mới → vào game ngủ 1 đêm để chắc không lỗi sự kiện/máy móc.
4. Khi game hoặc mod cập nhật, kiểm tra tương thích tại `smapi.io/mods`.
5. Lỗi → đọc log SMAPI để biết mod nào thiếu phụ thuộc hoặc sai version.
6. Mod đồ họa cho tải 2 bản thì **luôn lấy bản CP**, không lấy bản XNB — [[Bản XNB và bản CP]].

---

## 🧰 Công cụ ngoài game

> [!caution] Không phải mod SMAPI
> **Không bỏ vào thư mục `Mods`.**

### Farm Foundry 2.0.0.42 — trình sửa file save ❌ _chưa hỗ trợ 1.6_

![[assets/farm-foundry-2.png|420]]
![[assets/farm-foundry-1.png|420]]

**Save editor** chạy độc lập ngoài game — tên đầy đủ **Farm Foundry (SDVSE — Stardew Valley Save Editor)**, không phải mod nạp qua SMAPI. Để trong `Mods` thì SMAPI chỉ báo lỗi rồi bỏ qua.

**Công dụng** — mở file save sửa trực tiếp: **vật phẩm trong túi** · **rương / tủ lạnh / mọi vật chứa** · **bố cục & địa hình nông trại** (di chuyển, xóa vật thể) · **độ vui của vật nuôi** · đổi **mèo ↔ chó**. Ảnh 2 là tab nông trại: tên trại, cấp nhà, mùa/ngày/năm, giống thú cưng, cỏ khô, Óc chó vàng.

**Cách dùng** — **thoát game trước** → sao lưu `%AppData%\StardewValley\Saves` → mở công cụ → **Load** → sửa → **Save**. Màn hình chính (ảnh 1) có sẵn **Backup Manager** và **Reload Save**.

**Nexus** — https://www.nexusmods.com/stardewvalley/mods/127

> [!error] Tác giả ghi rõ: **chưa có bản cho 1.6**
> Nguyên văn trên trang Nexus: _"Note: 1.6 version is planned, please give us some time"_. Game của bạn đang chạy **1.6.15** → công cụ này **chưa đọc đúng định dạng save hiện tại**. Đây là rủi ro hỏng save thật, không phải cảnh báo cho có.
>
> File tải về (`Farm Foundry-127-2-0-0-42-…zip`) là bản **tháng 4/2024**, ngay sau khi 1.6 vừa ra — chưa kịp cập nhật. Hai ảnh trên còn là bản `2.0.0.9` cũ hơn nữa; trường mới nhất nó biết là **Óc chó vàng**, tính năng của **1.5**.
>
> ✅ **Dùng [[#CJB Cheats Menu 1.42.0|CJB Cheats Menu]] thay thế** cho gần như mọi nhu cầu — tiền, vật phẩm, kỹ năng, tình cảm, thời tiết, ngày giờ, dịch chuyển. Chạy trong game, đúng chuẩn 1.6.15, **không đụng vào file save**.

> [!success] Nếu vẫn dùng — nó có tự sao lưu
> Công cụ **tự tạo backup trước mỗi lần sửa**, kèm **Backup Manager** để khôi phục (nút ở màn hình chính, ảnh 1). Hỏng thì mở trình quản lý đó, hoặc vào thẳng thư mục backup lấy file ra.
>
> Vẫn nên tự chép thêm một bản ra chỗ khác, cộng với 3 lớp lưu sẵn có ở [[An toàn save]].

> [!info]- Image pack — không bắt buộc, và chưa cài
> Thiếu image pack thì công cụ **vẫn chạy nhưng không hiện hình vật phẩm**, chỉ có chữ. Cài bằng cách giải nén rồi chạy installer, hoặc chép thủ công thư mục `STCM` vào `%AppData%\StardewValley\`.
>
> Máy này **chưa có** thư mục `STCM` — trong `%AppData%\StardewValley\` hiện chỉ có `Saves`, `ErrorLogs`, `default_options`, `startup_preferences`.

> [!info]- Đọc được cả save bản Console
> Tác giả ghi công cụ đọc được save từ **mọi bản console, kể cả Switch**. Chỉ có ý nghĩa nếu sau này bạn muốn xem save từ máy khác — bản PC vẫn vướng vấn đề 1.6 ở trên.
