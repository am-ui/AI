# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 10:39:35 2021

@author: ThisPC
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt
facecascade = cv2.CascadeClassifier(r'C:\Users\ThisPC\Downloads\opencv-master\opencv-master\data\haarcascades\haarcascade_frontalface_default.xml')
eyecascade = cv2.CascadeClassifier(r"C:\Users\ThisPC\Desktop\haarcascades\haarcascade_eye.xml")
cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = facecascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        
        eyes = eyecascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
    
    