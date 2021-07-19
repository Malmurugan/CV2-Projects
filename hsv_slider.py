"""
Code for HSV color-space slider
"""
import cv2
import numpy as np


cap = cv2.imread("<<ex.jpg>>")


def nothing(x):
    pass


# Creating a window for later useq
cv2.namedWindow('result')

# Starting with 100's to prevent error while masking
h,s,v = 100,100,100

# Creating track bar
cv2.createTrackbar('h1', 'result',0,179,nothing)
cv2.createTrackbar('s1', 'result',0,255,nothing)
cv2.createTrackbar('v1', 'result',0,255,nothing)

cv2.createTrackbar('h2', 'result',0,179,nothing)
cv2.createTrackbar('s2', 'result',0,255,nothing)
cv2.createTrackbar('v2', 'result',0,255,nothing)

while(1):

    frame = cap

    # converting to HSV
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    # get info from track bar and appy to result
    h1 = cv2.getTrackbarPos('h1','result')
    s1 = cv2.getTrackbarPos('s1','result')
    v1 = cv2.getTrackbarPos('v1','result')

    h2 = cv2.getTrackbarPos('h2', 'result')
    s2 = cv2.getTrackbarPos('s2', 'result')
    v2 = cv2.getTrackbarPos('v2', 'result')

    # Normal masking algorithm
    lower = np.array([h1,s1,v1])
    upper = np.array([h2,s2,v2])

    mask = cv2.inRange(hsv,lower, upper)

    result = cv2.bitwise_and(frame,frame,mask = mask)

    cv2.imshow('result',result)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cap.release()

cv2.destroyAllWindows()