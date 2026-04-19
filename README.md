## PHẦN 1: THÔNG TIN SINH VIÊN
* **Họ và tên:** : Hồ Quốc Uy
* **Họ và tên:** : Vũ Bình Minh
* **Họ và tên:** : Hoàng Mạnh Cương
* **Lớp:** CNTT4.K25
* **Đề tài:** Hệ thống đăng nhập bằng nhận diện khuôn mặt thời gian thực.
* **Công nghệ sử dụng:** `Python`, `OpenCV`, `Face_Recognition`, `MySQL (XAMPP)`.


## PHẦN 2: HƯỚNG DẪN CÀI ĐẶT & THỰC NGHIỆM

### 1. Chuẩn bị môi trường hệ thống
Để chạy được các thư viện cần cài đặt các công cụ biên dịch:
* **CMake**: Hỗ trợ biên dịch mã nguồn xử lý khuôn mặt.
* **Visual Studio C++ Desktop Development**: Cung cấp trình biên dịch cho thư viện `Dlib`.

### 2. Cài đặt thư viện Python
Mở **Terminal/CMD** tại thư mục dự án và thực hiện lệnh cài đặt tự động:
```bash
pip install -r requirements.txt
```

### 3. Thiết lập Cơ sở dữ liệu (MySQL)
1. Khởi động **Apache** và **MySQL** từ bảng điều khiển XAMPP.
2. Truy cập `localhost/phpmyadmin` và tạo database mới tên là: `employee_management`.
3. Chọn thẻ **Import**, tìm đến file `employee_management.sql` để khởi tạo dữ liệu.
4. Cấu hình thông số kết nối tại file `credentials.py` cho khớp với máy cá nhân.

### 4. Khởi chạy chương trình
Thực hiện lệnh sau để bắt đầu hệ thống:
```bash
python main.py
```

## PHẦN 3: HƯỚNG DẪN VẬN HÀNH CHI TIẾT

Để chương trình hoạt động chính xác, người dùng thực hiện theo **04 bước** sau:

* **Bước 1 (Đăng ký):** Tại màn hình chính, bấm nút **Đăng ký**. Nhập tài khoản Admin: `admin` và mật khẩu: `123456` để truy cập quyền quản trị.
* **Bước 2 (Nhập liệu):** Tiến hành nhập đầy đủ thông tin nhân sự (Tên, Họ, SĐT, Email...). Sau khi nhấn lưu, hệ thống sẽ cấp một số **ID** tương ứng cho người đó.
* **Bước 3 (Nạp dữ liệu ảnh):** Đưa ảnh chân dung nhân viên vào thư mục `Images`, tiến hành **đổi tên file ảnh thành đúng số ID** vừa được cấp (Ví dụ: `1001.jpg`, `1002.png`).
* **Bước 4 (Đăng nhập):** Quay lại màn hình chính, bấm nút **Đăng nhập**. Hệ thống tự động nhận diện khuôn mặt, đối soát mã ID và hiển thị thông báo thành công.


## PHẦN 4: CÁC TÍNH NĂNG NỔI BẬT

1. **Nhận diện AI chính xác:** Sử dụng thuật toán HOG và Deep Learning trích xuất đặc trưng khuôn mặt 128 chiều, đảm bảo độ chính xác ngay cả khi thay đổi góc nhìn.
2. **Tương tác giọng nói tự động:** Tích hợp đa tiến trình (`Multiprocessing`) để phát giọng nói hướng dẫn ("Mời đưa mặt vào camera", "Đăng nhập thành công") cực kỳ mượt mà.
3. **Xử lý dữ liệu thời gian thực:** Tự động truy vấn MySQL để hiển thị **Họ tên nhân viên** và **Thời gian vào làm** ngay trên giao diện sau khi nhận diện.
4. **Giao diện người dùng (GUI) chuyên nghiệp:** Thiết kế bằng thư viện `Tkinter` với bố cục khoa học, phân chia rõ ràng giữa luồng Camera và bảng điều khiển.
5. **Hệ thống quản trị bảo mật:** Khu vực Admin được bảo vệ chặt chẽ, đảm bảo chỉ người có thẩm quyền mới có thể đăng ký nhân viên mới.


## CÁC HÌNH MINH HỌA SƠ BỘ VỀ HỆ THỐNG

<img width="975" height="637" alt="3mat" src="https://github.com/user-attachments/assets/0f5b6372-bc7d-4e40-a970-b42e3db3386d" />

<img width="970" height="635" alt="2mat" src="https://github.com/user-attachments/assets/f3736299-065f-467d-8568-838eba802653" />

<img width="975" height="633" alt="1mat" src="https://github.com/user-attachments/assets/9666d561-6ae0-4431-85db-79a8fb02efe3" />




