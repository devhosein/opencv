# import os
# import cv2
# import face_recognition
# import time

# def hellotest():
#     # نشان دادن جای فایل بدون دادن ادرس کامل 
#     dirname = os.path.dirname(__file__)
#     ##
#     #filename = os.path.join(dirname, "haarcascade_frontalface_default.xml")
#     #face_cascade = cv2.CascadeClassifier(filename)
#     ##


#     # دادن ایکس ام ال به اوپن سیوی
#     filename = os.path.join(dirname, "haarcascade_frontalface_default.xml")
#     face_cascade = cv2.CascadeClassifier(filename)

#     # کمرا
#     cap = cv2.VideoCapture(0)

#     # یکی از متغییر های لازم برای ذخیره ی عکس 
#     bool_avalin_tashkhis_face = False



#     # وایل مدام اجرا شدن سیستم تشخیص چهره
#     while cap.isOpened:
        
#         # تشخیص چهره توسط اوپن سی وی 
#         _, img = cap.read()
#         gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#         faces = face_cascade.detectMultiScale(gray, 1.1 , 8)
#         # face_for_eye = face_eye.detectMultiScale(gray, 1.1, 8)


#     # نشان دادن چهره و دور چهره خط کشیدن
#     #-------------------------------------------------------------------------------------------
#         # for (x, y ,w ,h) in faces:
#         #     cv2.rectangle(img, (x,y), ( x+w , y+h), (255,0,0) , 3)
#         #     cv2.putText(img, "face", (x+3, y+30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
#         # for (x, y , w, h) in face_for_eye:
#         #     cv2.rectangle(img , (x,y), (x+w , y+h), (0,0,255),3)
        
#     #     کد نشان دادن تصویر
#     #    cv2.imshow("img", img)

#     #    جهت بستن تصویر نمایش داده شده
#         # if cv2.waitKey(1) & 0xFF == ord("q"):
#         #     break
#     #-------------------------------------------------------------------------------------------
        
        
#         # گرفتن عکس و ذخیره کردن عکس پشت سر هم ... 
#         if len(faces) > 0:
#             bool_avalin_tashkhis_face = True
            
#         if bool_avalin_tashkhis_face == True:
#             result, img = cap.read()
#             filename2 = os.path.join(dirname, "frame.png")
#             if result:
#                 cv2.imwrite(filename2, img)
                
                
#         # مقایسه دو چهره
#     #-------------------------------------------------------------------------------------------------------------
#         # بارگذاری تصاویر چهره ها
#         filename3 = os.path.join(dirname, "image (1).jpg")
#         image1 = face_recognition.load_image_file(filename3)
#         # تصویر ذخیره شده توسط کمرا
#         filename4 = os.path.join(dirname, "frame.png")
#         image2 = face_recognition.load_image_file(filename4)


#         try:
#         # استخراج ویژگی‌های چهره‌ها
#             face_encoding1 = face_recognition.face_encodings(image1)[0]
        
        
#         # جلو گیری از ارور وجود نداشتن عکس و خراب بودن عکس
#             try:
#                 # گرفتن ویژگی های تصویر کمرا
#                 face_encoding_camera = face_recognition.face_encodings(image2)[0]
            
#                 # چقدر چهره ها لازمه مثل هم باشن ؟؟
#                 results = face_recognition.compare_faces([face_encoding1], face_encoding_camera, tolerance=0.5)
#                 # شبیه بود
#                 if results[0]:
#                     print("same")
#                     print("hello boss, very nice to meet you \n")


#                 # یکی دیگه بود
#                 else:
#                     x = print("diffrent")
#                     x = ("go away !! \n")
#             # تصویر نیست و یا خرابه
#             except:
#                 x = ("We do not have the face or The face is not clear !!")
            
#         except:
#             x = ("the diffalt picture is very bad")
#     #--------------------------------------------------------------------------------------------------------------
#         # خوابوندن تایم برای اینکه سیستم اذیت نشه یه وقت !!
#         time.sleep(0.2)
       
        
        
    

#     cap.release()
    
# hellotest()















import customtkinter as tk
import threading
import queue

# تابعی که می‌خواهید در نخ جداگانه اجرا شود
def function_to_run(output_queue):
    # کد مورد نظر برای اجرا
    output_text = "تابع در حال اجرا است..."
    output_queue.put(output_text)

# تابعی که نخ را ایجاد و شروع می‌کند
def start_thread(output_queue):
    thread = threading.Thread(target=function_to_run, args=(output_queue,))
    thread.start()

# تابعی برای بروزرسانی متن CTkLabel با استفاده از داده‌های صف
def update_label_from_queue(output_queue, label):
    try:
        # دریافت خروجی از صف
        output_text = output_queue.get_nowait()
        # بروزرسانی متن لیبل
        label.configure(text=output_text)
    except queue.Empty:
        # اگر صف خالی است، هیچ کاری انجام ندهید
        pass
    # برنامه ریزی برای بروزرسانی بعدی
    root.after(100, update_label_from_queue, output_queue, label)

# ایجاد صف
output_queue = queue.Queue()

# ایجاد رابط کاربری
root = tk.CTk()
root.geometry("1000x600")

# ایجاد و نمایش لیبل
output_label = tk.CTkLabel(root, text="منتظر خروجی...")
output_label.pack()

# شروع نخ و بروزرسانی لیبل
start_thread(output_queue)
root.after(100, update_label_from_queue, output_queue, output_label)

# شروع حلقه اصلی
root.mainloop()