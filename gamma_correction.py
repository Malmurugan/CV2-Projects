"""
code to apply gamma correction to an image
"""
from __future__ import print_function
import cv2 as cv
import numpy as np

image = cv.imread("<<img.jpg>>")
image = cv.medianBlur(image, 3)
if image is None:
    print('Could not open or find the image')
    exit(0)

new_image = np.zeros(image.shape, image.dtype)

alpha = 1.0  # Simple contrast control
beta = 0    # Simple brightness control

# Initialize values
print(' Basic Linear Transforms ')
print('-------------------------')
try:
    alpha = 2
    beta = 50

except ValueError:
    print('Error, not a number')

new_image = cv.convertScaleAbs(image, alpha=alpha, beta=beta)

# [basic-linear-transform-operation]
lookUpTable = np.empty((1,256), np.uint8)
gamma = 0.5
for i in range(256):
    lookUpTable[0,i] = np.clip(pow(i / 255.0, gamma) * 255.0, 0, 255)
res = cv.LUT(image, lookUpTable)

# Show stuff
cv.imshow('Original Image', image)
cv.imshow('New Image', new_image)
cv.imshow('gamma',res)
cv.imwrite("gamma0_5.jpg",res)
# Wait until user press some key
cv.waitKey()
