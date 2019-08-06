import numpy as np 
import matplotlib.pyplot as plt 
import cv2

img = cv2.imread('DATA/dog_backpack.jpg') #img reading

imgc = cv2.cvtColor(img,cv2.COLOR_BGR2RGB) # convert image from bgr to rgb

ret,thr = cv2.threshold(imgc,127,255,cv2.THRESH_BINARY) #binary thresholding

blended = cv2.addWeighted(imgc,0.7,thr,0.5,0)#blending with original rgb image

blended = cv2.cvtColor(blended,cv2.COLOR_BGR2GRAY) #convert blended image to grayscale

########################################################################################################################

imgc = cv2.cvtColor(imgc,cv2.COLOR_BGR2GRAY) #convert original image to grayscale

adp = cv2.adaptiveThreshold(imgc,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,51,5) # adaptive thresholding

plt.imshow(adp,cmap='gray')
cv2.imshow('orginal img',cv2.resize(imgc,(320,540)))
plt.show()