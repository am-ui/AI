# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 17:00:38 2021

@author: ThisPC
"""
import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
image = cv2.imread(r'C:\Users\ThisPC\Downloads\reciept.png')

image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
text = pytesseract.image_to_string(image, output_type='string')
print(text)
                     