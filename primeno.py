import numpy as np 
import cv2
import matplotlib.pyplot as plt 

#img = cv2.imread('')
#img = np.zeros((1000,1000,3),np.uint16)
mat = np.zeros((300,300,3))
j=1
for i in range(mat.shape[0]):
    for k in range(mat.shape[1]):
        c=0
        for l in range(2,j):
            if j%l==0:
                c+=1
                break
        if(c==0):
            mat[i,k]=1
        j+=1
mat*=255
mat[0,0]=0

title = 'prime_no_'+str(mat.shape[0])+'x'+str(mat.shape[1])+'.png'
cv2.imwrite(title,mat)
plt.imshow(mat,'gray')
plt.show()