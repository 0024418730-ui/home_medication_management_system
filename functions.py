import sqlite3
from database import get_connection
from datetime import datetime

def them_thuoc(ma, ten, loai, han, sl):
    conn = get_connection()
    try:
        # Sử dụng lệnh INSERT INTO để thêm dữ liệu vào SQLite
        conn.execute("INSERT INTO Medicines VALUES (?, ?, ?, ?, ?)", (ma, ten, loai, han, sl))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        # Lỗi này xảy ra khi nhập trùng mã thuốc (Primary Key)
        return False
    except sqlite3.Error as e:
        print(f"Lỗi cơ sở dữ liệu: {e}")
        return False
    finally:
        conn.close()

def lay_tat_ca():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM Medicines")
        data = cursor.fetchall()
        return data
    except sqlite3.Error as e:
        print(f"Lỗi truy vấn: {e}")
        return []
    finally:
        conn.close()

def sua_so_luong(ma, sl_moi):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("UPDATE Medicines SET so_luong = ? WHERE ma_thuoc = ?", (sl_moi, ma))
        conn.commit()
        # rowcount trả về số dòng bị ảnh hưởng, nếu > 0 tức là sửa thành công
        status = cursor.rowcount > 0
        return status
    except sqlite3.Error:
        return False
    finally:
        conn.close()

def xoa_thuoc(ma):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Medicines WHERE ma_thuoc = ?", (ma,))
        conn.commit()
        status = cursor.rowcount > 0
        return status
    except sqlite3.Error:
        return False
    finally:
        conn.close()

def thong_ke_het_han():
    # Lấy ngày hiện tại định dạng YYYY-MM-DD để so sánh trong SQL
    hom_nay = datetime.now().strftime('%Y-%m-%d')
    conn = get_connection()
    try:
        cursor = conn.cursor()
        # Truy vấn các thuốc có hạn dùng nhỏ hơn ngày hôm nay
        cursor.execute("SELECT * FROM Medicines WHERE han_dung < ?", (hom_nay,))
        data = cursor.fetchall()
        return data
    except sqlite3.Error:
        return []
    finally:
        conn.close()