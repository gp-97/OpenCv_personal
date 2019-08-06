import numpy as np 
import matplotlib.pyplot as plt 
import cv2

img = np.zeros((640,640,3))

ex = 640
ey = 640
ox,oy = 0,0
while ex>320:

    cv2.rectangle(img,(ox+10,oy+10),(ex-10,ey-10),(ex-30,ox+50,ex-50),5)

    ex-=10
    ey-=10
    ox+=10
    oy+=10

plt.imshow(img)

plt.show()