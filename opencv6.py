# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 14:46:37 2021

@author: ThisPC
"""
import cv2
import numpy as np
cap=cv2.VideoCapture(1)
while True:
    #_ is basically used to easily convert in function
    _,frame =cap.read()
    
    #hsv is used determine unique color or hue set value
    hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_red = np.array([150,150,50])
    upper_red = np.array([180, 255, 150])
    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow('frame', mask)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
    
cv2.destroyAllWindows()
cap.release()  
    
