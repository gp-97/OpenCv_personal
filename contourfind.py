import numpy as np 
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('DATA/internal_external.png',0)
contour, hierarchy = cv2.findContours(img,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)
print(hierarchy)
ext_img = np.zeros(img.shape)
for i in range(len(contour)):
    if hierarchy[0][i][3]==0:
        cv2.drawContours(ext_img,contour,i,255,-1)
plt.imshow(ext_img,'gray')
plt.show()