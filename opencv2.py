# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 11:25:51 2021

@author: ThisPC
"""

import cv2

import numpy as np
import matplotlib.pyplot as plt
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))
while True:
    ret, frame = cap.read()
    gray= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()