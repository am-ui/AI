# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 15:21:28 2021

@author: ThisPC
"""

import cv2
import numpy as np

img = cv2.imread(r'C:\Users\ThisPC\Downloads\green-background.jpeg')
fgbg = cv2.createBackgroundSubtractorMOG2()

fgmask = fgbg.apply(img)

cv2.imshow('fgmask', fgmask)
cv2.imshow('orignal', img)

cv2.waitKey(0)
cv2.destroyAllWindows()