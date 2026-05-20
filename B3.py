# Đầu vào: tên và tuổi bệnh nhân đã được kiểm tra
# Đầu ra: Đưa ra xếp loại ưu tiên và tránh các bẫy dữ liệu 

full_name = input("Hãy nhập họ và tên bệnh nhân:")
if full_name.strip() == "":
    print("Tên không hợp lệ. KHÔNG THỂ IN PHIẾU KHÁM!")
    exit()

age = int(input("Hãy nhập tuổi bệnh nhân:"))
if age < 0 or age > 150:
    print("Tuổi không hợp lệ. KHÔNG THỂ IN PHIẾU KHÁM!")
    exit()

if age < 6:
    priority = 1
elif age >= 80:
    priority = 2
else: 
    priority = 3

if priority == 1:
    text_priority = "ƯU TIÊN: Bệnh nhi - Chuyển thẳng phòng khám Nhi."
elif priority == 2:
    text_priority = "ƯU TIÊN: Người cao tuổi - Hỗ trợ xe lăn, chuyển phòng khám Lão khoa."
elif priority == 3:
    text_priority = "KHÁM THƯỜNG: Vui lòng lấy số thứ tự và chờ tới lượt tại sảnh."

print(f"""
------ PHIẾU KHÁM BỆNH ------
Tên: {full_name}
Tuổi: {age}
Kết quả phân luồng: {text_priority}
""")