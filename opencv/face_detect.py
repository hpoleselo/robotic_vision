import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
font = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 0.7
fontColor = (0,255,0)
fontThickness = 2

#desenhar origem
#cv2.drawAxis()

img = cv2.imread('photo1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


faces = face_cascade.detectMultiScale(gray, 1.3, 5)
print(faces)
for (x,y,w,h) in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    origin = (x,y)
    onScreenString = "x,y: " + str(x) + "," +  str(y)
    onScreenString2 = "[x+w] and [y+h]: " + str(x+w) + "," +  str(y+h)
    cv2.putText(img, onScreenString, origin, font, fontScale, fontColor, fontThickness,cv2.LINE_AA)
    cv2.putText(img, onScreenString2, (x+w,y+h), font, fontScale, fontColor, fontThickness,cv2.LINE_AA)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]

cv2,
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
