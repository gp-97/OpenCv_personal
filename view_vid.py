import cv2
import time

cap = cv2.VideoCapture('/home/gp/Videos/vid1.mp4')
fps = cap.get(cv2.CAP_PROP_FPS)
if cap.isOpened() == False:
    print('ERROR\n')

while cap.isOpened():
    ret,frame = cap.read()
    if ret:
        time.sleep(1/fps)
        cv2.imshow('video',frame)

        if cv2.waitKey(10) & 0xFF == ord('x'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
print(fps)
