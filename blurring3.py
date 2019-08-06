import numpy as np
import matplotlib.pyplot as plt 
import cv2
img = cv2.imread('DATA/gorilla.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
blurred = cv2.blur(img,(5,5))
blurred1 = cv2.GaussianBlur(img,(5,5),10)
blurred2 = cv2.medianBlur(img,5)
blurred3 = cv2.bilateralFilter(img,9,75,75)
plt.imshow(blurred3)
plt.show()