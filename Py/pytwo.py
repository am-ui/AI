# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 14:22:45 2021

@author: ThisPC
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(r'C:\Users\ThisPC\Downloads\man-walking-dog.jpg')
cv2.imshow('images', img)

(h,w,c) = img.shape[:3]


# images are simply NumPy arrays -- with the origin (0, 0) located at
# the top-left of the image
(b, g, r) = img[0, 0]
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

# access the pixel located at x=50, y=20
(b, g, r) = img[20, 50]
print("Pixel at (50, 20) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

# update the pixel at (50, 20) and set it to red
img[20, 50] = (0, 0, 255)
(b, g, r) = img[20, 50]
print("Pixel at (50, 20) - Red: {}, Green: {}, Blue: {}".format(r, g, b))
# compute the center of the image, which is simply the width and height
# divided by two
(cX, cY) = (w // 2, h // 2)

# since we are using NumPy arrays, we can apply array slicing to grab
# large chunks/regions of interest from the image -- here we grab the
# top-left corner of the image
tl = img[0:cY, 0:cX]
plt.imshow("Top-Left Corner", tl)

# in a similar fashion, we can crop the top-right, bottom-right, and
# bottom-left corners of the image and then display them to our
# screen
tr = img[0:cY, cX:w]
br = img[cY:h, cX:w]
bl = img[cY:h, 0:cX]
plt.imshow("Top-Right Corner", tr)
cv2.im
plt.imshow("Bottom-Right Corner", br)
plt.imshow("Bottom-Left Corner", bl)

# set the top-left corner of the original image to be green
img[0:cY, 0:cX] = (0, 255, 0)

# Show our updated image
plt.imshow("Updated", img)

cv2.waitKey(0)
cv2.destroyAllWindows()