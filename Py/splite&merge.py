# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 16:25:26 2021

@author: ThisPC
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt_imshow

image = cv2.imread(r'C:\Users\ThisPC\Downloads\man-walking-dog.jpg')



cv2.imshow("Original", image)
# load the input image and grab each channel -- note how OpenCV
# represents images as NumPy arrays with channels in Blue, Green,
# Red ordering rather than Red, Green Blue

(B, G, R) = cv2.split(image)

# show each channel individually
cv2.imshow("Red", R)
cv2.imshow("Green", G)
cv2.imshow("Blue", B)

merged = cv2.merge([B, G, R])
cv2.imshow("Merged", merged)

# visualize each channel in color
zeros = np.zeros(image.shape[:2], dtype="uint8")
cv2.imshow("Red", cv2.merge([zeros, zeros, R]))
cv2.imshow("Green", cv2.merge([zeros, G, zeros]))
cv2.imshow("Blue", cv2.merge([B, zeros, zeros]))




cv2.waitKey(0)
cv2.destroyAllWindows()