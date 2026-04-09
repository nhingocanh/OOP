class NhanVien:
    def __init__(self, ten_nhan_vien, luong_co_ban, he_so_luong, luong_max):
        self.__ten_nhan_vien = ten_nhan_vien
        self.__luong_co_ban = luong_co_ban
        self.__he_so_luong = he_so_luong
        self.__luong_max = luong_max

    def get_ten_nhan_vien(self):
        return self.__ten_nhan_vien

    def get_luong_co_ban(self):
        return self.__luong_co_ban

    def get_he_so_luong(self):
        return self.__he_so_luong

    def get_luong_max(self):
        return self.__luong_max

    def set_ten_nhan_vien(self, ten_moi):
        self.__ten_nhan_vien = ten_moi

    def set_luong_co_ban(self, luong_moi):
        if luong_moi > 0:
            self.__luong_co_ban = luong_moi

    def set_he_so_luong(self, he_so_moi):
        self.__he_so_luong = he_so_moi

    def tinh_luong(self):
        """Lương = Lương cơ bản * Hệ số lương"""
        return self.__luong_co_ban * self.__he_so_luong

    def tang_luong(self, he_so_tang):
        """
        Tăng hệ số lương. Trả về False nếu tổng lương vượt mức MAX.
        """
        he_so_moi_du_kien = self.__he_so_luong + he_so_tang
        luong_du_kien = self.__luong_co_ban * he_so_moi_du_kien
        
        if luong_du_kien > self.__luong_max:
            print("Thông báo: Tăng lương không thành công! Vượt mức tối đa cho phép.")
            return False
        else:
            self.__he_so_luong = he_so_moi_du_kien
            return True

    def in_ttin(self):
        """Hiển thị thông tin của đối tượng Nhân Viên tương ứng"""
        print(f"Tên: {self.__ten_nhan_vien}")
        print(f"Lương cơ bản: {self.__luong_co_ban:,.0f}")
        print(f"Hệ số lương: {self.__he_so_luong}")
        print(f"Tổng lương: {self.tinh_luong():,.0f}")
        print(f"Mức lương tối đa: {self.__luong_max:,.0f}")
        print("-" * 20)

nv = NhanVien("Trần Văn B", 3000000, 2.0, 15000000)

print(f"Đang làm việc với: {nv.get_ten_nhan_vien()}")

nv.tang_luong(1.5)
nv.in_ttin()