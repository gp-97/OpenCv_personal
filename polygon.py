import numpy as np
import matplotlib.pyplot as plt
import cv2

blank_img = np.zeros(shape=(1024,1024,3),dtype=np.int32)

vertices = np.array([[64,512],[768,512],[312,232],[234,455],[456,99]],dtype=np.int32)

pts = vertices.reshape((-1,1,2))

cv2.polylines(blank_img,[pts],isClosed=True,color=(255,0,0),thickness=5)
plt.imshow(blank_img)
plt.show()
