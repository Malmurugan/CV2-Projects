""" Code to apply clahe to rgb image"""

import cv2

bgr = cv2.imread("<<img.jpg>>")
lab = cv2.cvtColor(bgr, cv2.COLOR_BGR2LAB)

lab_planes = cv2.split(lab)

clahe = cv2.createCLAHE(clipLimit=2.0,tileGridSize=(8,8))

lab_planes[0] = clahe.apply(lab_planes[0])

lab = cv2.merge(lab_planes)

bgr = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)
cv2.imshow("bgr",bgr)
cv2.imwrite("<<clahe.jpg>>",bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()