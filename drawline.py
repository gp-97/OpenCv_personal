import numpy as np
import cv2

img = np.zeros((1024,512,3))

drawing = False
ix = -1
iy = -1

def line_draw(event,x,y,flags,param):
    global drawing, ix, iy

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix = x
        iy = y

    elif event == cv2.EVENT_MOUSEMOVE:
        #if event == cv2.EVENT_MOUSE
        if drawing:
            cv2.line(img,)


cv2.namedWindow(winname='Drawing_Space')
cv2.setMouseCallback('Drawing_Space',line_draw)


while True:
    cv2.imshow('Drawing_Space',img)
    if cv2.waitKey(1) & 0xFF = 27:
        break

cv2.destroyAllWindows()
