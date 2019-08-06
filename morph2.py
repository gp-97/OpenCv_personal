import cv2
import numpy as np
import matplotlib.pyplot as plt

blank_image = cv2.putText(np.zeros((400, 400, 3), np.int16), 'ABC',
                         (25, 300), cv2.FONT_HERSHEY_COMPLEX, 5, (255, 255, 255), 15)

noise = np.random.randint(0,2,(400,400,3),np.uint8)*255

blank_image+=noise
kernel = np.ones((5,5),np.uint8)
new_image = cv2.morphologyEx(blank_image,cv2.MORPH_OPEN,kernel)
erode = cv2.erode(new_image,kernel)
f = cv2.morphologyEx(erode,cv2.MORPH_CLOSE,kernel)
g = cv2.morphologyEx(f,cv2.MORPH_GRADIENT,kernel)

plt.imshow(g)
plt.show() 
