# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 11:08:17 2021

@author: ThisPC
"""

import numpy as np
import cv2
import matplotlib.pyplot as plt

img =cv2.imread(r"C:\Users\ThisPC\Downloads\Pic.jpg", cv2.IMREAD_GRAYSCALE)
"""
#IMREAD_COLOR =1
#IMREAD_UNCHANGED = -1
cv2.imshow('images', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
plt.imshow(img, cmap = 'gray', interpolation='bicubic')
plt.plot([50,100],[80,100],'c', linewidth=5)
plt.show()

cv2.imwrite('amit.png', img)
