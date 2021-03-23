import numpy as np
import cv2
import argparse
import imutils

image = cv2.imread(r"C:\Users\ThisPC\Downloads\watch.jfif")
cv2.imshow("images", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
#Rotate the images
# loop over the rotation angles

for angle in np.arange(0, 360, 15):
	rotated = cv2.rotate(image, angle)
	cv2.imshow("Rotated (Problematic)", rotated)
	cv2.waitKey(0)

# loop over the rotation angles again, this time ensuring
# no part of the image is cut off

for angle in np.arange(0, 360, 15):
	rotated = imutils.rotate_bound(image, angle)
	cv2.imshow("Rotated (Correct)", rotated)
	cv2.waitKey(0)
