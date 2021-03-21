#import important library
import cv2
import numpy as np
import matplotlib.pyplot as plt
#read the images as gray
img = cv2.imread(r"C:\Users\AMIT\Downloads\watch_image.jpg", cv2.IMREAD_GRAYSCALE)
#show the images
#cv2.imshow("images", img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
#show thw images using matplotlib
#show the images in gray clor and in bicubic format
plt.imshow(img, cmap='gray', interpolation='bicubic')
#draw the line
plt.plot([40,100], [100,120], linewidth = 5)
plt.show()