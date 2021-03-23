#import the important library
import numpy as np
import cv2
import imutils
from imutils.perspective import four_point_transform
from imutils import contours
#read the images
image = cv2.imread(r"C:\Users\ThisPC\Downloads\omr_finding_bubbles.jpg")
#print the images
#cv2.imshow("OMR", image)
#define Answer_key
#since Answer_keys in dictionary datatypes becuse it's mapping the question numbers
Answer_keys = {0:1, 1:3, 2:4, 3:2, 4:3}
#convert the images in gray scale
gry = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#Convert the images in Gaussian blurs
#Gaussian blur is define as area inclosed the curve
#Gaussian blur is used to reduce the high frequencyt noise
blrd = cv2. GaussianBlur(gry, (5,5), 0)
# Canny is used to detect the corner
edgd = cv2. Canny(blrd, 75,200)
#cv2.imshow("gray scale", gry)
#cv2.imshow("Gausian_Blured", blrd)
#cv2.imshow("canny_detection", edgd)
'''
In the above we see that we can apply "silhouette " (Silhouette is basically known darkest images identification)

in our problem statements we see that there are answered options are darkest so this method is beneficial for us

apply a marker to obtaining a top-down , and  Bird eye view

Apply silhouette methods

'''


cnts = cv2.findContours(edgd.copy(), cv2.RETR_EXTERNAL,
                        cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

docCnt = None

if len(cnts) > 0:
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)

    #for sorted contour
    for c in cnts:
        peri = cv2.arcLength(c, True)
        apprx = cv2.approxPolyDP(c, 0.02*peri, True)

        if len(apprx) == 4:
            docCnt = apprx
            break

            cv2.imread("docCnt")
            cv2.imread("cnts")
            cv2.imread("apprx")
            cv2.imshow("Destructed_images", docCnt)


            cv2.waitKey(0)
            cv2.destroyAllWindows()