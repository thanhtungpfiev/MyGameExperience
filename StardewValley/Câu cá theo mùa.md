# 🎣 Câu cá theo mùa

> Về [[00 Home]] · Nhật ký [[Daily]] · Mẹo câu cá [[Mẹo#🎣 Câu cá (Fishing)|Mẹo — Câu cá]] · Bản đồ [[Bản đồ khu vực]]
>
> _Note này trả lời **"mùa này câu được cá gì, ở đâu, lúc nào — và mình còn thiếu con nào"**. Cách câu, cần câu, thư Willy thì xem [[Mẹo#🎣 Câu cá (Fishing)|Mẹo]]._
>
> _Tên cá theo **bản Việt hóa đang cài** (tên tiếng Anh trong ngoặc để tra wiki). Giờ, thời tiết, cấp tối thiểu và chỗ câu lấy thẳng từ file game 1.6.15 (`Data/Fish`, `Data/Locations`); tầng mỏ theo wiki. Cột ✅ đối chiếu với save **Wind** (mục `fishCaught`) ngày **Xuân 17, Năm 1** — cập nhật lại khi câu thêm._

**Chú thích:** 🧩 = cần cho gói Trung tâm Cộng đồng · 🌧️ = chỉ ra khi mưa · ☀️ = chỉ ra khi nắng · "cả ngày" = 06:00–02:00.

---

## 🌸 Xuân

**Đã câu 17 / 21 loại** câu được mùa Xuân ở những chỗ đã vào được (không tính rong, tảo, sứa và mục 🔒).

### 🌊 Biển (Bãi biển)

| ✅ | Cá | Giờ | Thời tiết |
|---|---|---|---|
| [x] | Cá cơm (Anchovy) | cả ngày | bất kỳ |
| [x] | Cá mòi (Sardine) 🧩 | 06:00–19:00 | bất kỳ |
| [x] | Cá trích (Herring) | cả ngày | bất kỳ |
| [x] | Cá bơn (Flounder) | 06:00–20:00 | bất kỳ |
| [x] | Cá bơn lưỡi ngựa (Halibut) | 06:00–11:00 · 19:00–02:00 | bất kỳ |
| [x] | Lươn (Eel) 🧩 | 16:00–02:00 | 🌧️ |

### 🏞️ Sông (Thị trấn + Rừng Cindersap)

| ✅ | Cá | Giờ | Thời tiết |
|---|---|---|---|
| [x] | Cá thái dương (Sunfish) 🧩 | 06:00–19:00 | ☀️ |
| [x] | Cá trê (Catfish) 🧩 | 06:00–24:00 | 🌧️ |
| [x] | Cá trích dày mình (Shad) 🧩 | 09:00–02:00 | 🌧️ |
| [x] | Cá vược miệng nhỏ (Smallmouth Bass) | cả ngày | bất kỳ |
| [x] | Cá bống (Chub) | cả ngày | bất kỳ |
| [x] | Cá vền (Bream) 🧩 | 18:00–02:00 | bất kỳ |
| [ ] | **Cá bống tượng (Goby)** — _mới từ 1.6, khác Cá bống (Chub) ở trên_ | 08:00–18:00 | bất kỳ — câu ở **thác nước Rừng Cindersap** |

### ⛰️ Hồ trên Núi

| ✅ | Cá | Giờ | Thời tiết |
|---|---|---|---|
| [x] | Cá vược miệng rộng (Largemouth Bass) 🧩 | 06:00–19:00 | bất kỳ |
| [x] | Cá chép (Carp) 🧩 | cả ngày | bất kỳ |
| [x] | Cá đầu bò (Bullhead) 🧩 | cả ngày | bất kỳ |
| [ ] | **Cá huyền thoại (Legend)** | 06:00–20:00 | 🌧️ · **chỉ Xuân** · cần **cấp Câu cá 10** · quăng xa bờ **≥ 4 ô** · 1 con/save |

> [!info] Cá huyền thoại với cấp 7
> Game kiểm tra cấp Câu cá **gồm cả buff đồ ăn**, nên cấp 7 + món **+3 Câu cá** (vd Dish o' the Sea) là đủ 10. Còn thiếu một ngày mưa trước Xuân 28 — xem TV dự báo mỗi sáng. Độ khó 110 (khó nhất game); nếu `InstantCatch` ([[Mẹo#🎣 Câu cá (Fishing)|Mẹo]]) còn bật thì độ khó không còn là vấn đề.

### ⛏️ Hầm mỏ (mọi mùa)

Bạn đã xuống tới **tầng 70** → tầng 20 và 60 đều câu được.

| ✅ | Cá | Nơi | Cấp tối thiểu |
|---|---|---|---|
| [x] | Cá ma (Ghostfish) 🧩 | ao tầng 20 · 60 | — |
| [x] | Cá đá (Stonefish) | ao tầng 20 | 3 |
| [ ] | **Cá băng (Ice Pip)** | ao tầng 60 | 5 |
| [ ] | Lươn dung nham (Lava Eel) | ao tầng 100 — _chưa tới_ | 7 |
| [ ] | Thạch Hang Động (Cave Jelly) — _sứa, mới từ 1.6_ | ao tầng 20 · 60 (rất hiếm) · dung nham tầng 100 (dễ hơn) | — |

> [!info] Vì sao cá mỏ khó ra — không phải do minigame, mà do **tỉ lệ cắn câu**
> Soi code game 1.6.15 (`MineShaft.getFish`): mỗi lần cá cắn, game tung **1 lần xúc xắc riêng** cho cá của tầng đó; trượt thì rơi về danh sách thường của mỏ (Cá ma, tảo…).
>
> | Cá | Tỉ lệ mỗi lần cắn | Ở cấp 7, quăng xa bờ |
> |---|---|---|
> | Cá đá (tầng 20) | 2% + 1% × k | **~6%** |
> | Cá băng (tầng 60) | 1,5% + 0,9% × k | **~5%** |
> | Lươn dung nham (tầng 100) | 1% + 0,8% × k | ~4% |
>
> với **k = 1 + 0,4 × cấp Câu cá + 0,1 × độ sâu nước** (quăng càng xa bờ càng sâu). Tức là **~20 lần cắn mới ra 1 con Cá băng**.
>
> **Tăng tỉ lệ:** **Phao mồi kì lạ (Curiosity Lure)** cộng k **+5** (Cá băng lên ~10%) — cần Cần Iridium · **Mồi riêng loài** làm từ chính con cá đó ở **Máy làm mồi (Bait Maker)** cộng k **+10** (lên ~14%) · cả hai → ~19%. Quăng hết tầm cho nước sâu.
>
> **Thạch Hang Động:** ở tầng 20/60 chỉ ra khi xúc xắc cá mỏ trượt **và** các món thường phía trước cũng không rơi — nên cực hiếm. Ở **dung nham tầng 100**, hễ không ra Lươn dung nham là có **5% + 5% × Luck** ra Thạch, còn lại là rác → **để dành tới tầng 100 hãy săn**. Cần tập (Training Rod) dưới mỏ chỉ câu ra rác.

### 🔒 Chưa vào được

| ✅ | Cá | Cần gì |
|---|---|---|
| [ ] | Cá nhảy (Woodskip) 🧩 | Rừng Bí mật — **Rìu Thép** để chặt khúc gỗ |
| [ ] | Cá chép biến dị (Mutant Carp) | Cống ngầm — **Chìa khóa Gỉ** (quyên góp 60 món Bảo tàng) |
| [ ] | Cá cát (Sandfish) · Cá chép bò cạp (Scorpion Carp) | Sa mạc — sửa xe buýt, thường chưa kịp Năm 1 |

### 🎯 Còn làm được trong Xuân này

- [ ] **Cá bống tượng (Goby)** — ra thác nước Rừng Cindersap, 08:00–18:00, ngày nào cũng được.
- [x] **Cá đá** (tầng 20)
- [ ] **Cá băng** (tầng 60) — tiện ghé khi đi mỏ, dùng thang máy xuống thẳng; tỉ lệ thấp (~5%/lần cắn), xem khung Hầm mỏ ở trên.
- [ ] **Cá huyền thoại** — cần ngày mưa + buff +3 Câu cá (xem khung trên).
- Cá trê, Lươn, Cá trích dày mình (🌧️) đều đã có — ngày mưa còn lại cứ dồn cho Cá huyền thoại.

---

## ☀️ Hạ · 🍂 Thu · ❄️ Đông

_Chưa ghi — thêm khi tới mùa, cùng khuôn bảng như Xuân._
