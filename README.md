PHẦN 1: THÔNG TIN SINH VIÊN
Họ và tên:

Lớp: [Điền Tên Lớp]
Đề tài:Hệ thống đang nhập bằng nhận diện khuôn mặt
Công nghệ:Python, OpenCV, Face_Recognition, MySQL (XAMPP).


PHẦN 2: HƯỚNG DẪN CÀI ĐẶT & THỰC NGHIỆM

### 1. Chuẩn bị môi trường hệ thống
Để chạy được thư viện AI, máy tính cần cài đặt các công cụ biên dịch sau:
* **CMake**: Hỗ trợ biên dịch mã nguồn mã hóa khuôn mặt.
* **Visual Studio C++ Desktop Development**: Cung cấp trình biên dịch C++ cho thư viện Dlib.

### 2. Cài đặt thư viện Python
Mở Terminal/CMD tại thư mục dự án và thực hiện lệnh cài đặt tự động từ file requirements:
```bash
pip install -r requirements.txt
```

### 3. Thiết lập Cơ sở dữ liệu (MySQL)
1. Khởi động **Apache** và **MySQL** từ bảng điều khiển XAMPP.
2. Truy cập `localhost/phpmyadmin` và tạo database mới tên là "employee_management".
3. Chọn thẻ **Import**, tìm đến file `employee_management.sql` trong thư mục dự án để khởi tạo cấu trúc bảng dữ liệu.
4. Cấu hình thông số (User/Password) tại file `credentials.py` cho khớp với cấu hình máy cá nhân.

### 4. Khởi chạy chương trình
Thực hiện lệnh sau để bắt đầu hệ thống:
```bash
python main.py
```

PHẦN 3: HƯỚNG DẪN VẬN HÀNH
    Quy trình sử dụng hệ thống
Để chương trình hoạt động chính xác, người dùng thực hiện theo các bước sau:

Bước 1 (Đăng ký): Tại màn hình chính, bấm nút Đăng ký. Nhập tài khoản mặc định của Admin là 'admin' và mật khẩu là '123456' để truy cập quyền quản trị.

Bước 2 (Nhập liệu): Tiến hành nhập đầy đủ thông tin nhân sự (Tên, Họ, SĐT, Email...). Sau khi lưu, hệ thống sẽ cấp một số ID tương ứng cho người đó.

Bước 3 (Nạp dữ liệu ảnh): Đưa ảnh chân dung của nhân viên vào mục thư mục Images, tiến hành đổi tên file ảnh thành số ID vừa được cấp (Ví dụ: 1001.jpg, 1002.png).

Bước 4 (Đăng nhập): Quay lại màn hình chính, bấm nút Đăng nhập. Hệ thống sẽ tự động nhận diện khuôn mặt từ Camera, đối soát với mã ID, hiển thị tên và báo danh thành công.


PHẦN 4: CÁC TÍNH NĂNG NỔI BẬT

Nhận diện AI chính xác: Sử dụng thuật toán HOG và Deep Learning trích xuất đặc trưng khuôn mặt 128 chiều, đảm bảo nhận diện chính xác ngay cả khi thay đổi góc nhìn hoặc điều kiện ánh sáng.
Tương tác giọng nói tự động: Tích hợp công nghệ đa tiến trình (Multiprocessing) để phát âm thanh chỉ dẫn hướng dẫn người dùng ("Mời đưa mặt vào camera", "Đăng nhập thành công") mà không làm giật lag giao diện.
Xử lý dữ liệu thời gian thực: Hệ thống tự động truy vấn dữ liệu từ MySQL để hiển thị chính xác **Họ tên nhân viên** và **Thời gian đăng nhập** ngay trên màn hình kết quả sau khi nhận diện thành công.
Giao diện người dùng (GUI) chuyên nghiệp:Thiết kế bằng thư viện Tkinter với bố cục khoa học, phân chia rõ ràng giữa luồng Camera giám sát và bảng điều khiển chức năng.
Hệ thống quản trị bảo mật: Tích hợp khu vực Admin (đăng nhập bằng tài khoản/mật khẩu) để quản lý việc đăng ký thông tin cá nhân và mã hóa khuôn mặt cho nhân viên mới vào hệ thống.


CÁC HÌNH MINH HỌA SƠ BỘ VỀ HỆ THỐNG
<img width="972" height="633" alt="Screenshot 2026-04-16 214457" src="https://github.com/user-attachments/assets/74e157dd-4d0a-4ee4-8b35-35c614839e28" />

<img width="970" height="635" alt="2mat" src="https://github.com/user-attachments/assets/f3736299-065f-467d-8568-838eba802653" />

<img width="975" height="633" alt="1mat" src="https://github.com/user-attachments/assets/9666d561-6ae0-4431-85db-79a8fb02efe3" />




