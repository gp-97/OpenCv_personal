import numpy as np
import cv2
import matplotlib.pyplot as plt

capture = cv2.VideoCapture(0)

width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = capture.get(cv2.CAP_PROP_FPS)
width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))


face_cascade = cv2.CascadeClassifier('DATA/haarcascades/haarcascade_frontalface_default.xml')
eye_cascade  = cv2.CascadeClassifier('DATA/haarcascades/haarcascade_eye.xml')

def detect_face(img):
    face_img = img.copy()

    face_rects = face_cascade.detectMultiScale(face_img)

    for (x, y, w, h) in face_rects:
        cv2.rectangle(face_img, (x, y), (x+w, y+h), (0, 0, 255),3 )
    return face_img


while True:

    ret, frame = capture.read()
    frame = cv2.flip(frame, 1)
    frame = cv2.resize(frame, (900, 640))
    result = detect_face(frame)
    cv2.imshow('vid', result)
    if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cv2.destroyAllWindows()
