import cv2
import numpy as np
import matplotlib.pyplot as plt

flat_chessboard = cv2.imread('DATA/flat_chessboard.png')

real_chessboard = cv2.imread('DATA/real_chessboard.jpg')

flat_chessboard_gray = cv2.cvtColor(flat_chessboard,cv2.COLOR_BGR2GRAY)
real_chessboard_gray = cv2.cvtColor(real_chessboard,cv2.COLOR_BGR2GRAY)

gray = np.float32(flat_chessboard_gray)
gray1 = np.float32(real_chessboard_gray)

dst = cv2.cornerHarris(gray,2,3,0.04)
dst = cv2.dilate(dst,None)

dst1 = cv2.cornerHarris(gray1,2,3,0.04)
dst1 = cv2.dilate(dst1,None)


flat_chessboard[dst>0.01*dst.max()] = [255,0,0]
real_chessboard[dst1>0.01*dst1.max()] = [0,0,255]


while True:
    cv2.imshow('flat_chessboard_corners',flat_chessboard)
    cv2.imshow('real_chessboard_corners',real_chessboard)
    if cv2.waitKey(1) & 0xFF== ord('q'):
        break

cv2.destroyAllWindows()