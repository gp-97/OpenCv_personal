import numpy as np 
import matplotlib.pyplot as plt 
import cv2 

blank_image = np.zeros((600,600,3),np.int16)

def txt(wording):
    global blank_image
    fontface = cv2.FONT_HERSHEY_COMPLEX
    fontsize = 5
    blank_image = cv2.putText(blank_image,wording,(50,300),fontface,fontsize,(255,255,255),15)
        
str= input('Enter text\n')
txt(str)

plt.imshow(blank_image)
plt.show()
