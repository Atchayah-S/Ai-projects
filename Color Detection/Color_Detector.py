import cv2
import numpy as np
color_boundary={ 'red':([170,120,70],[180,255,255]) , 'green':([40,40,40],[90,255,255]),
       'blue':([100,150,0],[140,255,255]),'yellow':([15,100,100],[30,255,255]),
       'black':([0,0,0],[180,255,30]),'white':([0,0,200],[180,50,255]),'gray':([0,0,40],[180,20,200]), 'purple':([129,50,70],[158,255,255])}
def detector(obj):
    frame=cv2.cvtColor(obj,cv2.COLOR_BGR2HSV)
    for color,(low,up) in color_boundary.items():
        lb=np.array(low)
        ub=np.array(up)
        mask=cv2.inRange(frame,lb,ub)
        if cv2.countNonZero(mask)>500:
            return color
capture=cv2.VideoCapture(0)
while True:
    ret,frame=capture.read()
    if not ret:
        continue
    color=detector(frame)
    cv2.putText(frame,color,(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,0),4)
    cv2.imshow('Color Detection',frame)
    key=cv2.waitKey(10)
    print(key)
    if key==27:
        break
cv2.release()
cv2.destroyAllWindows()
