class HangHoa:
    def __init__(self, ma_hang, ten_hang, nha_sx, gia):
        self._ma_hang = ma_hang
        self._ten_hang = ten_hang
        self._nha_sx = nha_sx
        self._don_gia = gia

    def hienthi(self):
        print(f"Mã hàng: {self._ma_hang}")
        print(f"Tên hàng: {self._ten_hang}")
        print(f"Nhà sản xuất: {self._nha_sx}")
        print(f"Đơn giá: {self._don_gia:,.0f} VNĐ")

class HangDienMay(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, tg_baohanh, dien_ap, cong_suat):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self._tg_baohanh = tg_baohanh
        self._dien_ap = dien_ap
        self._cong_suat = cong_suat

    def hienthi(self):
        super().hienthi()
        print(f"Bảo hành: {self._tg_baohanh} tháng")
        print(f"Điện áp: {self._dien_ap}V | Công suất: {self._cong_suat}W")

class HangSanhSu(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, loai_nguyenlieu):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self._loai_nguyenlieu = loai_nguyenlieu

    def hienthi(self):
        super().hienthi()
        print(f"Nguyên liệu: {self._loai_nguyenlieu}")

class HangThucPham(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, ngay_sx, ngay_hethan):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self._ngay_sx = ngay_sx
        self._ngay_hethan = ngay_hethan

    def hienthi(self):
        super().hienthi()
        print(f"Ngày sản xuất: {self._ngay_sx}")
        print(f"Ngày hết hạn: {self._ngay_hethan}")

# Chương trình chính
if __name__ == "__main__":
    danh_sach = [
        HangDienMay("DM01", "Tivi Samsung 4K", "Samsung", 15000000, 24, 220, 100),
        HangSanhSu("SS01", "Bình hoa Chu Đậu", "Hải Dương", 2500000, "Gốm sứ"),
        HangThucPham("TP01", "Sữa tươi sạch", "TH True Milk", 45000, "2024-01-01", "2024-01-10")
    ]
    
    for hang in danh_sach:
        print(f"\n--- Thông tin {type(hang).__name__} ---")
        hang.hienthi()