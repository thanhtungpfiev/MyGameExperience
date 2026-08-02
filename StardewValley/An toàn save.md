# 🛟 An toàn save — Stardew Valley 1.6.15

> Về [[00 Home]] · Mods [[Mods]] · Nhật ký [[Daily]]
>
> _Đọc note này **trước khi thêm/bớt mod giữa chừng**. Hai mod đang dùng có đụng vào save serializer, và có 3 lớp lưu chồng nhau cần hiểu rõ vai trò._

## ⚠️ Hai mod đổi save serializer

SMAPI cảnh báo mỗi lần khởi động:

> _These mods change the save serializer. They may corrupt your save files, or make them unusable if you uninstall these mods._ — **MultiSave - Continued**, **QuickSave**

**Quyết định hiện tại: giữ cả hai**, vì hai mod làm hai việc khác nhau — [[Mods#QuickSave 1.5.0 ⚠️ _đổi save serializer_|QuickSave]] lưu giữa ngày với 1 slot ghi đè, [[Mods#MultiSaveContinued 1.0.7 ⚠️ _đổi save serializer_|MultiSave]] giữ nhiều mốc theo ngày game.

> [!save] Không gỡ đột ngột
> Gỡ một trong hai có thể làm save **không mở lại được**. Muốn gỡ: sao lưu trước → vào game **ngủ 1 đêm** để game ghi lại save bằng serializer gốc → mới gỡ.
>
> Đây cũng là 2 mod nghi phạm đầu tiên nếu save hỏng hoặc game không load được.

## 🗄️ Ba lớp lưu — vai trò khác nhau, không thay thế nhau

| Lớp | Mốc giữ được | Đơn vị | Ghi ở đâu |
|---|---|---|---|
| **QuickSave** (`F5`/`F7`) | **1** (ghi đè) | **đúng khoảnh khắc** trong ngày | `Quicksave` trong thư mục save |
| **MultiSave** (`F8` + tự động) | **7 ngày game** | **đầu** ngày game | `MultiSave_*` trong thư mục save |
| **Save Backup** (tự động) | **10 bản** | **ngày thực** | thư mục game (xem dưới) |

## 💾 Save Backup — mod SMAPI tự cài kèm

Không nằm trong thư mục mod tải về, SMAPI tự nạp từ `Mods\SaveBackup`. Cách hoạt động:

- Chạy **1 lần/ngày, ngay lúc khởi động game** — không phải lúc bạn lưu hay ngủ. Mở game 3 lần trong ngày thì chỉ backup ở lần đầu.
- Nén **toàn bộ** thư mục `Saves` thành 1 file `.zip`, gồm cả `Quicksave` lẫn các thư mục `MultiSave_*`.
- Giữ **10 bản gần nhất**, tự xóa bản cũ nhất. Đổi số này bằng cách tạo `Mods\SaveBackup\config.json` với `{ "BackupsToKeep": 30 }`.

**Nơi lưu** — `C:\Program Files (x86)\Steam\steamapps\common\Stardew Valley\save-backups\`

> [!save] Backup nằm trong thư mục game, không phải AppData
> Steam _Verify integrity of game files_, gỡ/cài lại game, hay chuyển thư viện sang ổ khác đều có thể **xóa sạch backup**. Nên copy định kỳ sang ổ `F:` hoặc cloud.

> [!lich] Tên file dùng ngày UTC
> VN là UTC+7 nên mở game trước 7h sáng sẽ ra tên file **lùi 1 ngày** — không phải thiếu backup.

## 🔧 Khôi phục khi hỏng save

1. **Thoát game.**
2. Giải nén file zip cần dùng trong `save-backups`.
3. Chép đè thư mục save (`Wind_<số>`) vào `%AppData%\StardewValley\Saves\`.
4. Mở game — save quay về trạng thái buổi sáng ngày đó.
