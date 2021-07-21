# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 16:14:16 2021

@author: ThisPC
"""

import pytesseract
import cv2
import matplotlib.pyplot as plt

# load the original image
image = cv2.imread(r'C:\Users\ThisPC\Downloads\.jpg')
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# get co-ordinates to crop the image
line_items_coordinates = image.shape[0]
c = line_items_coordinates[1]

#cropping image img = image[y0:y1, x0:x1]
img = image[c[0][1]:c[1][1], c[0][0]:c[1][0]]    

plt.figure(figsize=(10,10))
plt.imshow(img)

# convert the image to black and white for better OCR
ret,thresh1 = cv2.threshold(img,120,255,cv2.THRESH_BINARY)

# pytesseract image to string to get results
text = str(pytesseract.image_to_string(thresh1, config='--psm 6'))
print(text)