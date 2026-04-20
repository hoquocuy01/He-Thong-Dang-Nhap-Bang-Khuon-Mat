import cv2
import time
import pymysql
import numpy as np
from tkinter import *
import settings as st
import credentials as cr
import face_recognition as f
import videoStream as vs
import multiprocessing as mp
from datetime import datetime
from tkinter import messagebox
from playsound import playsound

# Lớp Hệ thống Đăng nhập
class LoginSystem:
    def __init__(self, root):
        # Cấu hình cửa sổ
        self.window = root
        self.window.title("Hệ Thống Đăng Nhập Khuôn Mặt")
        self.window.geometry("780x480")
        self.window.config(bg=st.color1)
        self.window.resizable(width = False, height = False)

        # Biến trạng thái
        self.status = False
        self.logged_in_name = "" # Biến lưu tên người đăng nhập

        # Frame bên trái (Hiển thị nội dung chính)
        self.frame1 = Frame(self.window, bg=st.color1)
        self.frame1.place(x=0, y=0, width=540, relheight = 1)

        # Frame bên phải (Thanh menu nút bấm)
        self.frame2 = Frame(self.window, bg = st.color2)
        self.frame2.place(x=540,y=0,relwidth=1, relheight=1)

        self.buttons()

    def buttons(self):
        loginButton = Button(self.frame2, text="Đăng Nhập", font=(st.font3, 12), bd=2, cursor="hand2", width=12, command=self.loginEmployee)
        loginButton.place(x=45, y=40)

        registerButton = Button(self.frame2, text="Đăng Ký", font=(st.font3, 12), bd=2, cursor="hand2", width=12, command=self.adminPanel)
        registerButton.place(x=45, y=100)

        clearButton = Button(self.frame2, text="Xóa Màn Hình", font=(st.font3, 12), bd=2, cursor="hand2", width=12, command=self.clearScreen)
        clearButton.place(x=45, y=160)

        exitButton = Button(self.frame2, text="Thoát", font=(st.font3, 12), bd=2, cursor="hand2", width=12, command=self.exit)
        exitButton.place(x=45, y=220)

    def loginEmployee(self):
        self.clearScreen()
        self.logged_in_name = "Unknown" 

        # Phát âm thanh chào mừng (Chạy ngầm, không chặn luồng chính)
        self.playVoice("Voices/voice1.mp3")
        
        # Không dùng time.sleep và terminate ở đây nữa để tránh ngắt giọng
        # Hệ thống sẽ bắt đầu nạp dữ liệu khuôn mặt ngay khi tiếng nói đang phát
        
        faces = vs.encode_faces()
        encoded_faces = list(faces.values())
        faces_name = list(faces.keys())
        video_frame = True

        video_stream = vs.VideoStream(stream=0)
        video_stream.start()

        while True:
            if video_stream.stopped is True:
                break
            else :
                frame = video_stream.read()
                if video_frame:
                    face_locations = f.face_locations(frame)
                    unknown_face_encodings = f.face_encodings(frame, face_locations)

                    face_names = []
                    for face_encoding in unknown_face_encodings:
                        matches = f.compare_faces(encoded_faces, face_encoding)
                        name = "Unknown"
                        face_distances = f.face_distance(encoded_faces, face_encoding)
                        best_match_index = np.argmin(face_distances)
                        if matches[best_match_index]:
                            name = faces_name[best_match_index]
                        face_names.append(name)

                video_frame = not video_frame

                for (top, right, bottom, left), faceID in zip(face_locations, face_names):
                    cv2.rectangle(frame, (left-20, top-20), (right+20, bottom+20), (0, 255, 0), 2)
                    cv2.putText(frame, "Da Phat Hien", (left -20, bottom + 15), cv2.FONT_HERSHEY_DUPLEX, 0.85, (255, 255, 255), 2)
                    self.status, self.logged_in_name = self.isPresent(faceID)

            cv2.imshow('Nhan Dien Khuon Mat - Nhan Q de thoat' , frame)
            if cv2.waitKey(1) & 0xFF == ord('q') or self.status == True:
                break

        video_stream.stop()
        cv2.destroyAllWindows()

        if self.status:
            # Phát âm thanh thông báo thành công
            self.playVoice("Voices/voice2.mp3")
            # Chuyển màn hình kết quả
            self.employeeEntered(self.logged_in_name) 
        else:
            self.clearScreen()

    def playVoice(self, voice):
        # Tạo một tiến trình riêng để chạy playsound
        # Tiến trình này sẽ tự kết thúc khi file âm thanh chạy hết
        process = mp.Process(target=playsound, args=(voice,))
        process.daemon = True # Đảm bảo âm thanh tắt nếu bạn đóng ứng dụng chính
        process.start()
        # Không return process để tránh việc gọi terminate nhầm lẫn ở nơi khác

    def isPresent(self, UID):
        try:
            connection = pymysql.connect(host=cr.host, user=cr.username, password=cr.password, database=cr.database)
            curs = connection.cursor()
            # Lấy Họ và Tên từ database
            curs.execute("select f_name, l_name from employee_register where uid=%s", UID)
            row = curs.fetchone()
            connection.close()

            if row == None:
                return False, "Unknown"
            else:
                full_name = f"{row[0]} {row[1]}" # Ghép Họ + Tên
                return True, full_name
        except Exception as e:
            return False, "Error"

    def employeeEntered(self, name):
        self.clearScreen()
        self.status = False

        heading = Label(self.frame1, text="KẾT QUẢ ĐĂNG NHẬP", font=(st.font4, 25, "bold"), bg=st.color1, fg=st.color3)
        heading.place(x=100, y=30)
        
        # HIỂN THỊ TÊN NGƯỜI DÙNG
        userLabel = Label(self.frame1, text=f"Xin chào: {name}", font=(st.font1, 20, "bold"), bg=st.color1, fg="#1e3a8a")
        userLabel.place(x=40, y=100)

        now = datetime.now().strftime("%H:%M:%S - %d/%m/%Y")

        label1 = Label(self.frame1, text="Thời gian vào:", font=(st.font1, 18, "bold"), bg=st.color1, fg=st.color3)
        label1.place(x=40, y=160)

        timeLabel = Label(self.frame1, text=now, font=(st.font1, 16), bg=st.color1, fg=st.color3)
        timeLabel.place(x=210, y=163)

        successLabel = Label(self.frame1, text="Đăng nhập thành công!", font=(st.font1, 18, "bold"), bg=st.color1, fg="green")
        successLabel.place(x=40, y=220)

    def playVoice(self, voice):
        process = mp.Process(target=playsound, args=(voice,))
        process.start()
        return process

    def clearScreen(self):
        for widget in self.frame1.winfo_children():
            widget.destroy()

    def exit(self):
        if messagebox.askyesno("Thoát", "Bạn có chắc chắn muốn đóng ứng dụng?"):
            self.window.destroy()

    # Các hàm Admin giữ nguyên...
    def adminPanel(self):
        self.clearScreen()
        heading = Label(self.frame1, text="QUẢN TRỊ VIÊN", font=(st.font4, 30, "bold"), bg=st.color1, fg=st.color3)
        heading.place(x=140, y=30)
        usernameLabel = Label(self.frame1, text="Tài khoản", font=(st.font1, 18), bg=st.color1, fg=st.color3)
        usernameLabel.place(x=40, y=120)
        self.userName = Entry(self.frame1, font=(st.font2, 15), width=20, bg=st.color4, fg=st.color1)
        self.userName.place(x=180, y=123)
        passwordLabel = Label(self.frame1, text="Mật khẩu", font=(st.font1, 18), bg=st.color1, fg=st.color3)
        passwordLabel.place(x=40, y=180)
        self.password = Entry(self.frame1, show="*", font=(st.font2, 15), width=20, bg=st.color4, fg=st.color1)
        self.password.place(x=180, y=183)
        loginButton = Button(self.frame1, text="Xác nhận", font=(st.font3, 12), bd=2, cursor="hand2", width=10, bg=st.color5, fg=st.color1, command=self.loginAdmin)
        loginButton.place(x=220, y=240)

    def loginAdmin(self):
        if self.userName.get() == "" or self.password.get() == "":
            messagebox.showerror("Thiếu thông tin", "Vui lòng nhập đầy đủ Tài khoản và Mật khẩu")
        else:
            try:
                connection = pymysql.connect(host=cr.host, user=cr.username, password=cr.password, database=cr.database)
                curs = connection.cursor()
                curs.execute("select * from admin where username=%s and password=%s", (self.userName.get(), self.password.get()))
                row=curs.fetchone()
                if row == None:
                    messagebox.showerror("Thất bại", "Tài khoản hoặc mật khẩu không đúng!", parent=self.window)
                else:
                    self.registerPage()
                    connection.close()
            except Exception as e:
                messagebox.showerror("Lỗi", f"Lỗi hệ thống: {str(e)}", parent=self.window)

    def registerPage(self):
        self.clearScreen()
        Label(self.frame1, text="Tên", font=(st.font2, 15, "bold"), bg=st.color1).place(x=40,y=30)
        self.nameEntry = Entry(self.frame1, bg=st.color4, fg=st.color1, font=(st.font2, 15))
        self.nameEntry.place(x=40,y=60, width=200)
        Label(self.frame1, text="Họ", font=(st.font2, 15, "bold"), bg=st.color1).place(x=300,y=30)
        self.surnameEntry = Entry(self.frame1, bg=st.color4, fg=st.color1, font=(st.font2, 15))
        self.surnameEntry.place(x=300,y=60, width=200)
        row = self.getUID()
        current_uid = 1000 if (row is None or row[0] is None) else row[0] + 1
        Label(self.frame1, text="Mã Nhân Viên*", font=(st.font2, 15, "bold"), bg=st.color1).place(x=40,y=100)
        self.uidLabel = Label(self.frame1, text=f"{current_uid}", bg=st.color1, fg=st.color3, font=(st.font2, 15))
        self.uidLabel.place(x=40,y=130)
        Label(self.frame1, text="Email", font=(st.font2, 15, "bold"), bg=st.color1).place(x=300,y=100)
        self.emailEntry = Entry(self.frame1, bg=st.color4, fg=st.color1, font=(st.font2, 15))
        self.emailEntry.place(x=300,y=130, width=200)
        Label(self.frame1, text="Chức vụ", font=(st.font2, 15, "bold"), bg=st.color1).place(x=40,y=170)
        self.designationEntry = Entry(self.frame1, bg=st.color4, fg=st.color1, font=(st.font2, 15))
        self.designationEntry.place(x=40,y=200, width=200)
        Label(self.frame1, text="Số điện thoại", font=(st.font2, 15, "bold"), bg=st.color1).place(x=300,y=170)
        self.contactEntry = Entry(self.frame1, bg=st.color4, fg=st.color1, font=(st.font2, 15))
        self.contactEntry.place(x=300,y=200, width=200)
        Label(self.frame1, text="Ngày sinh", font=(st.font2, 15, "bold"), bg=st.color1).place(x=40,y=240)
        self.dobEntry = Entry(self.frame1, bg=st.color4, fg=st.color1, font=(st.font2, 15))
        self.dobEntry.place(x=40,y=270, width=200)
        Label(self.frame1, text="Ngày vào làm", font=(st.font2, 15, "bold"), bg=st.color1).place(x=300,y=240)
        self.joinningDateEntry = Entry(self.frame1, bg=st.color4, fg=st.color1, font=(st.font2, 15))
        self.joinningDateEntry.place(x=300,y=270, width=200)
        Label(self.frame1, text="Giới tính", font=(st.font2, 15, "bold"), bg=st.color1).place(x=40,y=310)
        self.genderEntry = Entry(self.frame1, bg=st.color4, fg=st.color1, font=(st.font2, 15))
        self.genderEntry.place(x=40,y=340, width=200)
        Label(self.frame1, text="Địa chỉ", font=(st.font2, 15, "bold"), bg=st.color1).place(x=300,y=310)
        self.addressEntry = Entry(self.frame1, bg=st.color4, fg=st.color1, font=(st.font2, 15))
        self.addressEntry.place(x=300,y=340, width=200)
        Button(self.frame1, text='Lưu Dữ Liệu', font=(st.font3, 12), bd=2, command=self.submitData, cursor="hand2", bg=st.color5,fg=st.color1).place(x=200,y=389,width=120)

    def getUID(self):
        try:
            connection = pymysql.connect(host=cr.host, user=cr.username, password=cr.password, database=cr.database)
            curs = connection.cursor()
            curs.execute("select MAX(uid) from employee_register")
            row = curs.fetchone()
            connection.close()
            return row
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể lấy mã UID: {str(e)}", parent=self.window)

    def submitData(self):
        if self.nameEntry.get() == "" or self.surnameEntry.get() == "":
            messagebox.showwarning("Chú ý", "Vui lòng nhập đầy đủ Họ và Tên", parent = self.window)
        else:
            try:
                connection = pymysql.connect(host=cr.host, user=cr.username, password=cr.password, database=cr.database)
                curs = connection.cursor()
                curs.execute("insert into employee_register (f_name,l_name,email,designation,contact,dob,join_date,gender,address) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                        (
                                            self.nameEntry.get(),
                                            self.surnameEntry.get(),
                                            self.emailEntry.get(),
                                            self.designationEntry.get(),
                                            self.contactEntry.get(),
                                            self.dobEntry.get(),
                                            self.joinningDateEntry.get(),
                                            self.genderEntry.get(),
                                            self.addressEntry.get() 
                                        ))
                connection.commit()
                connection.close()
                messagebox.showinfo('Thành công', "Dữ liệu nhân viên đã được lưu vào hệ thống")
                self.resetFields()
            except Exception as e:
                messagebox.showerror("Lỗi", f"Không thể lưu dữ liệu: {str(e)}", parent=self.window)

    def resetFields(self):
        self.nameEntry.delete(0, END)
        self.surnameEntry.delete(0, END)
        row = self.getUID()
        self.uidLabel.config(text=f"{row[0] + 1}")
        self.emailEntry.delete(0, END)
        self.designationEntry.delete(0, END)
        self.contactEntry.delete(0, END)
        self.dobEntry.delete(0, END)
        self.joinningDateEntry.delete(0, END)
        self.genderEntry.delete(0, END)
        self.addressEntry.delete(0, END)

if __name__ == "__main__":
    root = Tk()
    obj = LoginSystem(root)
    root.mainloop()