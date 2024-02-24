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
