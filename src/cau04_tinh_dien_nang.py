print(" ")
print("Bài 4. Tính điện năng và chi phí:")
cong_suat_w = 250
so_phut = 90
don_gia_kwh = 3000
print(" ")

dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

print(f" Điện năng tiêu thụ : {dien_nang_kwh} kwh    | Kiểu: {type(dien_nang_kwh)}")
print(f" Chi phí điện       : {chi_phi}       | Kiểu: {type(chi_phi)}")

# Dự đoán: 
# Điện năng tiêu thụ: 0.375 kwh    | Kiểu: <class 'float'>
# Chi phí điện      : 750          | Kiểu: <class 'float'>
print(" ")

so_phut = 60
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh 
print(f" Điện năng tiêu thụ : {dien_nang_kwh} kwh     | Kiểu: {type(dien_nang_kwh)}")
print(f" Chi phí điện       : {chi_phi:,.0f}        | Kiểu: {type(chi_phi)}")
print(" ")

# So sánh: Điện năng tiêu thụ và chi phí điện ở phút 60 nhỏ hơn điện năng tiêu thụ và chi phí điện ở phút 90.