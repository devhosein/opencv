import customtkinter as tk
import cv2
import os
import subprocess
import pygame


dirname = os.path.dirname(__file__)
pygame.mixer.init()
filename0 = os.path.join(dirname ,"main_music.mp3")
sound = pygame.mixer.Sound(filename0) 
sound.play()

tk.set_appearance_mode("Dark")
tk.set_default_color_theme("dark-blue")

root = tk.CTk()
root.geometry("800x450")

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
