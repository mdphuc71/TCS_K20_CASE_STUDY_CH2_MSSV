print(" ")

ma_may = input("Nhập mã máy: ")
print(type(ma_may))
cong_suat_W = input("Nhập công suất (W): ")
print(type(cong_suat_W))

so_phut = input("Nhập số phút sử dụng: ")
print(type(so_phut))

don_gia = input("Nhập đơn giá điện (đ/kWh): ")
print(type(don_gia)) 

print(" ")
cong_suat_W = float(cong_suat_W)  
so_phut = int(so_phut)             
don_gia = float(don_gia)

dien_nang_kWh = (cong_suat_W / 1000) * (so_phut / 60)
chi_phi = dien_nang_kWh * don_gia

print(f"Mã máy: {ma_may}")
print(f"Công suất: {cong_suat_W} W")
print(f"Thời gian sử dụng: {so_phut} phút")
print(f"Điện năng tiêu thụ: {dien_nang_kWh} kWh")
print(f"Chi phí điện: {chi_phi:,.0f} đồng")
print(" ")