import numpy as np 
import matplotlib.pyplot as plt 
import cv2 
img1 = cv2.imread('DATA/dog_backpack.jpg')
img2 = cv2.imread('DATA\watermark_no_copy.png')
img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
img22 = cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
img2 = cv2.resize(img22,(600,600))
r1,c1,ch1 = img1.shape
r2,c2,ch2 = img2.shape
roi = img1[(r1-r2):,(c1-c2):]

newimg = cv2.bitwise_and(roi,img2)
img1[(r1-r2):,(c1-c2):] = newimg
print(img2.shape)
plt.imshow(img1)
plt.show()
cv2.imwrite('donotcopy_dogbackpack.jpg',cv2.cvtColor(img1,cv2.COLOR_BGR2RGB))