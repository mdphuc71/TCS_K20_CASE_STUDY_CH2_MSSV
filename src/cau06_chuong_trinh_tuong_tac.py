print(" ")

ma_phien = input("Nhập mã phiên: ").strip()
ma_may = input("Nhập mã máy: ").strip()
cong_suat = float(input("Nhập công suất (W): "))
so_phut = float(input("Nhập số phút sử dụng: "))
don_gia = float(input("Nhập đơn giá (đ/kWh): "))

thoi_gian_gio = so_phut / 60
dien_nang = cong_suat * thoi_gian_gio / 1000

chi_phi = dien_nang * don_gia

print(f"Mã phiên: {ma_phien}")
print(f"Máy: {ma_may}")
print(f"Điện năng: {dien_nang}")
print(f"Chi phí: {chi_phi}")

print(" ")