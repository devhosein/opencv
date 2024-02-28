import customtkinter as tk
import cv2
import os
import subprocess
from PIL import Image, ImageTk

tk.set_appearance_mode("Dark")
tk.set_default_color_theme("dark-blue")

root = tk.CTk()
root.geometry("800x450")

# تابع برای به‌روزرسانی تصویر دوربین در ویجت
def update_camera_image():
    ret, frame = cap.read()
    if ret:
        # تغییر اندازه تصویر برای نمایش در ویجت
        frame = cv2.resize(frame, (200, 150))
        # تبدیل تصویر cv2 به تصویر PIL
        cv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        pil_image = Image.fromarray(cv_image)
        imgtk = ImageTk.PhotoImage(image=pil_image)
        camera_label.imgtk = imgtk
        camera_label.configure(image=imgtk)
        camera_label.lift() # اوردن به عنوان تصویر رو
        # تنظیم تایمر برای به‌روزرسانی مجدد تصویر
        camera_label.after(10, update_camera_image)
        

# ایجاد ویجت برای نمایش تصویر دوربین
camera_label = tk.CTkLabel(root)
camera_label.place(x=650, y=10)  # می‌توانید موقعیت x و y را تغییر دهید تا با طراحی شما مطابقت داشته باشد

# ایجاد ویجت برای نمایش تصویر دوربین
camera_label = tk.CTkLabel(root, text="")  # حذف متن پیش‌فرض با قرار دادن یک رشته خالی
camera_label.place(x=600, y=300)  # تنظیم موقعیت ویجت در پایین سمت راست


# شروع دوربین
cap = cv2.VideoCapture(0)
update_camera_image()



# تابع برای گرفتن عکس از دوربین وب
def capture_image():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture image")
            break
        
        height, width, _ = frame.shape
        # محاسبه مرکز تصویر
        center_x, center_y = width // 2, height // 2
        # اندازه مربع
        square_size = min(width, height) // 2
        # تعیین نقاط بالا سمت چپ و پایین سمت راست مربع
        top_left = (center_x - square_size // 2, center_y - square_size // 2)
        bottom_right = (center_x + square_size // 2, center_y + square_size // 2)
        cv2.rectangle(frame, top_left, bottom_right, (0, 0, 255), 2)
        
        # اضافه کردن متن به تصویر
        text_position = (int(width / 6), int(height / 4) - 40)
        cv2.putText(frame, "Place your face within the red square", text_position, cv2.FONT_HERSHEY_SIMPLEX, 0.8, (225, 0, 0), 2)
        text_position = (int(width / 4), int(height / 4) - 10)
        cv2.putText(frame, "press space to take photo", text_position, cv2.FONT_HERSHEY_SIMPLEX, 0.8, (225, 0, 0), 2)
        
        
        # نمایش پیش‌نمایش تصویر
        cv2.imshow("Capture", frame)
        
        # بررسی برای کلید اسپیس
        if cv2.waitKey(1) == 32: # 32 کد ASCII برای کلید اسپیس است
            # ذخیره تصویر در مسیر فایل پایتون اصلی
            current_path = os.path.dirname(os.path.abspath(__file__))
            image_path = os.path.join(current_path, "image (1).jpg")
            cv2.imwrite(image_path, frame)
            print(f"Image captured and saved as '{image_path}'")
            break

    cap.release()
    cv2.destroyAllWindows()

# تابع برای اجرای کد پایتون دیگر
def run_another_script():
    # مسیر فایل اسکریپت دیگر
    script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Face_comparison.py")
    # بستن پنجره رابط کاربری
    root.destroy()
    # اجرای اسکریپت
    subprocess.run(["python", script_path], check=True)
    
    process = subprocess.Popen(["C:\\Program Files\\Python312\\python.exe", "A:\\Python\\MY_projects\\opencv\\conected codes\\sc1.py"], stdout=subprocess.PIPE)
    while True:
        output = process.stdout.read(1)
        if output == b"" and process.poll() is not None:
            break
        if output:
            print(output.decode(), end="")


frame = tk.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

labe0 = tk.CTkLabel(master=frame, text="Wellcom to BALOO Application", font=("Roboto", 35))
labe0.pack(pady=12, padx=10)


label = tk.CTkLabel(master=frame, text="Take the default picture for image processing", font=("Roboto", 22))
label.pack(pady=12, padx=10)

capture_image_button = tk.CTkButton(master=frame, text="Capture Image", command=capture_image)
capture_image_button.pack(pady=35, padx=18)

# متن قبل از دکمه
instruction_label = tk.CTkLabel(master=frame, text="Run the image processing code", font=("Roboto", 22))
instruction_label.pack(pady=12, padx=10)

# دکمه برای اجرای اسکریپت دیگر
run_script_button = tk.CTkButton(master=frame, text="Image processing", command=run_another_script)
run_script_button.pack(pady=35, padx=18)

root.mainloop()










