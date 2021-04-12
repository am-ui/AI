# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 18:34:29 2021

@author: ThisPC
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
img1 = cv2.imread(r'C:\Users\ThisPC\Downloads\opencv-feature-matching-template.jpg')
img2 = cv2.imread(r'C:\Users\ThisPC\Downloads\opencv-feature-matching-image.jpg')

#define feature matchings

orb = cv2.ORB_create()
#define key point for detecting
kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 =orb.detectAndCompute(img2, None)
#find keypoint in the detectors
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck =True)
#find the matches
matches =bf.match(des1, des2)
#sort the matches
matches = sorted(matches, key = lambda x:x.distance)
#draw line for detected element
img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:30],None, flags=2)
plt.imshow(img3)
plt.show()