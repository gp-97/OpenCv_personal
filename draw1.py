import numpy as np
#import matplotlib.pyplot as plt
import cv2

#img = np.zeros((1024,1024,3))
img = cv2.imread('/home/gp/Pictures/pic.jpg')
#img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img = cv2.resize(img,(1366,640))

def draw(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),80,(0,255,0),10)
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img,(x,y),80,(0,0,255),10)


cv2.namedWindow(winname='X_viewer')
cv2.setMouseCallback('X_viewer',draw)

while True:
    cv2.imshow('X_viewer',img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
