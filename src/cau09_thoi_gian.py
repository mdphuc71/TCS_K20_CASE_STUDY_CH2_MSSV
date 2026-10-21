print(" ")
from datetime import datetime
thoi_diem = datetime.now()
thoi_diem_text = thoi_diem.strftime("%Y-%m-%d %H:%M:%S")
print(thoi_diem)
print(type(thoi_diem))
print(thoi_diem_text)
print(type(thoi_diem_text))
print(" ")
bat_dau = datetime(2026, 10, 14, 13, 15)
ket_thuc = datetime(2026, 10, 14, 15, 5)
thoi_luong = ket_thuc - bat_dau
print(thoi_luong)
print(type(thoi_luong))
print(" ")
# Dự đoán:
# 1:50:00
# <class 'datetime.timedelta'>

#  Giải thích:
# datetime: mốc thời gian cụ thể, có ngày tháng, tính toán được
# str: chỉ là văn bản hiển thị, KHÔNG tính toán được
# timedelta: độ chênh lệch/khoảng thời gian, không có ngày tháng

