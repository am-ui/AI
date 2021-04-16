# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 12:59:37 2021

@author: ThisPC
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
import imutils

image = cv2.imread(r'C:\Users\ThisPC\Downloads\man-walking-dog.jpg')

cv2.imshow('real', image)
# flip the image horizontally
print("[INFO] flipping image horizontally...")
flipped = cv2.flip(image, 1)
cv2.imshow("Flipped Horizontally", flipped)

# flip the image vertically
flipped = cv2.flip(image, 0)
print("[INFO] flipping image vertically...")
cv2.imshow("Flipped Vertically", flipped)

# flip the image along both axes
flipped = cv2.flip(image, -1)
print("[INFO] flipping image horizontally and vertically...")
cv2.imshow("Flipped Horizontally & Vertically", flipped)


cv2.waitKey(0)
cv2.destroyAllWindows()