import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
font = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 0.7
fontColor = (0,255,0)
fontThickness = 2

img = cv2.imread('photo1.jpg')

# Reference axis drawingfor orientation on how the frame in OpenCV works
img_origin = (0,0)
green = (0,255,0)
y_line_ending = (0,450)
cv2.line(img,img_origin,y_line_ending,green,5)
red = (0,0,255)
x_line_ending = (450,0)
cv2.line(img,img_origin,x_line_ending,red,5)


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

offset_multiplier = 20
i = 0

faces = face_cascade.detectMultiScale(gray, 1.3, 5)
print(faces)
for (x,y,w,h) in faces:

    # Each iteration the we going to multiply by the offset_multiplier so the text gets shifted downwards
    i = i + 1
    position = i*offset_multiplier
    text_position = (30,position)

    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    bb_origin = (x,y)
    onScreenString =  "Face" + str(i) + ": x,y = " + "(" + str(x) + "," +  str(y) + ")"
    onScreenString2 = "Face" + str(i) + ": w,h = (" + str(w) + "," + str(h) + ")"
    onScreenString3 = "(x+w) and (y+h): " + "(" + str(x+w) + "," +  str(y+h) + ")"
    cv2.putText(img, onScreenString, bb_origin, font, fontScale, fontColor, fontThickness,cv2.LINE_AA)
    cv2.putText(img, onScreenString2, text_position, font, fontScale, fontColor, fontThickness,cv2.LINE_AA)
    cv2.putText(img, onScreenString3, (x+w,y+h), font, fontScale, fontColor, fontThickness,cv2.LINE_AA)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
