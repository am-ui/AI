# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 10:17:42 2021

@author: AMIT
"""

"""
Histogram is used to boost or improve the contrast of the images, on gray scale.

there are two types of histogram
1. Equalization :- this operation is perform on the entire images or pixels . it is basic histogram

2. Adaptive :-this operation perform on the some grid or some specific part of the images

"""

"""
Simple Equalization methods
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt_imshow

image= cv2.imread(r"C:\Users\AMIT\Downloads\histo.jpg")

def plt_imshow(title, image):
    # convert the image frame BGR to RGB color space and display it
	image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
	plt.imshow(image)
	plt.title(title)
	plt.grid(False)
	plt.show()
    
# # construct the argument parser and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", type=str, required=True,
# 	help="path to the input image")
# args = vars(ap.parse_args())

# since we are using Jupyter Notebooks we can replace our argument
# parsing code with *hard coded* arguments and values
args = {
    "image": r"C:\Users\AMIT\Downloads\histo.jpg"
}

# load the input image from disk and convert it to grayscale
print("[INFO] loading input image...")
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# apply histogram equalization
print("[INFO] performing histogram equalization...")
equalized = cv2.equalizeHist(gray)

# show the original grayscale image and equalized image
cv2.imshow("Input", gray)
cv2.imshow("Histogram Equalization", equalized)



# # construct the argument parser and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", type=str, required=True,
# 	help="path to the input image")
# ap.add_argument("-c", "--clip", type=float, default=2.0,
# 	help="threshold for contrast limiting")
# ap.add_argument("-t", "--tile", type=int, default=8,
# 	help="tile grid size -- divides image into tile x time cells")
# args = vars(ap.parse_args())

# since we are using Jupyter Notebooks we can replace our argument
# parsing code with *hard coded* arguments and values
args = {
    "image": "images/dog.png",
    "clip": 2.0,
    "tile": 8
}


# load the input image from disk and convert it to grayscale
print("[INFO] loading input image...")
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# apply CLAHE (Contrast Limited Adaptive Histogram Equalization)
print("[INFO] applying CLAHE...")
clahe = cv2.createCLAHE(clipLimit=args["clip"],
	tileGridSize=(args["tile"], args["tile"]))
equalized = clahe.apply(gray)

# show the original grayscale image and CLAHE output image
plt_imshow("Input", gray)
plt_imshow("CLAHE", equalized)