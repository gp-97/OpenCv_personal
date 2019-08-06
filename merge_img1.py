import cv2
import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.cvtColor(cv2.imread('/home/gp/Pictures/pic.jpg'),cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(cv2.imread('/home/gp/Pictures/pic1.jpg'),cv2.COLOR_BGR2RGB)

img1 = cv2.resize(img1,(1920,1080))
img2 = cv2.resize(img2,(1920,1080))

blended = cv2.addWeighted(img1,0.8,img2,0.2,10)

plt.imshow(blended)
plt.show()
cv2.imwrite('blended_img.jpg',cv2.cvtColor(blended,cv2.COLOR_BGR2RGB))
