// Khôi phục một bản vẽ stardewplan.com từ file *-stardewplan.json trong thư mục này.
// 1. Trên stardewplan.com: Plan options → New plan → Standard Farm, rồi Rename đúng `label` trong file.
// 2. F12 → Console, dán cả file này rồi Enter.
// 3. Gõ: khoiPhuc(<dán toàn bộ nội dung file .json>) rồi Enter. Trang tự tải lại.
// 4. Sửa một thứ bất kỳ trên bản vẽ (hoặc Rename giữ nguyên tên) để trang đẩy lên tài khoản.
async function khoiPhuc(plan) {
  const db = await new Promise((ok, err) => {
    const r = indexedDB.open('stardew-planner');
    r.onsuccess = () => ok(r.result);
    r.onerror = () => err(r.error);
  });
  const all = (store) => new Promise((ok) => {
    const q = db.transaction(store).objectStore(store).getAll();
    q.onsuccess = () => ok(q.result);
  });
  const map = (await all('maps')).find((m) => m.label === plan.label);
  if (!map) throw new Error(`Không thấy bản vẽ tên "${plan.label}" — tạo và đổi tên trước đã`);
  const meta = (await all('mapMeta')).find((m) => m.projectId === map.projectId && m.mapId === map.mapId);
  const now = Date.now();
  map.state = plan.state;
  map.updatedAt = now;
  Object.assign(meta, { dirty: true, syncState: 'pending', updatedAt: now });
  await new Promise((ok, err) => {
    const tx = db.transaction(['maps', 'mapMeta'], 'readwrite');
    tx.objectStore('maps').put(map);
    tx.objectStore('mapMeta').put(meta);
    tx.oncomplete = ok;
    tx.onerror = () => err(tx.error);
  });
  location.reload();
}
