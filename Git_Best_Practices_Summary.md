# Git Survival Guide: Rebase vs. Merge & Professional Workflows

Tài liệu tổng hợp các bài học "xương máu" về Git, đúc kết từ thực chiến để tránh conflict và quản lý code chuyên nghiệp.

---

## 1. Bản chất: Merge vs. Rebase

### git merge (Sự thật trần trụi)

- **Hành động:** Tạo ra một "nút thắt" (Merge Commit) để nối hai nhánh lại.
- **Hình dạng:** Lịch sử sẽ có hình thoi (Diamond shape), rẽ nhánh rồi chập lại.
- **Triết lý:** "Tôn trọng lịch sử đúng như nó đã diễn ra (dù có xấu)."
- **Dùng khi:** Muốn lưu lại cột mốc sáp nhập tính năng.

### git rebase (Nghệ thuật sắp đặt)

- **Hành động:** Nhấc bổng code của bạn lên và đặt lại vào vị trí mới nhất (trên đỉnh branch đích).
- **Hình dạng:** Một đường thẳng tắp (Linear history).
- **Triết lý:** "Làm đẹp lịch sử để dễ đọc, dễ quản lý."
- **Dùng khi:** Muốn cập nhật code mới từ `master` vào nhánh cá nhân đang làm dở.

---

## 2. Kim Chỉ Nam Quan Trọng Nhất (The Golden Rule)

> **⚠️ TUYỆT ĐỐI KHÔNG REBASE NHÁNH CHUNG (Shared/Public Branch)**

- **Nhánh Chung:** `master`, `develop`, `release`, hoặc bất kỳ nhánh nào `feature/team-login` mà có nhiều hơn 1 người đang cùng code.
- **Lý do:** Rebase viết lại lịch sử (thay đổi commit ID). Nếu bạn làm vậy trên nhánh chung, bạn sẽ hủy hoại code của đồng nghiệp (gây duplicate commit, conflict kinh hoàng).
- **Chỉ Rebase khi:** Nhánh đó là "sân chơi riêng" của một mình bạn (Private Branch).

---

## 3. Quy trình làm việc (Workflow)

### Case A: Solo Dev / Feature Riêng (1 mình 1 nhánh)

Đây là cách làm việc chuẩn "GitHub Flow" để code luôn sạch đẹp.

1. **Khởi tạo:** `git checkout -b feature/my-task`
2. **Cập nhật:** Hàng ngày (hoặc trước khi push), lấy code mới nhất từ team về:
    - `git fetch origin master:master` (Cập nhật master ngầm)
    - `git rebase master` (Đặt code mình lên trên code mới nhất)
3. **Hoàn thành:**
    - `git push origin feature/my-task` (Push nhánh thẳng hàng lên).
    - **Lên GitHub tạo Pull Request (PR).**
    - Leader review ok -> Bấm nút **Merge** trên web.

### Case B: Teamwork (Nhiều người 1 nhánh)

Khi bắt buộc phải chui chung vào một nhánh lớn (`feature/big-module`).

1. **Chia để trị (Ưu tiên số 1):** Cố gắng tách nhánh con nữa nếu được (`feature/big-module-ui`, `feature/big-module-api`). Ai xong thì merge vào nhánh cha này.
2. **Kỷ luật thép (Nếu không tách được):**
    - Phân chia file rõ ràng, tránh sửa cùng dòng code.
    - **Pull Early, Pull Often:** Pull liên tục 1-2h/lần để xử lý conflict nhỏ ngay lập tức.
    - Dùng lệnh: `git pull --rebase origin feature/big-module` (Giúp code chưa push của bạn được đặt lên trên code mới của đồng nghiệp, tránh tạo merge commit rác liên tục).

---
****
## 4. Các câu lệnh & Mẹo vặt "Thần thánh"

| Tình huống                                  | Lệnh Khuyên Dùng                 | Giải thích                                                     |
| :------------------------------------------ | :------------------------------- | :------------------------------------------------------------- |
| **Cập nhật Master (khi đang ở nhánh con)**  | `git fetch origin master:master` | Lấy code master mới nhất về máy mà không cần checkout qua lại. |
| **Dọn dẹp nhánh con**                       | `git rebase master`              | Làm code nhánh con thẳng hàng với master.                      |
| **Lấy code đồng nghiệp (trên nhánh chung)** | `git pull --rebase`              | Cập nhật code về và đặt code mình lên trên, tránh merge rác.   |
| **Gắp 1 commit sang nhánh khác**            | `git cherry-pick <commit-hash>`  | Dùng cho hotfix hoặc khi lỡ commit lộn nhánh.                  |
| **Chót Rebase quên Push**                   | `git push --force` (hoặc `-f`)   | **Cẩn thận!** Chỉ dùng cho nhánh riêng của mình.               |

---

## 5. Tổng kết ngắn gọn

1. **Rebase** cho **CÁ NHÂN** (để dọn dẹp).
2. **Merge** cho **TẬP THỂ** (để chốt đơn/lưu lịch sử).
3. **Đừng bao giờ** viết lại lịch sử (rebase) code mà người khác đang dùng.

$$
J(\theta) = \frac{1}{2m} \sum_{i=1}^{m} (h_\theta(x^{(i)}) - y^{(i)})^2
$$