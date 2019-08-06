import cv2, numpy as np, matplotlib.pyplot as plt
capture = cv2.VideoCapture(0)
width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

x = width//3
y = height//3

w = width//2
h = height//2
while True:
    ret,frame = capture.read()
    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),5)
    frame = cv2.resize(frame,(960,720))
    frame = cv2.flip(frame,1)
    
    
    cv2.imshow('stream',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
