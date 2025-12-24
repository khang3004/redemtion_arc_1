# 1. FROM: Chọn hệ điều hành cơ sở (Base Image)
# Giống như việc bạn chọn mua đất để xây nhà.
# Ở đây ta chọn image có sẵn công cụ 'pixi' để đỡ phải cài đặt lại từ đầu.
FROM ghcr.io/prefix-dev/pixi:latest

# 2. WORKDIR: Thiết lập thư mục làm việc
# Giống như lệnh 'cd' vào thư mục dự án. Mọi lệnh sau dòng này sẽ diễn ra ở đây.
WORKDIR /app

# 3. COPY (Lần 1): Copy file cấu hình trước
# Tại sao chỉ copy 2 file này trước? Để tận dụng cơ chế "Cache" của Docker.
# Nếu code bạn thay đổi nhưng pixi.toml không đổi, Docker sẽ bỏ qua bước cài đặt lại (rất tốn thời gian).
COPY pixi.toml pixi.lock ./

# 4. RUN: Cài đặt dependencies
# Lệnh này chạy LÚC BUILD (lúc xây nhà).
# --frozen: Đảm bảo cài đúng phiên bản chính xác trong lock file (không tự update lung tung).
RUN pixi install --frozen

# 5. COPY (Lần 2): Copy toàn bộ source code
# Bây giờ mới copy phần còn lại (.py file, data...).
COPY . .

# 6. CMD: Lệnh mặc định khi chạy container
# Lệnh này chạy LÚC RUN (lúc dọn vào ở).
# Dùng 'pixi run' để đảm bảo python được gọi từ môi trường ảo của pixi.
CMD ["pixi", "run", "python", "python_tutorial/logic_flow.py"]
