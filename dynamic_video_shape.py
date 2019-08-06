import cv2

capture = cv2.VideoCapture(0)

width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

ptx1=0
pty1=0
ptx2=0
pty2=0

top_left_clicked =False
bottom_right_clicked = False

def draw_shape(event,x,y,flags,param):
    global top_left_clicked, bottom_right_clicked,ptx1,ptx2,pty1,pty2
    if event == cv2.EVENT_LBUTTONDOWN:
        if top_left_clicked==False and bottom_right_clicked==False:
            ptx1 = x
            pty1 = y
            top_left_clicked = True
        elif top_left_clicked and bottom_right_clicked == False:
            ptx2 = x
            pty2 = y
            bottom_right_clicked = True
        elif top_left_clicked and bottom_right_clicked:
            ptx1 = 0
            pty1 = 0
            ptx2 = 0
            pty2 = 0
            top_left_clicked = False
            bottom_right_clicked = False


cv2.namedWindow('video')
cv2.setMouseCallback('video',draw_shape)

while True:
    ret, frame = capture.read()
    frame = cv2.flip(frame, 1)
    if top_left_clicked and bottom_right_clicked==False:
        cv2.circle(frame,(ptx1,pty1),3,(0,0,255),-1)
    elif top_left_clicked and bottom_right_clicked:
        cv2.rectangle(frame,(ptx1,pty1),(ptx2,pty2),(0,0,255),3)
    
    
    cv2.imshow('video',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
    
