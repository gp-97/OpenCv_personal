import cv2
import numpy as np
import matplotlib.pyplot as plt

sammy = cv2.imread('DATA/sammy.jpg', 0)
sammy_face = cv2.imread('DATA/sammy_face.jpg', 0)

sift = cv2.xfeatures2d.SIFT_create()

kp1,des1 = sift.detectAndCompute(sammy_face,None)
kp2,des2 = sift.detectAndCompute(sammy,None)

bf = cv2.BFMatcher()
matches = bf.knnMatch(des1,des2,k=2)

good = list()

#ratio test
for match1,match2 in matches:
    if match1.distance<0.75*match2.distance:
        good.append([match1])

m = cv2.drawMatchesKnn(sammy_face,kp1,sammy,kp2,good,None,flags=2)
plt.imshow(m)
plt.show()
