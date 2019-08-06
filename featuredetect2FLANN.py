import cv2
import numpy as np
import matplotlib.pyplot as plt

sammy = cv2.imread('DATA/sammy.jpg', 0)
sammy_face = cv2.imread('DATA/sammy_face.jpg', 0)

sift = cv2.xfeatures2d.SIFT_create()

kp1,des1 = sift.detectAndCompute(sammy_face,None)
kp2, des2 = sift.detectAndCompute(sammy, None)

FLANN_INDEX_KDTREE = 0
index_params = dict(algorithm = FLANN_INDEX_KDTREE,trees = 5)
search_params = dict(checks = 50)

flann = cv2.FlannBasedMatcher(index_params,search_params)

matches = flann.knnMatch(des1,des2,k=2)

good = []

for match1,match2 in matches:
    if match1.distance<0.75*match2.distance:
        good.append([match1])

flann_matches = cv2.drawMatchesKnn(sammy_face,kp1,sammy,kp2,good,None,flags=0)
plt.imshow(flann_matches,'gray')
plt.show()
