import numpy as np
import sqlite3
import cv2

facedetector= cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0);
rec = cv2.face.LBPHFaceRecognizer_create();
rec.read("trainner\\trainnerdata.yml")
id = 0

fontFace = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 1
fontColor = (255, 255, 255)


def getprofile(id):
    conn = sqlite3.connect("database.db")
    cmd = "SELECT * FROM People WHERE ID="+ str(id)
    cursor = conn.execute(cmd)
    profile = None

    for row in cursor:
        profile = row
    conn.close()
    return profile

while(True):
    ret, img = cam.read();
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = facedetector.detectMultiScale(gray, 1.3, 5);
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

        id,conf=rec.predict(gray[y:y+h,x:x+w])

        profile = getprofile(id)
        if profile != None:
            cv2.putText(img,profile[1],(x,y+h+30),fontFace,2,(155,0,0),2);
            cv2.putText(img,profile[3],(x,y+h+60),fontFace,2,(155,0,0),2);
    cv2.imshow('frame',img);
    if (cv2.waitKey(1) == ord('q')):
        break;
    
cam.release()
cv2.destroyAllWindows()

