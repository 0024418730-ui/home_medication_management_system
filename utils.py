from datetime import datetime

def kiem_tra_ngay(ngay_str):
    """Kiểm tra định dạng YYYY-MM-DD"""
    try:
        datetime.strptime(ngay_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def kiem_tra_so_luong(sl_str):
    """Kiểm tra số lượng phải là số nguyên không âm"""
    try:
        sl = int(sl_str)
        return sl if sl >= 0 else None
    except ValueError:
        return None