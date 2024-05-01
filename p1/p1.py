import cv2
import numpy
import face_recognition
import time



import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "haarcascade_frontalface_default.xml")
face_cascade = cv2.CascadeClassifier(filename)




#face_cascade = cv2.CascadeClassifier("./haarcascade_frontalface_default.xml")
#######face_cascade = cv2.CascadeClassifier("a:/Python/MY_projects/opencv/p1/haarcascade_frontalface_default.xml")
#face_eye = cv2.CascadeClassifier("a:/Python/MY_projects/opencv/p1/haarcascade_eye_tree_eyeglasses.xml")



#cap = cv2.VideoCapture("test.mp4")
#cap = cv2.VideoCapture("a:/Python/MY_projects/opencv/p1/test.mp4")
cap = cv2.VideoCapture(0)

bool_avalin_tashkhis_face = False

while cap.isOpened:
    _, img = cap.read()
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1 , 8)
    # face_for_eye = face_eye.detectMultiScale(gray, 1.1, 8)

    # for (x, y ,w ,h) in faces:
    #     cv2.rectangle(img, (x,y), ( x+w , y+h), (255,0,0) , 3)
    #     cv2.putText(img, "face", (x+3, y+30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    # for (x, y , w, h) in face_for_eye:
    #     cv2.rectangle(img , (x,y), (x+w , y+h), (0,0,255),3)
    

    # کد نشان دادن تصویر
#    cv2.imshow("img", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    
    
    
    # take a photo and save it   
    if len(faces) > 0:
        bool_avalin_tashkhis_face = True
        
    if bool_avalin_tashkhis_face == True:
        result, img = cap.read()
        if result:
            cv2.imwrite("A:\Python\MY_projects\opencv\p1\hello.png", img)
            
            
    ### مقایسه دو چهره

    # بارگذاری تصاویر دو چهره
    image1 = face_recognition.load_image_file("a:/Python/MY_projects/opencv/p1/image (1).jpg")
    image2 = face_recognition.load_image_file("a:/Python/MY_projects/opencv/p1/hello.png")

    # استخراج ویژگی‌های چهره‌ها
    face_encoding1 = face_recognition.face_encodings(image1)[0]
    # face_encoding2 = face_recognition.face_encodings(image2)[0]
    try:
        face_encoding2 = face_recognition.face_encodings(image2)[0]
        results = face_recognition.compare_faces([face_encoding1], face_encoding2, tolerance=0.5)
        if results[0]:
            print("same")
        else:
            print("difrent")
    except:
        print("The face is not clear !!")
    
    

        
    time.sleep(0.2)

                
cap.release()


