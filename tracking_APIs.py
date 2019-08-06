import cv2

def tracker_choice():
    trackers = {'0':'Boosting','1':'MIL','2':'KCF','3':'TLD','4':'MEDIANFLOW'}
    choice = input('Enter tracker choice between - 0 to 4\n')
    print('You chose:\t', trackers[choice],'\n')
    if choice=='0':
        tracker_name = cv2.TrackerBoosting_create()
    if choice=='1':
        tracker_name = cv2.TrackerMIL_create()
    if choice=='2':
        tracker_name = cv2.TrackerKCF_create()
    if choice=='3':
        tracker_name = cv2.TrackerTLD_create()
    if choice=='4':
        tracker_name = cv2.TrackerMedianFlow_create()
    
    return tracker_name

tracker = tracker_choice()
tracker_name = str(tracker).split()[0][1:]
cap=cv2.VideoCapture(0)
ret, frame = cap.read()
frame = cv2.flip(frame,1)
roi = cv2.selectROI(frame, False)
ret = tracker.init(frame, roi)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)
    success, roi = tracker.update(frame)
    (x,y,w,h) = tuple(map(int,roi))
    
    if success:
        p1 = (x,y)
        p2 = (x+w, y+h)
        cv2.rectangle(frame,p1,p2,(0,0,255),3)
    else:
        cv2.putText(frame, 'Failure to detect object', (50, 50),
                    cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255), 2)
    
    cv2.imshow(tracker_name, frame)
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

        

    
