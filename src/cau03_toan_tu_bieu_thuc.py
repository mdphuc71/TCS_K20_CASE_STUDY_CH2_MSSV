print(" ")
print("Bài 3. Toán tử và biểu thức")
print(" ")

tong_phut = 135
cong_suat_w = 250

print(f" Số giờ trọn vẹn: {tong_phut // 60 }")
print(f" Số phút còn lại: {tong_phut % 60 }")
print(" ")

su_dung_lau = bool( tong_phut > 60 )
print(f" Khi tong_phut > 60: {su_dung_lau}")
print(" ")

du_lieu_hop_le = bool(tong_phut > 0) and (cong_suat_w > 0)
print(f" Khi cong_suat_w > 0 và tong_phut > 0: {du_lieu_hop_le}")
print(" ")

bt1 = 100 + 20 * 3
bt2 = (100 + 20) * 3

print(f"  100 + 20  * 3 = {bt1}")
print(f" (100 + 20) * 3 = {bt2}")
print(" ")