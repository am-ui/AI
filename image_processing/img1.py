# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 10:53:11 2021

@author: ThisPC
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt_imshow

#start the camera
cap = cv2.VideoCapture(0)
#save the video
fourcc = cv2.VideoWriter_fourcc(*'XVID')
#save the images in desired resolutions
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
#open the camera untill found
while(True):
    ret, frame = cap.read()
    #show the capture video
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
 
cap.release()
cv2.destroyAllWindows()