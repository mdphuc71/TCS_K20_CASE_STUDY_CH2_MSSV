print(" ")
ma_may = input("Nhập mã máy: ")
cong_suat_w = float(input("Nhập công suất W: "))  
so_phut = int(input("Nhập số phút: "))
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
print(f"Máy: {ma_may}")
print(f"Điện năng: {dien_nang_kwh:.3f} kWh")
print(" ")
# Lỗi 1 — TypeError: biến cong_suat_w kiểu chuỗi không tính toán được
# Nguyên nhân: input() trả về str, không chuyển sang số nên không nhân với int được
# Cách sửa: dùng float(input(...)) để chuyển công suất sang kiểu số thực

# Lỗi 2 — SyntaxError + NameError: thiếu dấu đóng ngoặc và sai tên biến
# Nguyên nhân: dòng print thiếu ký tự ')' ở cuối; đồng thời gọi biến dien_nang
# trong khi khai báo là dien_nang_kwh → Python hiểu là 2 biến khác nhau
# Cách sửa: thêm ')' và viết đúng tên biến dien_nang_kwh