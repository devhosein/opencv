import cv2

#face_cascade = cv2.CascadeClassifier("./haarcascade_frontalface_default.xml")
face_cascade = cv2.CascadeClassifier("a:/Python/MY_projects/opencv/p1/haarcascade_frontalface_default.xml")
face_eye = cv2.CascadeClassifier("a:/Python/MY_projects/opencv/p1/haarcascade_eye_tree_eyeglasses.xml")



#cap = cv2.VideoCapture("test.mp4")
#cap = cv2.VideoCapture("a:/Python/MY_projects/opencv/p1/test.mp4")
cap = cv2.VideoCapture(0)
# حرکات گنده ای در این برنچ زدم عشق کنی

while cap.isOpened:
    _, img = cap.read()
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1 , 8)
    face_for_eye = face_eye.detectMultiScale(gray, 1.1, 8)

    for (x, y ,w ,h) in faces:
        cv2.rectangle(img, (x,y), ( x+w , y+h), (255,0,0) , 3)
        cv2.putText(img, "face", (x+3, y+30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    for (x, y , w, h) in face_for_eye:
        cv2.rectangle(img , (x,y), (x+w , y+h), (0,0,255),3)
    
    

    
    
    cv2.imshow("img", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


cap.release()



