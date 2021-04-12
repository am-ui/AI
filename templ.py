# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 16:03:14 2021

@author: ThisPC
"""

"""
Template Matching is a method for searching and finding the location of a template image in a larger image. 
OpenCV comes with a function cv2.matchTemplate() for this purpose. 
It simply slides the template image over the input image (as in 2D convolution) and compares the template and patch of input image under the template image

"""
import cv2
import  numpy as np
img_rgb = cv2.imread(r"C:\Users\ThisPC\Desktop\temp2.jpg")
#img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)



template = cv2.imread(r'C:\Users\ThisPC\Desktop\temp1.jpg', 0)
#img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

#template = cv2.imread('',0)
w, h = template.shape[::-1]

res = cv2.matchTemplate(img_rgb,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.4
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)
    
cv2.imshow('Detected',img_rgb)
#cv2.imshow('image1', img_rgb)
cv2.imshow('detected', res)
#cv2.imshow('image2', img_gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
