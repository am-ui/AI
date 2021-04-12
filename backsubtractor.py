# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 18:55:50 2021

@author: ThisPC
"""

import cv2
import numpy as np
cap = cv2.VideoCapture(r'C:\Users\ThisPC\Downloads\people-walking.mp4')
fgbg = cv2.createBackgroundSubtractorMOG2()

while(1):
    ret, frame = cap.read()

    fgmask = fgbg.apply(frame)
 
    cv2.imshow('fgmask',frame)
    cv2.imshow('frame',fgmask)

    
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    

cap.release()
cv2.destroyAllWindows()