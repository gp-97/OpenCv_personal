import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
pic = Image.open('/home/gp/Pictures/cassie-boca-293379-unsplash.jpg')
pic_arr = np.asarray(pic)
#print(pic_arr)
#pic_arr_g = pic_arr.copy()
#pic_arr_g = pic_arr_g[:,:,1]
#pic_arr_g = 0
pic_arr_r = pic_arr.copy()
pic_arr_r[:,:,1]=0
pic_arr_r[:,:,0]=0

#pic_arr_b = pic_arr.copy()
#pic_arr_b = pic_arr_b[:,:,2]
#pic_arr_b = 0
plt.imshow(pic_arr_r)
plt.show()
#plt.imshow(pic_arr_g)
#plt.show()
#plt.imshow(pic_arr_b)
#plt.show()
