"""
Code to implement padding for both left and right frames
"""
import cv2
import numpy as np

# read image
img = cv2.imread('<<frameright.png>>')

ht, wd, cc= img.shape
print(ht)
# create new image of desired size and color (blue) for padding
ww = 1460
hh = 720
color = (255,0,0)
result = np.full((hh,ww,cc), color, dtype=np.uint8)

# compute center offset
xx = 180
yy = 0

# copy img image into center of result image
result[yy:yy+ht, xx:xx+wd] = img

# view result
result = cv2.resize(result, (730, 360), interpolation=cv2.INTER_AREA)
cv2.imshow("result", result)

img1 = cv2.imread('<<frameleft.png>>')

ht1, wd1, cc1= img1.shape

# create new image of desired size and color (blue) for padding
ww1 = 1460
hh1 = 720
color1 = (255,0,0)
result1 = np.full((hh1,ww1,cc1), color1, dtype=np.uint8)

# compute center offset
xx1 = 0
yy1 = 0

# copy img image into center of result image
result1[yy1:yy1+ht1, xx1:xx1+wd1] = img1

# view result
result1 = cv2.resize(result1, (730, 360), interpolation=cv2.INTER_AREA)
cv2.imshow("result1", result1)


added_image = cv2.addWeighted(result,0.4,result1,0.2,0)
cv2.imshow("addedimage", added_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

# save result
cv2.imwrite("out/right_result.jpg", result)
cv2.imwrite("out/left_result.jpg", result1)