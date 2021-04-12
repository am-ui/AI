# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 18:09:02 2021

@author: ThisPC
"""

import numpy as np
import cv2

img = cv2.imread(r'C:\Users\ThisPC\Downloads\opencv-corner-detection-sample.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #convert the images in to gray
#convert the pixels in to float
gray = np.float32(gray)

#detect the corners
corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)
corners = np.int0(corners)
for corner in corners:
    x,y = corner.ravel() #revel is used to change a 2-dimensional array or a multi-dimensional array into a contiguous flattened array
    cv2.circle(img,(x,y),3,255,-1) #marked the circle on the line of corners
    
cv2.imshow('Corner',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
