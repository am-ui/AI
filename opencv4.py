# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 11:56:52 2021

@author: ThisPC
"""

import numpy as np
import cv2
import matplotlib.pyplot as plt

img =cv2.imread(r"C:\Users\ThisPC\Downloads\Pic.jpg", cv2.IMREAD_GRAYSCALE)
px = img[55,55]
print(px)
ROI = img
"""
img[55,55] = [255, 255, 255]
px = img[55,55]
print(px)
#ROI :- Region of images
px = img[100:150,100:150]
print(px)
img[100:150,100:150] = [255,255,255]
print(img.shape)
print(img.size)
print(img.dtype)
my_face = img[37:111,107:194]
img[0:74,0:87] = my_face
#IMREAD_COLOR =1
#IMREAD_UNCHANGED = -1

cv2.imshow('images', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""