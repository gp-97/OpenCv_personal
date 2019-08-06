import numpy as np, cv2, matplotlib.pyplot as plt 
nadia = cv2.imread('DATA/Nadia_Murad.jpg',0)
denis = cv2.imread('DATA/Denis_Mukwege.jpg',0)
solvay = cv2.imread('DATA/solvay_conference.jpg',0)

gpimg = cv2.imread('DATA/groupImg.jpg')
gpimg = cv2.cvtColor(gpimg,cv2.COLOR_BGR2RGB)



face_cascade = cv2.CascadeClassifier('DATA/haarcascades/haarcascade_frontalface_default.xml')

def detect_face(img):
    face_img = img.copy()
    
    face_rects = face_cascade.detectMultiScale(face_img)

    for (x,y,w,h) in face_rects:
        cv2.rectangle(face_img,(x,y),(x+w,y+h),(255,0,255),2)
    return face_img

result = detect_face(gpimg)
plt.imshow(result,'gray')
plt.show()
