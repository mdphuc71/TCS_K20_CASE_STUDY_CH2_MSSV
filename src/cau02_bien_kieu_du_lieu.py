print(" ")
print(f"Bài 2: Biến và kiểu dữ liệu")
print(" ")
print(f" Phiên sử dụng có thông tin:")
ma_phien = "LAB026"
ma_may = "PC12"
cong_suat = 250.0 
thoi_gian = 90 
trang_thai = True
ghi_chu = None


print(f" Mã phiên                  : {ma_phien}      | Kiểu: {type(ma_phien)}")
print(f" Mã máy                    : {ma_may}        | Kiểu: {type(ma_may)}")    
print(f" Công suất                 : {cong_suat} W     | Kiểu: {type(cong_suat)} ")
print(f" Thời gian                 : {thoi_gian} Phút     | Kiểu: {type(thoi_gian)}")
print(f" Trạng thái đang hoạt động : {trang_thai}        | Kiểu: {type(trang_thai)}    ")
print(f" Ghi chú                   : {ghi_chu}        | Kiểu: {type(ghi_chu)}")

# Mã phiên: str
# Mã máy: str
# Công suất: float
# Thời gian: int
# Trạng thái đang hoạt động: bool
# Ghi chú: NoneType
print(" ")
print(f" Thay thời gian sử dụng từ 90 thành 120 ")
thoi_gian = 120
print(f" Thời gian : {thoi_gian} Phút ")
print(" ")

