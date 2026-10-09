# 🪱 Điểm cổ vật (Artifact Spot)

> Về [[00 Home]] · Mẹo chơi [[Mẹo]] · Bản đồ [[Bản đồ khu vực]]
>
> _Tra cứu: đào bằng gì, ra món gì, luật mọc, "Hạt giống cổ đại", Đất sét và cổ vật trùng. Mẹo lượm chung ở [[Mẹo#🌰 Lượm (Foraging)|Mẹo — Lượm]]._

Mảng đất nhỏ sẫm màu có **3 con giun trắng ngọ nguậy** nhô lên — nên hay được gọi là "điểm giun đất", nhưng bản dịch trong game gọi là **Điểm cổ vật**. Đào bằng **Cuốc (Hoe)**, một nhát là xong.

⚠️ **Cuốc chim (Pickaxe) không ăn** — chỉ Cuốc mới đào được. Đây là chỗ hay bấm nhầm rồi tưởng nó hỏng.

| Nhóm | Món ra | Dùng làm gì |
|---|---|---|
| 🧱 **Nguyên liệu** | **Đất sét (Clay)** — hay ra nhất · Đá · Than · Quặng | Đất sét là lý do chính phải đào mỗi ngày |
| 🏺 **Cổ vật (Artifacts)** | Mỗi khu một bảng riêng | Quyên góp **Bảo tàng** cho Gunther |
| 📖 **Cuốn sách thất lạc (Lost Book)** | **21 cuốn** cả game | Tự bay vào **Thư viện**, mở kiến thức ẩn |
| ❄️ **Mùa Đông** | **Rễ cây mùa đông (Winter Root)** · **Khoai lang tuyết (Snow Yam)** | Chỉ ra khi đào/cuốc đất, không mọc trên mặt đất |

**Ba luật phải nhớ:**

1. **Chỉ mọc ngoài trời**, trên ô đào được — Thị trấn, Rừng, Núi, Bãi biển, Bến Xe, và cả trên nông trại.
2. **Không biến mất lúc hết ngày.** Mỗi đêm, mỗi điểm chưa đào có **15%** khả năng biến mất, còn lại nằm nguyên. Thấy rồi để mai đào vẫn được, nhưng để lâu thì dễ mất.
3. **Điểm mới chỉ mọc khi khu đó gần hết điểm**: còn tối đa 1 điểm (trên nông trại: không còn điểm nào; mùa Đông: còn tối đa 4). Đào hết điểm cũ thì hôm sau mới mọc thêm, vị trí ngẫu nhiên. **May mắn không ảnh hưởng** số điểm mọc.

> [!info] Khoảng 1/6 "Điểm cổ vật" thật ra là điểm hạt giống
> Từ 1.6, mỗi điểm mới mọc có 16,6% là **Seed Spot** — trông y hệt và bản dịch cũng hiện tên **Điểm cổ vật**, nhưng đào lên ra **hạt giống** thay vì món ở bảng trên.

_Đã kiểm trong file game 1.6.15: luật mọc/biến mất ở `GameLocation.spawnObjects` (xoá 15% mỗi đêm, chỉ mọc khi còn ≤ 1 điểm, 16,6% là `SeedSpot`), bảng món rơi ở `Data/Locations` (`ArtifactSpots`)._

**Bảng cổ vật khác nhau theo từng khu**, nên muốn đủ bộ Bảo tàng thì phải đào **rải khắp các khu**, đào mãi một chỗ sẽ thiếu. Cổ vật chưa quyên góp thì mang đi donate trong ngày, chưa kịp thì tạm cất rương **`Cổ Vật, Đồ Trang Trí, Trang Phục`** (xem [[Quy hoạch nông trại#📦 Kho & rương — bảng màu và cách đặt tên|Kho & rương]]).

> [!warning] "Hạt giống cổ đại" — bản dịch đặt **cùng một tên** cho hai món khác nhau
> | | Cổ vật (Ancient Seed) | Gói hạt (Ancient Seeds) |
> |---|---|---|
> | Mã game | `(O)114` | `(O)499` |
> | Mô tả khi rê chuột | _"Hạt giống đã khô kiệt… nhìn kiểu gì cũng thấy nó đã chết lâu rồi"_ | _"Liệu chúng có nảy mầm được nữa không?"_ |
> | Trồng được? | ❌ | ✅ ra **Trái cổ đại (Ancient Fruit)** |
>
> Tặng **cổ vật đầu tiên** cho Bảo tàng → nhận **1 gói hạt** + **công thức chế tác** `1 cổ vật → 1 gói hạt`. Nên công thức trông như "Hạt giống cổ đại → Hạt giống cổ đại" là **đúng**, không phải lỗi: cổ vật nhặt về sau cứ chế hết thành hạt.
>
> Trái cổ đại: Xuân–Thu, **28 ngày** lớn lần đầu rồi **7 ngày** ra trái lại, cây sống mãi; **không trồng được trong chậu** — hợp nhất là Nhà kính. Nhân giống bằng **Máy tạo Hạt giống (Seed Maker)** trước khi đem ủ rượu (xem [[Mẹo#💰 Kiếm tiền theo giai đoạn|Mẹo — Kiếm tiền]]).
>
> ⚠️ **Gieo gói hạt ngay, đừng để dành chờ máy.** Máy tạo Hạt giống nhận **trái** (1 Trái cổ đại → 1–3 gói hạt _— số lượng do code game tính, chưa kiểm chứng_), không nhận hạt — gói hạt để trong túi thì chẳng nhân được gì, chỉ mất trắng một mùa sinh trưởng. Máy lại mở ở **Trồng trọt cấp 9** (25 Gỗ + 10 Than đá + 1 Thỏi vàng), còn xa. Lộ trình: gieo ngay → trái ra thì **cất vào rương `Rau, Hoa, Trái Cây`**, đừng bán/ủ → có máy rồi đem nhân → cổ vật đào thêm cứ chế thành hạt gieo luôn.

> [!tien] Đất sét — gom từ Ngày 1, đừng đợi tới lúc cần
> **Kho chứa Cỏ (Silo) cần 10 Đất sét.** Đất sét gần như chỉ ra từ điểm cổ vật (cuốc đất thường cũng có tỉ lệ nhỏ). Đào tốn **2 năng lượng**/nhát, mà `InfiniteStamina` đang bật nên với máy này là **miễn phí** — thấy giun là đào, không có lý do bỏ qua.

> [!tien] Cổ vật trùng — đã quyên góp rồi, nhặt thêm thì làm gì?
> Bảo tàng chỉ đếm **mỗi món một lần**, món trùng không đẩy mốc thưởng nào lên. Biết món nào trùng: rê chuột lên — **UI Info Suite 2** còn hiện **icon đầu Gunther** là **chưa** quyên góp, hết icon là trùng.
>
> | Món trùng | Làm gì |
> |---|---|
> | **Hạt giống cổ đại** (cổ vật) | Chế thành gói hạt rồi gieo — xem khối ngay trên |
> | **Trứng khủng long** | Ấp trong **Lò ấp trứng** ở **Chuồng gia cầm lớn** → khủng long đẻ thêm trứng |
> | Còn lại | **Tặng Penny hoặc Dwarf** — cả hai đều **Thích** mọi cổ vật · hoặc bỏ thùng giao hàng |
>
> Giá gốc vài món: **Búp bê kỳ lạ** 1.000g · **Mặt nạ hoàng kim** 500g · **Trứng khủng long** 350g · **Tượng gà**, **Rìu đá tiền sử** 50g · **Thìa rỉ sét** 25g · **Cuộn giấy Người lùn I–IV** 1g. Đọc sách **Treasure Appraisal Guide** (bản dịch để nguyên tiếng Anh) thì giá bán cổ vật **×3**. Món rẻ như Thìa rỉ sét đem tặng Penny còn được hơn bán.
>
> _Giá, sở thích quà theo [Artifacts](https://stardewvalleywiki.com/Artifacts) và [Penny](https://stardewvalleywiki.com/Penny) trên wiki 1.6; tên món theo file bản Việt hoá đang cài._
