import numpy as np
import matplotlib.pyplot as plt 
import cv2
img = cv2.imread('DATA/gorilla.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
gam = 0.5
bimg=img/255
new = np.power(bimg,gam)
plt.imshow(new)
plt.show()