import numpy as np
import matplotlib.pyplot as plt
import cv2
import time
capture = cv2.VideoCapture(0)
width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = capture.get(cv2.CAP_PROP_FPS)
#writer = cv2.VideoWriter('/home/gp/Videos/lilac_procc.mp4',
#                         cv2.VideoWriter_fourcc(*'DIVX'),fps,(width,height))

width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))



while True:
    ret, frame = capture.read()
    frame = cv2.flip(frame,1)
    #frame = cv2.resize(frame,(900,640))
    frame1 = frame
    frame = cv2.medianBlur(frame,7)
    frame = cv2.blur(frame,(3,3))
    median = np.median(frame)
    frame = cv2.Canny(frame,int(max(0,0.7*median)),int(min(255,1.3*median)))
 #   writer.write(frame)
   # time.sleep(1/fps)
    cv2.imshow('vid',frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
#writer.release()
cv2.destroyAllWindows()

