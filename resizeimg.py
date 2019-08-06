import numpy as np
import cv2
import matplotlib.pyplot as plt
org_img = cv2.imread('/home/gp/Pictures/cassie-boca-293379-unsplash.jpg')
#new_img = cv2.resize(org_img,(4096,2160))
#plt.imshow(new_img)
#plt.show()

#resizing by ratio
w_ratio=0.5
h_ratio=0.5
#resize to 50%

new_img = cv2.resize(org_img,(0,0),org_img,w_ratio,h_ratio)
# (0,0) ----> a tuple for no apparent reason

plt.imshow(new_img)
plt.show()

plt.imshow(org_img)
plt.show()
