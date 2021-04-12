# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 12:48:05 2021

@author: ThisPC
"""

import cv2
import numpy as np
img = cv2.imread(r'C:\Users\ThisPC\Downloads\old_book.jpg')
sharpen_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
sharpen = cv2.filter2D(img, -1, sharpen_kernel)

cv2.imshow('sharpen', sharpen)

retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)
cv2.imshow('pages', sharpen)
cv2.imshow('thresold', threshold)

grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
retval, threshold = cv2.threshold(grayscaled, 10, 255, cv2.THRESH_BINARY)
cv2.imshow('original',sharpen)
cv2.imshow('threshold',threshold)


th = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
cv2.imshow('original',sharpen)
cv2.imshow('Adaptive threshold',th)


cv2.waitKey(0)
cv2.destroyAllWindows()