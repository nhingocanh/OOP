class CanBo:
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi):
        self._ho_ten = ho_ten
        self._tuoi = tuoi
        self._gioi_tinh = gioi_tinh
        self._dia_chi = dia_chi

    def get_ho_ten(self):
        return self._ho_ten

    def __str__(self):
        return f"Họ tên: {self._ho_ten}, Tuổi: {self._tuoi}, Giới tính: {self._gioi_tinh}, Địa chỉ: {self._dia_chi}"

class CongNhan(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, bac):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self._bac = bac

    def __str__(self):
        return super().__str__() + f", Bậc: {self._bac}/10"

class KySu(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, nganh_dao_tao):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self._nganh_dao_tao = nganh_dao_tao

    def __str__(self):
        return super().__str__() + f", Ngành đào tạo: {self._nganh_dao_tao}"

class NhanVien(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, cong_viec):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self._cong_viec = cong_viec

    def __str__(self):
        return super().__str__() + f", Công việc: {self._cong_viec}"

class QLCB:
    def __init__(self):
        self._danh_sach_can_bo = []

    def them_moi_can_bo(self, can_bo):
        self._danh_sach_can_bo.append(can_bo)
        print("Thêm mới thành công!")

    def tim_kiem_theo_ten(self, ten):
        ket_qua = [cb for cb in self._danh_sach_can_bo if ten.lower() in cb.get_ho_ten().lower()]
        if not ket_qua:
            print(f"Không tìm thấy cán bộ có tên: {ten}")
        else:
            print(f"--- Kết quả tìm kiếm cho '{ten}': ---")
            for cb in ket_qua:
                print(cb)

    def hien_thi_danh_sach(self):
        if not self._danh_sach_can_bo:
            print("Danh sách trống.")
        else:
            print("--- Danh sách toàn bộ cán bộ: ---")
            for cb in self._danh_sach_can_bo:
                print(cb)

#chuong trinh chinh

def main():
    qlcb = QLCB()
    while True:
        print("\n--- HỆ THỐNG QUẢN LÝ CÁN BỘ ---")
        print("1. Thêm mới cán bộ")
        print("2. Tìm kiếm theo họ tên")
        print("3. Hiển thị danh sách cán bộ")
        print("4. Thoát")
        
        choice = input("Nhập lựa chọn của bạn: ")

        if choice == '1':
            print("Chọn loại cán bộ: 1-Công nhân, 2-Kỹ sư, 3-Nhân viên")
            type_cb = input("Lựa chọn: ")
            ten = input("Nhập họ tên: ")
            tuoi = int(input("Nhập tuổi: "))
            gioi = input("Nhập giới tính: ")
            dc = input("Nhập địa chỉ: ")

            if type_cb == '1':
                bac = int(input("Nhập bậc (1-10): "))
                qlcb.them_moi_can_bo(CongNhan(ten, tuoi, gioi, dc, bac))
            elif type_cb == '2':
                nganh = input("Nhập ngành đào tạo: ")
                qlcb.them_moi_can_bo(KySu(ten, tuoi, gioi, dc, nganh))
            elif type_cb == '3':
                cv = input("Nhập công việc: ")
                qlcb.them_moi_can_bo(NhanVien(ten, tuoi, gioi, dc, cv))

        elif choice == '2':
            ten_tim = input("Nhập tên cần tìm: ")
            qlcb.tim_kiem_theo_ten(ten_tim)

        elif choice == '3':
            qlcb.hien_thi_danh_sach()

        elif choice == '4':
            print("Cảm ơn bạn đã sử dụng chương trình!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng thử lại.")

if __name__ == "__main__":
    main()