"""
Code for lab color-space slider
"""
import cv2
import numpy as np

cap = cv2.imread("<<ex.png>>")
cap = cv2.resize(cap, (852, 480), interpolation=cv2.INTER_AREA)


def nothing(x):
    pass


# Creating a window for later useq
cv2.namedWindow('result')

# Starting with 100's to prevent error while masking
h,s,v = 100,100,100

# Creating track bar
cv2.createTrackbar('l1', 'result',0,255,nothing)
cv2.createTrackbar('a1', 'result',0,255,nothing)
cv2.createTrackbar('b1', 'result',0,255,nothing)

cv2.createTrackbar('l2', 'result',0,255,nothing)
cv2.createTrackbar('a2', 'result',0,255,nothing)
cv2.createTrackbar('b2', 'result',0,255,nothing)


while(1):

    frame = cap

    # converting to HSV
    lab = cv2.cvtColor(frame,cv2.COLOR_BGR2LAB)
    l,a,b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))

    # get info from track bar and appy to result
    l1 = cv2.getTrackbarPos('l1','result')
    a1 = cv2.getTrackbarPos('a1','result')
    b1 = cv2.getTrackbarPos('b1','result')
    
    l2 = cv2.getTrackbarPos('l2', 'result')
    a2 = cv2.getTrackbarPos('a2', 'result')
    b2 = cv2.getTrackbarPos('b2', 'result')

    # Normal masking algorithm
    lower = np.array([l1,a1,b1])
    upper = np.array([l2,a2,b2])

    mask = cv2.inRange(lab,lower, upper)

    result = cv2.bitwise_and(frame,frame,mask = mask)

    cv2.imshow('result',result)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cap.release()

cv2.destroyAllWindows()