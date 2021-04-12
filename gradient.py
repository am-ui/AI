# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 15:32:57 2021

@author: ThisPC
"""
import cv2
import numpy as np
cap = cv2.VideoCapture(1)

while(1):

    # Take each frame
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower_red = np.array([30,150,50])
    upper_red = np.array([255,255,180])
    
    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame,frame, mask= mask)

#Laplace(f)=∂2f/∂x2+∂2f/∂y2
#The Laplacian operator is implemented in OpenCV by the function Laplacian() . In fact, since the Laplacian uses the gradient of images, it calls internally the Sobel operator to perform its computation.

    laplacian = cv2.Laplacian(frame,cv2.CV_64F)
    
#The Sobel Operator is a discrete differentiation operator. It computes an approximation of the gradient of an image intensity function.
#The Sobel Operator combines Gaussian smoothing and differentiation.

    
    sobelx = cv2.Sobel(frame,cv2.CV_64F,1,0,ksize=5)
    sobely = cv2.Sobel(frame,cv2.CV_64F,0,1,ksize=5)

    cv2.imshow('Original',frame)
    cv2.imshow('Mask',mask)
    cv2.imshow('laplacian',laplacian)
    cv2.imshow('sobelx',sobelx)
    cv2.imshow('sobely',sobely)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()