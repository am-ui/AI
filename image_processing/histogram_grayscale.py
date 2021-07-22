"""
Created on Thu Jul 22 10:59:33 2021

@author: ThisPC

"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

#read the image
img = cv2.imread(r'C:\Users\ThisPC\Downloads\man-walking-dog.jpg')
#cv2.imshow("orignal", img)
#print number of rows, column and chanel
#print(img)

#x = img.shape
#print number of pixels
#print(img.size)




#convert the images into grayscale
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#cv2.imshow('gray_scale', grey)
# Calculate histogram using cv2.calcHist()
hist = cv2.calcHist([img], [0], None, [256], [0,256])
cv2.imshow('histo', hist)
# Display the histogram
#plt.plot(hist)

plt.hist(img.flatten(), 256, [0,256])
#plt.show()

cv2.waitKey()
cv2.destroyAllWindows()