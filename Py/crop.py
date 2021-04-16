# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 14:24:30 2021

@author: ThisPC
"""


import cv2
import numpy as np
import matplotlib.pyplot as plt
import imutils

image = cv2.imread(r'C:\Users\ThisPC\Downloads\man-walking-dog.jpg')


# load the input image and display it to our screen
cv2.imshow("Original", image)

# cropping an image with OpenCV is accomplished via simple NumPy
# array slices in startY:endY, startX:endX order -- here we are
# cropping the face from the image (these coordinates were
# determined using photo editing software such as Photoshop,
# GIMP, Paint, etc.)
face = image[85:250, 85:220]
cv2.imshow("Face", face)

# apply another image crop, this time extracting the body
body = image[90:450, 0:290]
cv2.imshow("Body", body)