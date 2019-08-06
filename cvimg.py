import numpy as np
import matplotlib.pyplot as plt
import cv2
pic = cv2.imread('/home/gp/Pictures/cassie-boca-293379-unsplash.jpg')
#fix_pic = cv2.cvtColor(pic,cv2.COLOR_BGR2RGB)
fix_pic2 = cv2.imread('/home/gp/Pictures/cassie-boca-293379-unsplash.jpg',cv2.IMREAD_GRAYSCALE)
#plt.imshow(fix_pic)
plt.imshow(fix_pic2,cmap='gray')
plt.show()
