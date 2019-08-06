import numpy as np
import matplotlib.pyplot as plt 
import cv2
img = cv2.imread('DATA/gorilla.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
blurred = cv2.blur(img,(10,10))
plt.imshow(blurred)
plt.show()