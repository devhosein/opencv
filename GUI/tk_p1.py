# #https://www.youtube.com/watch?v=iM3kjbbKHQU
# import customtkinter as tk



# tk.set_appearance_mode("Dark")
# tk.set_default_color_theme("dark-blue")

# root = tk.CTk()
# root.geometry("500x350")

# def login():
#     print("test")

# frame = tk.CTkFrame(master=root)
# frame.pack(pady=20, padx=60, fill="both", expand=True)


# label = tk.CTkLabel(master=frame, text= "login system", font= ("Roboto", 24) )
# label.pack(pady= 12, padx=10)



# root.mainloop()




import customtkinter as tk
import cv2

tk.set_appearance_mode("Dark")
tk.set_default_color_theme("dark-blue")

root = tk.CTk()
root.geometry("500x350")

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
            # ذخیره تصویر
            cv2.imwrite("captured_image.jpg", frame)
            print("Image captured and saved as 'captured_image.jpg'")
            break

    cap.release()
    cv2.destroyAllWindows()

frame = tk.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = tk.CTkLabel(master=frame, text="login system", font=("Roboto", 24))
label.pack(pady=12, padx=10)

capture_image_button = tk.CTkButton(master=frame, text="Capture Image", command=capture_image)
capture_image_button.pack(pady=12, padx=10)

root.mainloop()

