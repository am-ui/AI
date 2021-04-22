# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 16:53:59 2021

@author: AMIT
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt_imshow
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type = str, required = True, 
                help="path of the images")

args= vars(ap.parse_args())

#load the input images
print("[info] loading input images")
image = cv2.imread(args["image"])

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#apply histogram

equalized = cv2.equalizeHist(gray)

cv2.imshow("input", gray)
cv2.imshow("histogram", eqaulized)


cv2.waitkey(0)
cv2.destroyAllWindow()