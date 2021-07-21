# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 17:10:11 2021

@author: ThisPC
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt_imshow
import time
import os


img = cv2.imread(r"C:\Users\ThisPC\bicubic.png")

#print(img)

#median blur of the images
median = cv2.medianBlur(img, 5)
dst = cv2.fastNlMeansDenoisingColored(median,None,10,10,7,21)
#show the orignal images
#cv2.imshow("Original image", img)
#show the blured images
#cv2.imshow("Median", median)
#Create our shapening kernel, it must equal to one eventually
kernel_sharpening = np.array([[-1,-1,-1], 
                              [-1, 9,-1],
                              [-1,-1,-1]])
# applying the sharpening kernel to the input image & displaying it.
sharpened = cv2.filter2D(dst, -1, kernel_sharpening)
#cv2.imshow("sharp", sharpened)
cv2.imwrite("rmblur.png", sharpened)


cv2.waitKey(0)
cv2.destroyAllWindows()