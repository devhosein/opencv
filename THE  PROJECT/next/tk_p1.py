import customtkinter as tk
import cv2
import os
import subprocess
import time
import threading
import face_recognition
from PIL import Image, ImageTk
import random
from tkinter.scrolledtext import ScrolledText
import sys

dirname = os.path.dirname(__file__)
zero = True

# متغیر بولین برای کنترل حلقه‌ها
running = True

tk.set_appearance_mode("Dark")
tk.set_default_color_theme("dark-blue")

root = tk.CTk()
root.geometry("1000x600")
root.title("image prossing program")

x =""

####----
# تابع برای به‌روزرسانی تصویر دوربین در ویجت
def update_camera_image():
    global image2
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
        
        # # تصویر ذخیره شده توسط کمرا
        # dirname = os.path.dirname(__file__)
        # filename4 = os.path.join(dirname, "frame.png")
        # image2 = face_recognition.load_image_file(filename4)


        

# ایجاد ویجت برای نمایش تصویر دوربین
camera_label = tk.CTkLabel(root)
camera_label.place(x=650, y=10)  # می‌توانید موقعیت x و y را تغییر دهید تا با طراحی شما مطابقت داشته باشد

# ایجاد ویجت برای نمایش تصویر دوربین
camera_label = tk.CTkLabel(root, text="")  # حذف متن پیش‌فرض با قرار دادن یک رشته خالی
camera_label.place(x=800, y=450)  # تنظیم موقعیت ویجت در پایین سمت راست


# شروع دوربین
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# update_camera_image()
thread = threading.Thread(target=update_camera_image)
thread.daemon = True  # این باعث می‌شود که thread با بسته شدن برنامه خاتمه یابد
thread.start()
####----


####----
# تابع برای گرفتن عکس از دوربین وب
def capture_image():
    global cap
    # cap = cv2.VideoCapture(0)
    global running
    while running:
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
        

    # cap.release()
    cv2.destroyAllWindows()
####----


#######-------
# main code 
def run_another_script():
    global cap, zero ,x, image2, running

    dirname = os.path.dirname(__file__)

    # دادن ایکس ام ال به اوپن سیوی
    filename = os.path.join(dirname, "haarcascade_frontalface_default.xml")
    face_cascade = cv2.CascadeClassifier(filename)

    # یکی از متغییر های لازم برای ذخیره ی عکس 
    bool_avalin_tashkhis_face = False

    # وایل مدام اجرا شدن سیستم تشخیص چهره
    while running:
        
        # جهت بستن تصویر نمایش داده شده
        if cv2.waitKey(1) & 0xFF == ord("q"):
            running = False
            break

        # تشخیص چهره توسط اوپن سی وی 
        _, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1 , 8)
        # face_for_eye = face_eye.detectMultiScale(gray, 1.1, 8)

        # گرفتن عکس و ذخیره کردن عکس پشت سر هم ... 
        if len(faces) > 0:
            bool_avalin_tashkhis_face = True
            
        if bool_avalin_tashkhis_face == True:
            result, img = cap.read()
            filename2 = os.path.join(dirname, "frame.png")
            if result:
                cv2.imwrite(filename2, img)
                
        # مقایسه دو چهره
    #-------------------------------------------------------------------------------------------------------------
        # بارگذاری تصاویر چهره ها
        filename3 = os.path.join(dirname, "image (1).jpg")
        image1 = face_recognition.load_image_file(filename3)
        # تصویر ذخیره شده توسط کمرا
        filename4 = os.path.join(dirname, "frame.png")
        image2 = face_recognition.load_image_file(filename4)


        try:
        # استخراج ویژگی‌های چهره‌ها
            face_encoding1 = face_recognition.face_encodings(image1)[0]
        
        
        # جلو گیری از ارور وجود نداشتن عکس و خراب بودن عکس
            try:
                # گرفتن ویژگی های تصویر کمرا
                face_encoding_camera = face_recognition.face_encodings(image2)[0]
            
                # چقدر چهره ها لازمه مثل هم باشن ؟؟
                results = face_recognition.compare_faces([face_encoding1], face_encoding_camera, tolerance=0.5)
                # شبیه بود
                if results[0]:
                    x = ("same")
                    x = ("hello boss, very nice to meet you \n")

                # یکی دیگه بود
                else:
                    x = ("diffrent")
                    x = ("go away !! \n")
            # تصویر نیست و یا خرابه
            except:
                x = ("We do not have the face or The face is not clear !!")
            
        except:
            x = ("the diffalt picture is very bad")
    #--------------------------------------------------------------------------------------------------------------
        print(x)
        # output_def()
        
        if zero:
            label12 = tk.CTkLabel(master=frame, text=x, font=("Roboto", 22))
            label12.pack(pady=12, padx=10)
            zero = False
        else:
            label12.configure(text=x)
        
        # خوابوندن تایم برای اینکه سیستم اذیت نشه یه وقت !!
        time.sleep(2)

    
    
    # cap.release()
######------
    
    
##-------------------------------------------------------------------------------------------
# پنجره ی ساخت اکانت جدید
def save_data():
    # این تابع مقادیر ورودی را در متغیرهای جهانی ذخیره می‌کند
    global user_text, user_number ,text_entry ,number_entry, new_window
    user_text = text_entry.get()
    user_number = number_entry.get()
    print("متن ذخیره شده:", user_text)
    print("عدد ذخیره شده:", user_number)
    #بستن پنجره جدید
    new_window.destroy()
    # عکس گرفتن
    capture_image()


def create_new_window():
    global user_text, user_number ,text_entry ,number_entry , new_window
    new_window = tk.CTkToplevel()
    new_window.title("new win")
    new_window.geometry("600x450")  # اندازه پنجره جدید را تنظیم می‌کند
    new_window.grab_set()  # این خط باعث می‌شود که پنجره جدید تمرکز کاربر را به خود جلب کند
    new_window.focus_set()  # این خط پنجره جدید را در مرکز توجه قرار می‌دهد
    tk.CTkLabel(new_window, text="this is a new win", font=("Roboto", 22)).pack(pady=12, padx=10)
    
    
    label = tk.CTkLabel(new_window, text="creat new acount", font=("Roboto", 22))
    label.pack(pady=12, padx=10)

    # ایجاد ویجت ورودی برای متن
    text_entry = tk.CTkEntry(new_window, placeholder_text="enter your name:", font=("Roboto", 22))
    text_entry.pack(pady=12, padx=10)

    # ایجاد ویجت ورودی برای عدد
    number_entry = tk.CTkEntry(new_window, placeholder_text="enter text:",font=("Roboto", 22))
    number_entry.pack(pady=12, padx=10)

    # ایجاد دکمه برای ذخیره‌سازی داده‌ها
    save_button = tk.CTkButton(new_window, text="save and take the photo",font=("Roboto", 22), command=save_data)
    save_button.pack(pady=12, padx=10)
    

# new_acuont = tk.CTkButton(root, text="open a new win", command=create_new_window)
# new_acuont.pack(pady= 35, padx = 18 )

##----------------------------------------------------------------------------------------------------




####----
# محیط گرافیکی    
frame = tk.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

labe0 = tk.CTkLabel(master=frame, text="Wellcom to BALOO Application", font=("Roboto", 35))
labe0.pack(pady=12, padx=10)


label = tk.CTkLabel(master=frame, text="press botton to creat new acount", font=("Roboto", 22))
label.pack(pady=12, padx=10)

# capture_image_button = tk.CTkButton(master=frame, text="Capture Image", command=capture_image)
# capture_image_button.pack(pady=35, padx=18)

new_acuont = tk.CTkButton(master=frame, text="open a new win", command=create_new_window)
new_acuont.pack(pady= 35, padx = 18 )


# متن قبل از دکمه
instruction_label = tk.CTkLabel(master=frame, text="Run the image processing code", font=("Roboto", 22))
instruction_label.pack(pady=12, padx=10)



def stop_another_script():
    global running
    running = False # این مقدار را به False تغییر دهید
    # print("kdfjaskdkjfl;ajd;lkasfjlkasjdfl;kasjfl;kasjdf;fka")
    root.destroy()
    

# ایجاد یک نخ برای اسکریپت دیگر
thread = threading.Thread(target=run_another_script)


# دکمه برای اجرای اسکریپت دیگر
run_script_button = tk.CTkButton(master=frame, text="Run script", command=thread.start)
run_script_button.pack(pady=35, padx=18)

# دکمه برای توقف اسکریپت دیگر
stop_script_button = tk.CTkButton(master=frame, text="Stop script", command=stop_another_script)
stop_script_button.pack(pady=35, padx=18)
####-----



# run
root.mainloop()