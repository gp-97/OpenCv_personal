import cv2, numpy as np, matplotlib.pyplot as plt
img = cv2.imread('DATA/sammy.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
face = cv2.imread('DATA/sammy_face.jpg')
face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)

methods = ['cv2.TM_CCOEFF','cv2.TM_CCOEFF_NORMED','cv2.TM_CCORR','cv2.TM_CCORR_NORMED',
                                                'cv2.TM_SQDIFF','cv2.TM_SQDIFF_NORMED']

r, c, ch = face.shape

for m in methods:
    tm = eval(m)
    img1 = np.copy(img)
    res  = cv2.matchTemplate(img1,face,tm)
    
    minval,maxval,minloc,maxloc = cv2.minMaxLoc(res)
    
    tlx,tly,brx,bry = 0,0,0,0
    if m in ['cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']:
        tlx,tly = minloc
    else:
        tlx,tly = maxloc
    
    brx = tlx + c
    bry = tly + r
    cv2.rectangle(img1,(tlx,tly),(brx,bry),(255,0,0),5)
    plt.subplot(121)
    plt.imshow(res)
    plt.subplot(122)
    plt.imshow(img1)
    plt.show()
    
