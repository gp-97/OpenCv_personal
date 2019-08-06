import numpy as np
import cv2

img = np.zeros((640,1360,3))

drawing = False
ix=-1
iy=-1

def drawer(event,x,y,flags,param):

    global drawing, ix, iy

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix = x
        iy = y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            r = int(((x-ix)**2+(y-iy)**2)**0.5)
            cv2.circle(img,(ix,iy),r,(255,0,0),1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        r = int(((x-ix)**2+(y-iy)**2)**0.5)
        cv2.line(img,(x,y),r,(255,0,0),1)

cv2.namedWindow(winname='Picture')
cv2.setMouseCallback('Picture',drawer)

while True:
    cv2.imshow('Picture',img)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
#cv2.imwrite('CoolDesign.jpg',cv2.resize(img,(1366,768)))
