import cv2,numpy as np, matplotlib.pyplot as plt

flat_chessboard = cv2.imread('DATA/flat_chessboard.png')

real_chessboard = cv2.imread('DATA/real_chessboard.jpg')

flat_chessboard_gray = cv2.cvtColor(flat_chessboard, cv2.COLOR_BGR2GRAY)
real_chessboard_gray = cv2.cvtColor(real_chessboard, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(real_chessboard_gray,100,0.01,10)

corners = np.int0(corners)
for i in corners:
    print(i)
    x,y = i.ravel()
    cv2.circle(real_chessboard,(x,y),3,(255,0,255),-1)

while True:
#    cv2.imshow('flat_chessboard_corners', flat_chessboard)
    cv2.imshow('real_chessboard_corners', real_chessboard)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
