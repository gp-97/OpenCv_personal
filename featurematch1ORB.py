import cv2
import numpy as np
import matplotlib.pyplot as plt 
    
puffs = cv2.imread('DATA/reeses_puffs.png',0)
aisle = cv2.imread('DATA/many_cereals.jpg',0)

#creating ORB descriptors
orb = cv2.ORB_create()

#key point and descriptor
kp1,des1 = orb.detectAndCompute(puffs,None)
kp2,des2 = orb.detectAndCompute(aisle,None)

#brute-force matching
bf = cv2.BFMatcher(cv2.NORM_HAMMING2,True)

matches = bf.match(des1,des2)


sort = sorted(matches,key = lambda x:x.distance)

matches = cv2.drawMatches(puffs,kp1,aisle,kp2,matches[:15],None,flags=2)

plt.imshow(matches)
plt.show()