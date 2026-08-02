# 📦 Bản XNB và bản CP — tải bản nào

> Về [[00 Home]] · Mods [[Mods]] · An toàn save [[An toàn save]]
>
> _Nhiều mod **đồ họa** trên Nexus cho tải hai bản cho cùng một nội dung. Chọn sai là mất tính năng hoặc hỏng cả bộ mod._

> [!success] Luôn tải bản **CP**. Đừng đụng bản XNB.
> Bản XNB chỉ còn dành cho người **không cài SMAPI** — mà SMAPI là nền của cả bộ mod này.

## Khác nhau ở đâu

**XNB (kiểu cũ, "legacy")** — `.xnb` là định dạng file nội dung **đã biên dịch** của game; hình gốc nằm sẵn ở `Stardew Valley\Content\` dạng `Content\Portraits\Abigail.xnb`, `Content\Characters\Abigail.xnb`… Mod XNB nghĩa là **chép đè thẳng lên file gốc**, cài xong là file gốc biến mất (phải tự sao lưu trước).

**CP (Content Patcher)** — chỉ là **một thư mục** bỏ vào `Mods`, gồm `manifest.json` + `content.json` + ảnh `.png` thường. **Không đụng vào `Content\`**; [[Mods#Content Patcher 2.9.1|Content Patcher]] đọc mô tả rồi "vá" hình vào **lúc game chạy**. Tiền tố `[CP]` trong tên thư mục chính là quy ước ghi "đây là content pack cho Content Patcher".

| | XNB | CP |
|---|---|---|
| Cài / gỡ | Chép đè, phải tự sao lưu file gốc | Thêm/xóa thư mục là xong |
| Game cập nhật | **Bị ghi đè, mất mod** — kể cả khi Steam _Verify integrity_ | Không sao |
| 2 mod cùng sửa 1 nhân vật | **Loại trừ nhau**, chỉ 1 cái sống | Chồng lớp được, có thứ tự ưu tiên |
| Tùy chọn bật/tắt | Không có | Có `config.json` → hiện thẳng ra **GMCM** |
| Đổi theo mùa / thời tiết / trong–ngoài nhà | **Không làm được**, 1 file 1 hình, tĩnh | Làm được — đây là điểm cốt lõi |
| Đa ngôn ngữ | Không | Có |
| SMAPI quản lý | Không thấy mod, không báo lỗi, không nhắc cập nhật | Có đủ |

## Áp vào bộ mod này

Cả hai content pack đang dùng — **bản Việt hóa** và **Seasonal Cute Characters** — đều là **bản CP**, tức là đang đúng. Thư mục `[CP] Seasonal Cute Characters` có **994 file `.png`, 0 file `.xnb`**, và `manifest.json` ghi `"ContentPackFor": "Pathoschild.ContentPatcher"`.

> [!info]- Vì sao bản XNB không thể làm được thứ đang dùng
> Trong `assets\Code\Abigail.json` của pack:
>
> ```json
> "AbigailSpring":        { "Sprite": "Characters/Abigail_Spring",         "Season": "spring" }
> "AbigailWinterIndoor":  { "Sprite": "Characters/Abigail_Winter_Indoor",  "Season": "winter", "Indoors": true }
> "AbigailWinterOutdoor": { "Sprite": "Characters/Abigail_Winter_Outdoor", "Season": "winter", "Outdoors": true }
> ```
>
> Mấy dòng `Season` / `Indoors` / `Outdoors` **chỉ tồn tại được trong CP**. Bản XNB thì Abigail chỉ có **đúng một bộ đồ** mãi mãi — mất sạch phần đồ theo mùa và đồ ấm ngoài trời mùa đông.
>
> Toàn bộ ~70 tuỳ chọn trong GMCM (`HarveyFacialHair`, `PennyFreckles: OnlySummer`…) cũng đến từ khối `ConfigSchema` trong `content.json` — XNB **không có khái niệm này**.

> [!warning] Bản XNB còn đá nhau với bản Việt hóa
> [[Mods#Stardew Valley - Vietnamese|Bản VH]] cũng vẽ lại một số hình (biển báo, bảng hiệu). Hai bên tranh cùng một file `.xnb` gốc thì **chỉ một bên thắng** — bên kia mất trắng. Dạng CP thì chồng lớp được, nên mới có tùy chọn _"Mod đồ họa khác"_ trong GMCM của bản VH để nhường hình cho mod ảnh khác.
