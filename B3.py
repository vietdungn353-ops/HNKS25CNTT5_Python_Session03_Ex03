# Input: Mã nhân viên, Họ và tên nhân viên, Phòng ban công tác
# Output: In ra phiếu Hồ Sơ Điện Tử với các thông tin ở trên
# Giải pháp: 
#   - Tạo ra một biến đếm số người để làm hồ sơ.
#   - Sử dụng for hoặc while để chạy bước thu thập thông tin 
#   người dùng.
#   - Sử dụng if else để lọc ra các trường hợp dữ liệu bị bỏ trống
#   hoặc để khoảng trắng và hiện ra thống báo
#   - In phiếu gọn gàng, đẹp mắt
# Mô ta luồng: 
#   - Khi bắt đầu sẽ hiện thị thông báo nhập thông tin của người
#   thứ nhất. Khi người dùng nhập xong trường đầu tiên: nếu có bỏ 
#   trống hoặc để khoảng trắng thì cần phải in ra cảnh báo ngay 
#   cho người dùng và cho người dùng nhập lại trường đó. Làm
#   tương tự với 2 người còn lại đến khi nào hết 3 người thì dừng
#   chương trình

for user in range(3):
    id_employees = input("Hãy nhập mã nhân viên: ")
    while id_employees.strip() == "":
        print("[CẢNH BÁO] Dữ liệu tên hoặc mã không hợp lệ! Hủy bỏ tạo hồ sơ cho nhân viên này.")
        id_employees = input("Hãy nhập mã nhân viên: ")

    name_employees = input("Hãy nhập tên nhân viên: ")
    while name_employees.strip() == "":
        print("[CẢNH BÁO] Dữ liệu tên hoặc mã không hợp lệ! Hủy bỏ tạo hồ sơ cho nhân viên này.")
        name_employees = input("Hãy nhập tên nhân viên: ")

    room_management = input("Hãy nhập phòng quản lý: ")
    while room_management.strip() == "":
        print("[CẢNH BÁO] Dữ liệu phòng quản lý không hợp lệ! Hủy bỏ tạo hồ sơ cho nhân viên này.")
        room_management = input("Hãy nhập phòng quản lý: ")
    
    print(f"""
    -------- HỒ SƠ ĐIỆN TỬ -------
    Mã nhân viên: {id_employees}
    Tên nhân viên: {name_employees}
    Phòng ban công tác: {room_management}
    """)