import sqlite3
import os

# Tự động xác định đường dẫn để file .db nằm cùng thư mục với code
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "TuThuoc.db")

def get_connection():
    return sqlite3.connect(DB_PATH)

def init_db():
    """Khởi tạo file database và bảng dữ liệu"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Medicines (
            ma_thuoc TEXT PRIMARY KEY,
            ten_thuoc TEXT NOT NULL,
            loai_thuoc TEXT,
            han_dung TEXT,
            so_luong INTEGER
        )
    ''')
    conn.commit()
    conn.close()