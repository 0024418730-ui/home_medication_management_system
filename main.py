import sys
from database import init_db
import functions as func
import utils

def login():
    """Logic đăng nhập 3 lần bám sát yêu cầu"""
    for i in range(3):
        tk = input('Nhập tên đăng nhập: ')
        mk = input('Nhập mật khẩu: ')
        
        if tk == 'Admin' and mk == 'abc':
            print('🎉 Đăng nhập thành công!')
            return True
        else:
            print('Tên đăng nhập hoặc mật khẩu không đúng.')
            if i < 2:
                print(f'Bạn còn {2-i} lần thử')
            else:
                print('Tài khoản đã bị khóa!')
    return False

def hien_thi_menu():
    print("\n" + "="*20 + " QUẢN LÝ TỦ THUỐC GIA ĐÌNH " + "="*20)
    print("1. Xem danh sách thuốc")
    print("2. Thêm thuốc mới")
    print("3. Cập nhật số lượng")
    print("4. Xóa thuốc")
    print("5. Thống kê thuốc hết hạn")
    print("0. Thoát chương trình")
    print("=" * 67)

def main():
    init_db() # Đảm bảo file .db được tạo ngay khi chạy
    if not login():
        sys.exit()

    while True:
        hien_thi_menu()
        chon = input("Chọn chức năng (0-5): ")

        if chon == '1':
            data = func.lay_tat_ca()
            print(f"\n{'Mã':<10} {'Tên Thuốc':<20} {'Loại':<15} {'Hạn dùng':<12} {'SL':>5}")
            print("-" * 67)
            for r in data:
                print(f"{r[0]:<10} {r[1]:<20} {r[2]:<15} {r[3]:<12} {r[4]:>5}")
        
        elif chon == '2':
            ma = input("Mã thuốc (duy nhất): ").upper()
            ten = input("Tên thuốc: ")
            loai = input("Loại thuốc: ")
            while True:
                han = input("Hạn dùng (YYYY-MM-DD): ")
                if utils.kiem_tra_ngay(han): break
                print("⚠️ Sai định dạng ngày!")
            while True:
                sl = utils.kiem_tra_so_luong(input("Số lượng: "))
                if sl is not None: break
                print("⚠️ Số lượng phải là số nguyên dương!")
            
            if func.them_thuoc(ma, ten, loai, han, sl):
                print("✅ Thêm thành công!")
            else:
                print("❌ Lỗi: Mã thuốc đã tồn tại!")

        elif chon == '3':
            ma = input("Nhập mã thuốc cần sửa: ").upper()
            sl = utils.kiem_tra_so_luong(input("Nhập số lượng mới: "))
            if sl is not None and func.sua_so_luong(ma, sl):
                print("✅ Đã cập nhật!")
            else:
                print("❌ Không tìm thấy mã thuốc hoặc dữ liệu sai!")

        elif chon == '4':
            ma = input("Nhập mã thuốc cần xóa: ").upper()
            if func.xoa_thuoc(ma):
                print("✅ Đã xóa!")
            else:
                print("❌ Không tìm thấy mã thuốc!")

        elif chon == '5':
            het_han = func.thong_ke_het_han()
            print(f"\n🚨 Phát hiện {len(het_han)} thuốc hết hạn:")
            for h in het_han:
                print(f"- {h[1]} (Hết hạn: {h[3]})")

        elif chon == '0':
            print("Cảm ơn bạn đã sử dụng chương trình!")
            break
        
        input("\nNhấn Enter để tiếp tục...")

if __name__ == "__main__":
    main()