import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread('/home/gp/Pictures/pic.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

blank_img = np.zeros(shape=(1024,1024,3),dtype=np.int32)
cv2.rectangle(blank_img,pt1=(256,256),pt2=(768,768),color=(255,0,0),thickness=5)
cv2.circle(blank_img,center =(512,512),radius=256,color=(0,0,255),thickness=5)
cv2.line(blank_img,pt1=(512,256),pt2=(512,768),color=(0,255,0),thickness=5)
cv2.line(blank_img,pt1=(256,512),pt2=(768,512),color=(127,127,127),thickness=5)

plt.imshow(blank_img)
plt.show()

#cv2.imwrite('basic_shapes.jpg',blank_img)
