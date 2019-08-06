import numpy as np 
import matplotlib.pyplot as plt 
import cv2

blank_image = np.zeros((600, 600, 3), np.int16)

blank_image = cv2.putText(blank_image,'ABCDE', (25, 300), cv2.FONT_HERSHEY_COMPLEX,5, (255, 255, 255), 15)

kernel = np.ones((5,5),np.uint16)
new_image = cv2.erode(blank_image,kernel)


while True:
    cv2.imshow('original_image',blank_image)
    cv2.imshow('eroded_image',new_image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
