#import impotant library
import cv2
import numpy as np
import matplotlib.pyplot as plt
#read the image
img = cv2.imread(r"C:\Users\AMIT\Downloads\watch_image.jpg", cv2.IMREAD_COLOR)
#draw a line on the images
cv2.line(img, (0,0),(150,180), (300,300,300), 15)
#draw a rectangle on the images
cv2.rectangle(img, (15,25), (150,200), (0,300,0),10)
#draw a circle
cv2.circle(img, (60,70), 50, (0, 0 ,200), -1 )
#draw a ploygon
pts =np.array([[10,15], [20,30], [70,20], [50,10]], np.int32)
cv2.polylines(img, [pts], True, (0,255,255), 5)
#write s this is Amit on the images
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'this is Amit', (0,150), font, 0.3, (200,255, 255), 1, cv2.LINE_AA)
cv2.imshow('images', img)
cv2.waitKey(0)
cv2.destroyAllWindows()