#import the important library
import cv2
import numpy as np
import matplotlib as plt
#capture video
cap = cv2.VideoCapture(0)
#save the video file
fourcc = cv2.VideoWriter_fourcc(* 'avid')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))
while True:
    ret, frame = cap.read() # read the frame
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY) #read the frame in gray
    out.write(frame)
    cv2.imshow("frame", frame) #show the frame
    cv2.imshow("gra_frame", gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()