from abc import ABC, abstractmethod
class GiaKhongHopLe(Exception):
    def __init__(self, gia):
        self.gia = gia
        super().__init__(f"Giá {gia} không hợp lệ")

class HangHoa(ABC):
    def __init__(self, ma, ten, nsx, gia):
        self.__ma = ma
        self.__ten = ten
        self.__nsx = nsx
        self.gia = gia

    @property
    def ma_hang(self): return self.__ma_hang
    @property
    def ten_hang(self): return self.__ten_hang
    @property
    def nha_sx(self): return self.__nha_sx
    @property
    def gia(self):
        return self.__gia
    
    @gia.setter 
    def gia(self, value):
        if value < 0:
            raise GiaKhongHopLe(value)
        self.__gia = value

    @abstractmethod
    def loai_hang(self):
        pass

    def inThongTin(self):
        return (f"[{self.loai_hang()}] Mã: {self.__ma_hang}"
                f" | {self.__ten_hang} | NSX: {self.__nha_}"
                f" | Giá: {self.__gia:,.0f}đ") 

    def __str__(self):
        return self.inThongTin()

    def _repr_(self):
        return (f"{self.__class__.__name__}('{self.__ma_}', "
                f"'{self.__ten_hang}', '{self.__nha_}" )   
     def __eq__(self, other):
        if not isinstance(other, HangHoa): return NotImplemented
        return self.__ma_hang == other.__ma_hang

    def __lt__(self, other):
        return self.__gia < other.__gia

    def __hash__(self):
        return hash(self.__ma_hang)

class HangDienMay(HangHoa):
    """Kế thừa HangHoa, thêm: bảo hành, điện áp, công suất."""

    def __init__(self, ma_hang, ten_hang, nha_sx, gia,
                 tg_baohanh, dien_ap, cong_suat):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self.__tg_baohanh = tg_baohanh
        self.__dien_ap    = dien_ap
        self.__cong_suat  = cong_suat

    def loai_hang(self):        
        return "Điện máy"

    def inTTin(self):           # Override — CÙNG TÊN → đa hình
        return (f"{super().inTTin()} | BH: {self.__tg_baohanh}th"
                f" | {self.__dien_ap}V | {self.__cong_suat}W")

class HangSanhSu(HangHoa):
    """Kế thừa HangHoa, thêm: loại nguyên liệu."""

    def __init__(self, ma_hang, ten_hang, nha_sx, gia,
                 loai_nguyenlieu):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self.__loai_nguyenlieu = loai_nguyenlieu

    def loai_hang(self):
        return "Sành sứ"

    def inTTin(self):
        return f"{super().inTTin()} | NL: {self.__loai_nguyenlieu}"

class HangThucPham(HangHoa):
    """Kế thừa HangHoa, thêm: ngày SX, ngày hết hạn."""

    def __init__(self, ma_hang, ten_hang, nha_sx, gia,
                 ngay_sx, ngay_hethan):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self.__ngay_sx     = ngay_sx
        self.__ngay_hethan = ngay_hethan

    def loai_hang(self):
        return "Thực phẩm"

    def inTTin(self):
        return f"{super().inTTin()} | SX: {self.__ngay_sx} | HSD: {self.__ngay_hethan}"

sp1 = HangDienMay("DM01", "Tủ lạnh", "LG", 12_000_000, 24, 220, 150)
sp2 = HangSanhSu("SS01", "Bình hoa", "Minh Long", 350_000, "Sứ cao cấp")
sp3 = HangThucPham("TP01", "Sữa tươi", "Vinamilk", 32_000, "2025-01-01", "2025-07-01")

print("── Đa hình: print(sp) ──")
kho = [sp1, sp2, sp3]
for sp in kho:
    print(sp)               

print("\n── Sắp xếp theo giá ──")
for sp in sorted(kho):
    print(f"  {sp.gia:>12,.0f}đ | {sp.ten_hang}")

print("\n── So sánh & loại trùng ──")
sp1_copy = HangDienMay("DM01", "Tủ lạnh", "LG", 12_000_000, 24, 220, 150)
print(f"  sp1 == sp1_copy? {sp1 == sp1_copy}")
print(f"  set loại trùng: {len([sp1, sp2, sp1_copy])} → {len(set([sp1, sp2, sp1_copy]))}")

print("\n── Validation ──")
try:
    sp_loi = HangDienMay("DM99", "Test", "X", -5000, 12, 220, 50)
except GiaKhongHopLe as e:
    print(f"  Bắt lỗi: {e}")

try:
    h = HangHoa("X", "Test", "Y", 100)
except TypeError as e:
    print(f"  ABC: {e}")

print("\n── Lưu file (with) ──")
with open("kho_hang.txt", "w", encoding="utf-8") as f:
    for sp in kho:
        f.write(repr(sp) + "\n")
print(f"  Đã lưu {len(kho)} sản phẩm")