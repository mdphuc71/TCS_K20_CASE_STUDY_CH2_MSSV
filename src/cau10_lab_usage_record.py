print(" ")
from datetime import datetime
ma_phien = input("Nhập mã phiên: ")
ma_may = input("Nhập mã máy: ")
cong_suat_w = float(input("Nhập công suất (W): "))
thoi_luong_phut = int(input("Nhập thời gian sử dụng (phút): "))
don_gia = float(input("Nhập đơn giá điện (VND/kWh): "))

dien_nang = (cong_suat_w / 1000) * (thoi_luong_phut / 60)
chi_phi = dien_nang * don_gia
su_dung_qua_60 = thoi_luong_phut > 60
gio_ghi_nhan = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

print(" ")
print(f"Mã phiên: {ma_phien}")
print(f"Máy: {ma_may}")
print(f"Công suất: {cong_suat_w:.2f} W")
print(f"Thời lượng: {thoi_luong_phut} phút")
print(f"Điện năng: {dien_nang:.3f} kWh")
print(f"Chi phí: {chi_phi:.2f} VND")
print(f"Trên 60 phút: {su_dung_qua_60}")
print(f"Ghi nhận lúc: {gio_ghi_nhan}")
print(" ")