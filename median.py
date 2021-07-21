# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 18:49:42 2021

@author: ThisPC
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt_imshow
import time
import os


img = cv2.imread(r"C:\Users\ThisPC\Downloads\balloons_noisy.png")

#print(img)

#median blur of the images
median = cv2.medianBlur(img, 5)
cv2.imshow("images", median)

cv2.waitKey(0)
cv2.destroyAllWindows()