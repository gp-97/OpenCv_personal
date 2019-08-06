import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread('DATA/sudoku.jpg',0)

sobel_x = cv2.Sobel(img,cv2.CV_64F,1,0)
sobel_y = cv2.Sobel(img, cv2.CV_64F, 0,1)

blended = cv2.addWeighted(sobel_x,5,sobel_y,5,2)

ret,thr = cv2.threshold(blended,100,255,cv2.THRESH_BINARY)
blur = cv2.blur(thr,(5,5))

laplacian = cv2.Laplacian(img,cv2.CV_64F)
plt.imshow(laplacian,'gray')
plt.show()
