class NhanVien:
    LUONG_CO_BAN = 1800000

    def __init__(self, ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_max):
        self._ma_nv = ma_nv
        self._ho_ten = ho_ten
        self._nam_sinh = nam_sinh
        self._gioi_tinh = gioi_tinh
        self._dia_chi = dia_chi
        self._he_so_luong = he_so_luong if he_so_luong > 0 else 1.0
        self._luong_max = luong_max

    def tinh_thu_nhap(self):
        return self._he_so_luong * self.LUONG_CO_BAN

    def hien_thi(self):
        print(f"[{self._ma_nv}] {self._ho_ten} | Hệ số: {self._he_so_luong}")
        print(f"Thu nhập: {min(self.tinh_thu_nhap(), self._luong_max):,.0f} VNĐ")

class CongTacVien(NhanVien):
    def __init__(self, ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_max, thoi_han, phu_cap_ld):
        super().__init__(ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_max)
        self._thoi_han = thoi_han  
        self._phu_cap_ld = phu_cap_ld

    def tinh_thu_nhap(self):
        # Thu nhập = Lương thường + Phụ cấp lao động
        return super().tinh_thu_nhap() + self._phu_cap_ld

class NhanVienChinhThuc(NhanVien):
    def __init__(self, ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_max, vi_tri):
        super().__init__(ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_max)
        self._vi_tri = vi_tri

class TruongPhong(NhanVien):
    def __init__(self, ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_max, ngay_ql, phu_cap_ql):
        super().__init__(ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_max)
        self._ngay_ql = ngay_ql
        self._phu_cap_ql = phu_cap_ql

    def tinh_thu_nhap(self):
        # Thu nhập = Lương thường + Phụ cấp quản lý
        return super().tinh_thu_nhap() + self._phu_cap_ql

#Kiểm tra chương trình
if __name__ == "__main__":
    ctv = CongTacVien("CTV01", "Nguyễn Văn A", 2002, "Nam", "HN", 1.5, 5000000, "6 tháng", 500000)
    nvct = NhanVienChinhThuc("NV01", "Lê Thị B", 1995, "Nữ", "HCM", 3.0, 15000000, "Kế toán")
    tp = TruongPhong("TP01", "Trần Văn C", 1988, "Nam", "ĐN", 5.0, 30000000, "2020-01-01", 2000000)

    print("--- THÔNG TIN PHÒNG BAN ---")
    for nv in [ctv, nvct, tp]:
        nv.hien_thi()
        print("-" * 20)