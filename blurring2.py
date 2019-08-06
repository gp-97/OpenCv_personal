import numpy as np
import matplotlib.pyplot as plt 
import cv2
img = cv2.imread('DATA/gorilla.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

kern = np.ones((5,5),np.uint16)/25
print(kern)
mat = np.array([[0.0625,0.125,0.0625],[0.125,0.25,0.125],[0.0625,0.125,0.0625]])
print(mat)
blurred = cv2.filter2D(img,-1,mat)

plt.imshow(blurred)
plt.show()