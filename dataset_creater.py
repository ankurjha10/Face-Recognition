import cv2
import numpy as np
import sqlite3

faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0)

def insertorupdate(Id, Name, age):
    conn = sqlite3.connect("database.db")
    cmd = "SELECT * FROM STUDENTS WHERE ID=" + str(Id)
    cursor = conn.execute(cmd)
    isRecordExist = 0
    for row in cursor:
        isRecordExist = 1
    if(isRecordExist == 1):
        conn.execute("UPDATE STUDENTS SET Name=? WHERE Id=?", (Name, Id))
        conn.execute("UPDATE STUDENTS SET age=? WHERE Id=?", (age, Id))
    else:
        conn.execute("INSERT INTO STUDENTS (Id,Name,age) values(?,?,?)", (Id, Name, age))
    conn.commit()
    conn.close()

Id = input('Enter User ID: ')
Name = input('Enter User Name: ')
age = input('Enter User Age: ')

insertorupdate(Id, Name, age)

sampleNum = 0
while True:
    ret, img = cam.read()

    # ✅ Flip the camera preview so it looks like mirror
    img = cv2.flip(img, 1)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        sampleNum += 1
        # Save the flipped face from grayscale
        cv2.imwrite("dataset/user." + str(Id) + "." + str(sampleNum) + ".jpg", gray[y:y+h, x:x+w])
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.waitKey(100)

    # ✅ Preview bhi flipped hi dikhega
    cv2.imshow("Face", img)
    cv2.waitKey(1)

    if sampleNum > 20:
        break

cam.release()
cv2.destroyAllWindows()
