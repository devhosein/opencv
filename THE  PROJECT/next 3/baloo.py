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
import numpy as np
import json

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

# ###----
#  # تابع برای به‌روزرسانی تصویر دوربین در ویجت
# def update_camera_image():
#     global image2
#     ret, frame = cap.read()
#     if ret:
#         # تغییر اندازه تصویر برای نمایش در ویجت
#         frame = cv2.resize(frame, (200, 150))
#         # تبدیل تصویر cv2 به تصویر PIL
#         cv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         pil_image = Image.fromarray(cv_image)
#         imgtk = ImageTk.PhotoImage(image=pil_image)
#         camera_label.imgtk = imgtk
#         camera_label.configure(image=imgtk)
#         camera_label.lift() # اوردن به عنوان تصویر رو
#         # تنظیم تایمر برای به‌روزرسانی مجدد تصویر
#         camera_label.after(10, update_camera_image)
        
#         # # تصویر ذخیره شده توسط کمرا
#         # dirname = os.path.dirname(__file__)
#         # filename4 = os.path.join(dirname, "frame.png")
#         # image2 = face_recognition.load_image_file(filename4)


        

# # ایجاد ویجت برای نمایش تصویر دوربین
# camera_label = tk.CTkLabel(root)
# camera_label.place(x=650, y=10)  # می‌توانید موقعیت x و y را تغییر دهید تا با طراحی شما مطابقت داشته باشد

# # ایجاد ویجت برای نمایش تصویر دوربین
# camera_label = tk.CTkLabel(root, text="")  # حذف متن پیش‌فرض با قرار دادن یک رشته خالی
# camera_label.place(x=800, y=450)  # تنظیم موقعیت ویجت در پایین سمت راست


# # # شروع دوربین
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# # update_camera_image()
# thread = threading.Thread(target=update_camera_image)
# thread.daemon = True  # این باعث می‌شود که thread با بسته شدن برنامه خاتمه یابد
# thread.start()
# ####----


####----
# تابع برای گرفتن عکس از دوربین وب
numn = None
def capture_image():
    global cap , name_text, dirname, numn
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
            
            # مسیر فایل جیسون
            json_file_path = r"A:\Python\MY_projects\opencv\THE  PROJECT\\next 3\\info.json"

            # باز کردن فایل جیسون و تبدیل به دیکشنری
            with open(json_file_path, "r") as json_file:
                data = json.load(json_file)

            # یافتن عدد در آخرین براکت
            last_id = data["accounts"][-1]["id"]

            # افزودن یک به عدد یافته
            numn = last_id + 1

            # ذخیره تصویر در مسیر فایل پایتون اصلی
            current_path = os.path.dirname(os.path.abspath(__file__))
            current_path += "\\accounts\\"
            image_path = os.path.join(current_path, f"{numn}.jpg")
            cv2.imwrite(image_path, frame)
            print(f"Image captured and saved as '{numn}'")
            
            time.sleep(1)
            
            filename_face_accounts = os.path.join(dirname + "\\accounts\\" ,f"{numn}.jpg")
            image1 = face_recognition.load_image_file(filename_face_accounts)
            face_encoding1 = face_recognition.face_encodings(image1)
            face_encoding1 = str(face_encoding1)
            face_encoding1 = face_encoding1.replace("\n", "")
            face_encoding1 = face_encoding1.replace("[array(" , "")
            face_encoding1 = face_encoding1.replace(")]" , "")
            
                
            # json
            dirname = os.path.dirname(__file__)
            filename10 = os.path.join(dirname, "info.json")
            with open (filename10 , "r") as jf:
                d = {
                    "id" : numn,
                    "name" : name_text,
                    "nothing for now" : None,
                    "face code" : face_encoding1
                }
                data = json.load(jf)
            data["accounts"].append(d)
            with open (filename10 , "w") as jf:
                json.dump(data , jf , indent= 3)
            
            
            break
        

    # cap.release()
    cv2.destroyAllWindows()
####----


#######-------
# main code 
def run_another_script():
    global cap, zero ,x, image2, running, name_text
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
        # # بارگذاری تصاویر چهره ها
        # filename3 = os.path.join(dirname + "\\acounts\\", f"{name_text}")
        # image1 = face_recognition.load_image_file(filename3)
        # # تصویر ذخیره شده توسط کمرا
        # filename4 = os.path.join(dirname, "frame.png")
        # image2 = face_recognition.load_image_file(filename4)


        # try:
        # # استخراج ویژگی‌های چهره‌ها
        #     face_encoding1 = face_recognition.face_encodings(image1)[0]
        
        
        # # جلو گیری از ارور وجود نداشتن عکس و خراب بودن عکس
        #     try:
        #         # گرفتن ویژگی های تصویر کمرا
        #         face_encoding_camera = face_recognition.face_encodings(image2)[0]
            
        #         # چقدر چهره ها لازمه مثل هم باشن ؟؟
        #         results = face_recognition.compare_faces([face_encoding1], face_encoding_camera, tolerance=0.5)
        #         # شبیه بود
        #         if results[0]:
        #             x = ("same")
        #             x = ("hello boss, very nice to meet you \n")

        #         # یکی دیگه بود
        #         else:
        #             x = ("diffrent")
        #             x = ("go away !! \n")
        #     # تصویر نیست و یا خرابه
        #     except:
        #         x = ("We do not have the face or The face is not clear !!")
            
        # except:
        #     x = ("the diffalt picture is very bad")
        
        
        
    #     # مسیر تصویر ذخیره شده توسط دوربین
    #     filename4 = os.path.join(dirname, "frame.png")
    #     image2 = face_recognition.load_image_file(filename4)

    #     try:
    #         # استخراج ویژگی‌های چهره‌ها از تصویر دوربین
    #         face_encoding_camera = face_recognition.face_encodings(image2)[0]

    #         # مسیر پوشه حاوی تصاویر حساب‌ها
    #         accounts_folder_path = os.path.join(dirname, "accounts")

    #         # پیمایش تمام فایل‌های تصویر در پوشه 'accounts'
    #         for image_file in os.listdir(accounts_folder_path):
    #             image_path = os.path.join(accounts_folder_path, image_file)
    #             try:
    #                 # بارگذاری تصویر و استخراج ویژگی‌های چهره
    #                 image1 = face_recognition.load_image_file(image_path)
    #                 face_encoding1 = face_recognition.face_encodings(image1)[0]

    #                 # مقایسه چهره‌ها
    #                 results = face_recognition.compare_faces([face_encoding1], face_encoding_camera, tolerance=0.5)

    #                 # بررسی نتایج و چاپ پیام متناسب
    #                 if results[0]:
    #                     x= print(f"{image_file}")
    #                 # else:
    #                 #     x = print(f"")

    #             except IndexError:
    #                 # اگر چهره‌ای در تصویر یافت نشود یا تصویر واضح نباشد
    #                 x =print(f"در تصویر {image_file} چهره‌ای یافت نشد یا چهره واضح نیست.")

    #     except Exception as e:
    #         # چاپ خطا در صورت بروز مشکل
    #         x =print(f"خطایی رخ داده است: {e}")
                
  
    # #--------------------------------------------------------------------------------------------------------------
    #     print(x)
    #     # output_def()
        
    #     if zero:
    #         label12 = tk.CTkLabel(master=frame, text=x, font=("Roboto", 22))
    #         label12.pack(pady=12, padx=10)
    #         zero = False
    #     else:
    #         label12.configure(text=x)
        
    #     # خوابوندن تایم برای اینکه سیستم اذیت نشه یه وقت !!
    #     time.sleep(2)


        # مسیر تصویر ذخیره شده توسط دوربین
        filename4 = os.path.join(dirname, "frame.png")
        image2 = face_recognition.load_image_file(filename4)

        # مقداردهی اولیه x با یک رشته خالی
        x = ""

        json_file_path = os.path.join(dirname , "info.json")
        with open (json_file_path, "r") as jf:
            data_info = json.load(jf)
       
        
        
        try:
            # استخراج ویژگی‌های چهره از تصویر دوربین
            face_encoding_camera = face_recognition.face_encodings(image2)[0]

            # مسیر پوشه حاوی تصاویر حساب‌ها
            accounts_folder_path = os.path.join(dirname, "accounts")

            # for account in data_info["accounts"]:
            #     face_code = account.get("face code", "")
            #     print(f"Face Code: {face_code}")

            # پیمایش تمام فایل‌های تصویر در پوشه 'accounts'
            for image_file in data_info["accounts"]:
                face_code = image_file.get("face code", "")
                
                
                
                id = image_file.get("id", "")
                # print(f"Face Code: {face_code}")
                
                try:
                    face_encoding1 = eval(face_code)
                    print(type(face_encoding1))
                    # # face_encoding1 = [float(value) for value in face_encoding1]
                    print((face_encoding1))
                    
                    
    #                 face_encoding1 = [-0.11280267,  0.14145838,  0.08018201, -0.00721943, -0.08341715,
    #    -0.00737467, -0.09255081, -0.04201489,  0.09721249, -0.13722058,
    #     0.16613708, -0.02358679, -0.17738828,  0.01263383, -0.03514534,
    #     0.11443079, -0.17246965, -0.13363405, -0.0925321 , -0.03192507,
    #     0.07265631,  0.02960062, -0.03145688,  0.01934741, -0.19897103,
    #    -0.24933299, -0.05345555, -0.07910147,  0.01468277, -0.09238974,
    #    -0.05970011,  0.01262081, -0.15833288, -0.06216215,  0.03326654,
    #     0.1053894 , -0.02119614, -0.01827122,  0.16326623,  0.01349117,
    #    -0.17167389,  0.12390915,  0.06033196,  0.2787444 ,  0.18255034,
    #     0.10085205,  0.00929125, -0.14951234,  0.08070201, -0.17552033,
    #     0.042058  ,  0.15431055,  0.09536897,  0.14445816,  0.03090554,
    #    -0.17823237,  0.08216581,  0.04323204, -0.12752257,  0.07048375,
    #     0.05332949, -0.04839368,  0.09205095, -0.01311017,  0.20425592,
    #     0.00649036, -0.06580383, -0.12497421,  0.087662  , -0.16056764,
    #    -0.08251055,  0.08487719, -0.08776714, -0.1809506 , -0.21913323,
    #     0.05154318,  0.43696192,  0.20777005, -0.18442993,  0.06639418,
    #    -0.03339871, -0.13276626,  0.09905048,  0.13597932, -0.08972022,
    #     0.00206419, -0.02703499,  0.06467727,  0.28189299, -0.00202206,
    #    -0.02021896,  0.18191066,  0.07794417,  0.01044347,  0.06714465,
    #    -0.05016447, -0.11726888,  0.02748273, -0.11316042, -0.05819146,
    #    -0.01228336, -0.1074791 , -0.00496402,  0.09835649, -0.1691    ,
    #     0.14804649, -0.00900794, -0.05294512, -0.03781606,  0.11865336,
    #    -0.12300778, -0.05224946,  0.16455656, -0.21500643,  0.19078164,
    #     0.22787738,  0.09813271,  0.12530968,  0.15702257,  0.10907631,
    #     0.03880517,  0.08882717, -0.11018606, -0.06510164,  0.08780763,
    #    -0.02491565,  0.16878702,  0.03476463]
                    
                    # مقایسه چهره‌ها
                    results = face_recognition.compare_faces([face_encoding1], face_encoding_camera, tolerance=0.4)

                    # بررسی نتایج و تنظیم پیام مناسب
                    if results[0]:
                        x += f"{id} matches.\n"
                    # else:
                    #     x += f"{image_file} does not match.\n"

                except IndexError:
                    # اگر چهره‌ای در تصویر یافت نشود یا تصویر واضح نباشد
                    x += f"No face found or the face is not clear in {image_file}.\n"
                    

        except Exception as e:
            # چاپ خطا در صورت بروز مشکل
            x += f"An error occurred: {e}\n"
            

        # چاپ نتیجه یا به‌روزرسانی متن لیبل
        if zero:
            label12 = tk.CTkLabel(master=frame, text=x, font=("Roboto", 22))
            label12.pack(pady=12, padx=10)
            zero = False
        else:
            label12.configure(text=x)

        # خواباندن برنامه برای جلوگیری از اذیت شدن سیستم
        time.sleep(1)

        
    # cap.release()
######------
    
    
##-------------------------------------------------------------------------------------------
# پنجره ی ساخت اکانت جدید
def save_data():
    # این تابع مقادیر ورودی را در متغیرهای جهانی ذخیره می‌کند
    global user_number ,name_entry ,number_entry, new_window, name_text
    name_text = name_entry.get()
    user_number = number_entry.get()
    print("متن ذخیره شده:", name_text)
    print("عدد ذخیره شده:", user_number)
    #بستن پنجره جدید
    new_window.destroy()
    # عکس گرفتن
    capture_image()


def create_new_window():
    global user_text, user_number ,name_entry ,number_entry , new_window
    new_window = tk.CTkToplevel()
    new_window.title("new win")
    new_window.geometry("600x450")  # اندازه پنجره جدید را تنظیم می‌کند
    new_window.grab_set()  # این خط باعث می‌شود که پنجره جدید تمرکز کاربر را به خود جلب کند
    new_window.focus_set()  # این خط پنجره جدید را در مرکز توجه قرار می‌دهد
    tk.CTkLabel(new_window, text="this is a new win", font=("Roboto", 22)).pack(pady=12, padx=10)
    
    
    label = tk.CTkLabel(new_window, text="creat new acount", font=("Roboto", 22))
    label.pack(pady=12, padx=10)

    # ایجاد ویجت ورودی برای متن
    name_entry = tk.CTkEntry(new_window, placeholder_text="enter your name:", font=("Roboto", 22))
    name_entry.pack(pady=12, padx=10)

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