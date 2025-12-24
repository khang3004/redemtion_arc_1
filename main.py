from fastapi import FastAPI
import os
import psycopg2

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from Dockerized FastAPI! 🚀"}

@app.get("/users")
def get_users_from_db():
    # Kết nối DB để lấy danh sách user
    try:
        conn = psycopg2.connect(
            host=os.environ.get('DB_HOST', 'postgres_db'),
            database='zero2hero_db',
            user=os.environ.get('DB_USER'),
            password=os.environ.get('DB_PASS')
        )
        cur = conn.cursor()
        cur.execute("SELECT * FROM users;")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        
        # Format lại dữ liệu trả về cho đẹp
        data = [{"id": r[0], "name": r[1], "role": r[2]} for r in rows]
        return {"status": "success", "data": data}
    except Exception as e:
        return {"status": "error", "message": str(e)}
