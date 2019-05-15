import cv2
import sqlite3
cam = cv2.VideoCapture(0)
detector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def insertorupdate(Id,Name):
    conn = sqlite3.connect("database.db")
    cmd = "SELECT * FROM People WHERE ID="+str(Id)
    cursor = conn.execute(cmd)
    isrecordexist = 0
    for row in cursor:
        isrecordexist = 1
    if(isrecordexist==1):
        cmd="UPDATE people SET Name =" +str(Name) + "WHERE ID="+str(Id)
    else:
        cmd = "INSERT INTO people(ID,Name) Values("+str(Id)+","+str(Name)+")"
    conn.execute(cmd)
    conn.commit()
    conn.close()
    
Id=input('enter your id')
name=input("enter your name ")

insertorupdate(Id,name) 
sampleNum=0
while(True):
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        
        
        sampleNum=sampleNum+1
       
        cv2.imwrite("dataSet/User."+Id +'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])

        cv2.imshow('frame',img)
  
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break
  
    elif sampleNum>50:
        break
cam.release()
cv2.destroyAllWindows()
