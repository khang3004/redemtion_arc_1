import os
import psycopg2
from time import sleep

# Lấy thông tin kết nối từ Biến Môi Trường (được set trong docker-compose.yml)
# Code này sẽ linh hoạt: Chạy máy Khang thì lấy pass của Khang, chạy máy Server thì lấy pass Server.
DB_HOST = os.environ.get('DB_HOST', 'postgres_db')
DB_USER = os.environ.get('DB_USER', 'khang_admin')
DB_PASS = os.environ.get('DB_PASS', 'secret123')
DB_NAME = 'zero2hero_db'

print("⏳ Đang cố gắng kết nối tới Database...", flush=True)

try:
    # Thực hiện kết nối
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )
    
    # Tạo con trỏ để thực thi lệnh SQL
    cur = conn.cursor()
    
    # 1. Tạo bảng (nếu chưa có)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            role VARCHAR(50)
        );
    """)
    
    # 2. Thêm dữ liệu mẫu
    cur.execute("INSERT INTO users (name, role) VALUES ('KhangDS', 'AI Engineer');")
    cur.execute("INSERT INTO users (name, role) VALUES ('Docker', 'DevOps Tool');")
    
    # Commit thay đổi
    conn.commit()
    
    # 3. Lấy dữ liệu ra xem
    cur.execute("SELECT * FROM users;")
    rows = cur.fetchall()
    
    print("\n🎉 KẾT NỐI THÀNH CÔNG! Dữ liệu trong Database:")
    for row in rows:
        print(f" - ID: {row[0]} | Name: {row[1]} | Role: {row[2]}")
        
    cur.close()
    conn.close()

except Exception as e:
    print(f"\n❌ LỖI KẾT NỐI: {e}")
