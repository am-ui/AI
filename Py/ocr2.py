# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 15:02:34 2021

@author: ThisPC
"""

import cv2
import matplotlib.pyplot as plt_imshow

import numpy as np
import pytesseract

img = cv2.imread(r"C:\Users\ThisPC\Downloads\download.png")
cv2.imshow('orignal', img)
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
digits :1
#str: "A"
if img['digits'] > 0:
	options = "outputbase digits"

# OCR the input image using Tesseract
text = pytesseract.image_to_string(rgb, config=options)
print(text)
plt_imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()