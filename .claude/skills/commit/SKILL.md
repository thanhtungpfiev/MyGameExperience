---
name: commit
description: >
  Viết commit message ghi lại VÌ SAO vault tiến hoá như vậy, theo khung
  Problem → Solution → Implications, subject dùng Conventional Commits tiếng Anh.
  Dùng mỗi khi tạo git commit, viết hoặc sửa commit message, hoặc khi người dùng
  nói "commit", "tạo commit", "sửa commit message". Áp dụng cả khi commit chỉ là
  hệ quả của một việc khác.
---

# Commit message

Commit message là bản ghi lịch sử **vì sao vault tiến hoá như vậy** — đoạn văn mà người đọc
sau này rơi vào từ `git blame`. Diff đã nói *cái gì* đổi rồi; message phải cung cấp đúng
phần diff không phục hồi được.

Với vault này thì "vì sao" thường là **một chi tiết game đã kiểm chứng lại**: mở khoá theo
điều kiện gì, thư đến theo ngày hay theo level, bundle nào chặn bundle nào. Diff chỉ cho
thấy con số đã đổi từ 5 thành 6; message mới nói được là vì cái tháp bị khoá.

## Khung: Problem → Solution → Implications

Trả lời ba câu này, theo đúng thứ tự, viết thành văn xuôi:

1. **Problem** — giới hạn, lỗi, hay vướng víu nào buộc phải thay đổi? Trước đó cái gì sai,
   khó hiểu, hoặc không làm theo được?
2. **Solution** — đã chọn cách nào, và **đã cân nhắc rồi loại bỏ phương án nào, vì sao?**
   Một phương án bị loại thường là dòng giá trị nhất trong cả message: nó ngăn người sau
   mở lại cuộc tranh luận đã khép.
3. **Implications** — đánh đổi và hệ quả, **cả tốt lẫn xấu**. Trên hết: điều gì sẽ khiến
   người đọc sau này **bất ngờ**? Giả định đang gánh cả kế hoạch, thứ gỡ ra là hỏng dây
   chuyền, chi tiết chỉ đúng với đúng một phiên bản game.

## Bố cục thân bài

Mỗi phần là một đoạn mở đầu bằng dấu gạch ngang và nhãn viết rõ — nhãn là thứ làm
`git log` quét được bằng mắt và giữ cho khung không tan trở lại thành một khối chữ:

```
- Problem: …

- Solution: …

- Implications: …
```

Bỏ hẳn một phần khi nó không có gì để nói (sửa lỗi chính tả thì làm gì có Implications);
đừng bao giờ để nhãn rỗng. Ngắt dòng ở khoảng 76 ký tự, dòng nối thụt vào cho thẳng với
phần chữ chứ không thẳng với dấu gạch.

## Subject: Conventional Commits, tiếng Anh

**Cả subject lẫn thân bài đều viết bằng tiếng Anh**, đúng như 21 commit gần nhất của repo.
Đây là điểm khác biệt lớn nhất so với vault `MyLifeExperience` bên cạnh — đừng bê quy ước
tiếng Việt từ đó sang.

```
<type>(<Scope>): <Câu mô tả, viết hoa chữ đầu, không dấu chấm cuối>
```

- **type** — dùng đúng năm loại đã có: `feat` (thêm mảng nội dung mới), `fix` (sửa thông
  tin sai), `docs` (bổ sung, mở rộng nội dung đã đúng), `refactor` (sắp xếp lại, không đổi
  thông tin), `chore` (cấu hình vault, .gitignore, việc ngoài nội dung).
  Ranh giới `fix` và `docs` là chỗ hay lẫn: **`fix` khi thông tin cũ sai**, `docs` khi
  thông tin cũ đúng nhưng thiếu.
- **Scope** — tên note **bỏ dấu**, viết hoa như tên note: `Meo` (Mẹo.md), `Ban do`
  (Bản đồ khu vực.md), `Quy hoach` (Quy hoạch nông trại.md), `Daily`, `Mods`. Cấu hình
  vault thì dùng `Obsidian`. Chạm nhiều note cùng lúc thì bỏ scope hẳn, đừng liệt kê.
- Subject một dòng, ≤ ~72 ký tự.

## Cân theo độ phức tạp

| Thay đổi | Message |
|---|---|
| Sửa chính tả, đổi tên, format | Chỉ một dòng subject |
| Sửa nhỏ tự nó đã rõ | Subject + 1–2 câu (thường chỉ cần Problem) |
| Bổ sung nội dung hoặc sắp xếp lại bình thường | Subject + mỗi phần một đoạn, bỏ phần nào rỗng |
| Sửa một chi tiết game sai kéo theo dây chuyền, đổi cấu trúc note | Vài đoạn — chính phần lập luận mới là thứ cần giao |

Đừng bao giờ độn thêm cho đủ khung khi thay đổi nhỏ. Cũng đừng nén một dây chuyền phụ
thuộc nhiều bước xuống còn một dòng.

## Những kiểu nên tránh

- **Kể lại diff.** "Thêm mục X, sửa bảng Y" — người đọc tự thấy được. Xoá đi và nói vì sao
  phải làm những việc đó.
- **Liệt kê mọi thứ đã đụng thành changelog.** Một danh sách gạch đầu dòng điểm danh từng
  note đọc ra chỉ thấy nhiễu; người đọc cần mạch lập luận, không cần bảng kê.
- **Lấy tên note làm bố cục.** Tổ chức theo *ý*, không theo file.
- **Giấu đánh đổi.** Nếu một kế hoạch từ nay phụ thuộc vào thứ tự ngày, hoặc một chi tiết
  chỉ đúng với đúng một phiên bản game, thì phải nói. Chính câu đó là lý do message tồn tại.

## Đặc thù vault này

**Ghi nguồn đã kiểm chứng vào Implications.** Nội dung ở đây là chi tiết game, sai một chỗ
là kéo hỏng cả chuỗi ngày phía sau, mà đọc note thì không thể biết chi tiết đó lấy từ đâu:
đoán, đọc wiki, hay mở file game ra soi. Câu như *"Verified against the installed game
files: Forest_WizardTower_Locked, the wizardJunimoNote mail entry"* nói cho người đọc biết
độ tin của thông tin — thứ mà diff hoàn toàn không cho thấy. Ghi cả phiên bản game khi chi
tiết phụ thuộc phiên bản.

**Link gãy là hỏng thật.** Vault đang có 221 wikilink, và link đi theo `[[tên file]]` nên
đổi tên note là gãy hàng loạt mà không có gì báo. Khi thay đổi có đổi tên hay di chuyển
note, để kết quả kiểm chứng vào Implications.

## Các bước

1. **Đọc thay đổi thật** — `git diff --staged` (hoặc `git diff`, `git status`). Đừng bao
   giờ viết message theo trí nhớ về cuộc hội thoại; diff đã stage mới là nguồn sự thật.
2. **Xem subject gần đây** — `git log -5 --format='%s%n%n%b'` — và giữ cho nhất quán.
3. **Viết subject** theo `type(Scope): …` ở trên, một dòng, ≤ ~72 ký tự.
4. **Viết thân bài** bằng tiếng Anh theo khung, cân theo bảng trên. Ngắt dòng ở ~76 ký tự.
5. **Commit bằng file, không dùng chuỗi inline:**
   ```bash
   git commit -F <đường-dẫn>/msg.txt      # hoặc: git commit --amend -F <đường-dẫn>/msg.txt
   ```
   Chuỗi `-m` nhiều dòng bị shell quoting làm hỏng — cụ thể, here-string của PowerShell
   (`@'…'@`) lọt một ký tự `@` vào message khi chạy qua Bash. Ghi message ra file tạm rồi
   truyền `-F`. File phải là UTF-8 vì tên note nhắc trong thân bài có dấu.
6. **Kiểm lại**: `git log -1 --format='%s%n%n%b'`.

## Về các commit cũ

21 trong 25 commit đã theo `type(Scope):` tiếng Anh; bốn cái sớm nhất thì chưa
(`Initial commit`, `Add Stardew Valley 1.6.15 notes vault`, và hai commit tiếng Việt).
Phần lớn thân bài đã lập luận đúng tinh thần Problem → Solution → Implications nhưng ở
dạng văn xuôi không nhãn. **Nhãn là quy ước kể từ đây**, không viết lại commit cũ.

## Sửa lại message đã có

Chỉ amend commit **chưa push** — kiểm tra bằng `git status -sb` (`ahead N`) hoặc
`git log @{u}..`. Mặc định là **không amend**: cứ để commit cũ nguyên đó và áp quy ước cho
commit kế tiếp.

Viết lại message đã push thì phải force-push, nên **chỉ làm khi người dùng yêu cầu rõ**.
Khi đó đừng amend thủ công từng cái:

1. `git branch backup-<lý-do>` làm phao, và `git stash push` phần đang sửa dở —
   `filter-branch` từ chối chạy khi working tree còn thay đổi chưa commit.
2. Ghi mỗi message mới ra một file tên theo sha ngắn của commit gốc, rồi:
   ```bash
   git filter-branch -f --msg-filter '
     short=$(echo "$GIT_COMMIT" | cut -c1-7)
     if [ -f "$M/$short.txt" ]; then cat "$M/$short.txt"; else cat; fi
   ' -- main <các-nhánh-khác>
   ```
   `$GIT_COMMIT` là sha **gốc**, nên bảng tra không bị lệch khi sha đổi dần. Nhớ liệt kê
   cả nhánh cũ nằm trong `main`, không thì chúng giữ message cũ sống mãi.
3. **Kiểm chứng bắt buộc**: `git diff <backup> main` phải rỗng — chứng minh chỉ message
   đổi, không byte nội dung nào đụng vào. Kiểm luôn `%an %ae %ad` còn nguyên.
4. `git push --force-with-lease` (không dùng `--force` trần), rồi `git stash pop`.

Đừng tham chiếu commit khác bằng sha trong message, vì viết lại là sha đổi hết và tham
chiếu thành trỏ vào hư không — gọi bằng dòng subject của nó thì bền qua mọi lần rewrite.

## Ví dụ

Chỉ subject, vì thay đổi tự nó đã rõ:

```
chore(Obsidian): Set editor fonts and turn off readable line length
```

Một thay đổi mà phần lập luận mới là thứ đáng giá — lấy đúng nội dung commit
`fix(Daily): Correct the wizard chain…` sẵn có, xếp lại theo bố cục có nhãn:

```
fix(Daily): Correct the wizard chain, add the pet and Willy's mail

- Problem: day 5 sent you to the wizard's tower, but the tower stays
  locked until his letter arrives, and that letter only shows up the
  morning after you first step inside the community centre. Followed as
  written, day 5 could not reach him and could not hand in any bundle.

- Solution: move the wizard to day 6, in front of reading the bundle
  boards, and spell the two-day chain out instead of letting the reader
  discover the lock in game. Willy's "new stock" letters turned out to
  key off fishing level rather than date, so they cannot sit in a
  day-by-day plan at all — they get their own table in Meo instead.

- Implications: every day number after 5 now assumes you entered the
  community centre on schedule; slip that and the whole chain shifts.
  Verified against the installed game files: Forest_WizardTower_Locked,
  the wizardJunimoNote mail entry, and Collections_Letters.
```
