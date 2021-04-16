# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 10:44:22 2021

@author: ThisPC
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
import imutils

img = cv2.imread(r"C:\Users\ThisPC\Downloads\man-walking-dog.jpg")
cv2.imshow("orignal", img)

# shift the image 25 pixels to the right and 50 pixels down
M = np.float32([[1, 0, 25], [0, 1, 50]])
shifted = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
cv2.imshow("Shifted Down and Right", shifted)


# now, let's shift the image 50 pixels to the left and 90 pixels
# up by specifying negative values for the x and y directions,
# respectively
M = np.float32([[1, 0, -50], [0, 1, -90]])
shifted = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
cv2.imshow("Shifted Up and Left", shifted)

# use the imutils helper function to translate the image 100 pixels
# down in a single function call
shifted = imutils.translate(img, 0, 100)
cv2.imshow("Shifted Down", shifted)

cv2.waitKey(0)
cv2.destroyAllWindows()