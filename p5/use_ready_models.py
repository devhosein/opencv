import numpy
import face_recognition

# بارگذاری تصاویر دو چهره
image1 = face_recognition.load_image_file("a:/Python/MY_projects/opencv/p5/image (1).jpg")
image2 = face_recognition.load_image_file("a:/Python/MY_projects/opencv/p5/image (2).jpg")

# استخراج ویژگی‌های چهره‌ها
face_encoding1 = face_recognition.face_encodings(image1)[0]
face_encoding2 = face_recognition.face_encodings(image2)[0]

# مقایسه دو چهره با یک آستانه 0.6
results = face_recognition.compare_faces([face_encoding1], face_encoding2, tolerance=0.6)

# چاپ نتیجه
if results[0]:
    print("same")
else:
    print("difrent")