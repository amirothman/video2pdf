import copy
import cv2
from scipy import spatial
import numpy as np

sourceVideo = "This_Cool_Machine_Turns_Waste_Paper_Into_New_Paper_Within_Just_3_Minutes-LL9YgFEHW5U.mp4"
sourceVideo = "Sutherland-Hodgman_Polygon_Clipping_Algorithm-S091lKYWbSs.mp4"
cap = cv2.VideoCapture(sourceVideo)
cv2.waitKey(1)
counter = 0
while(cap.isOpened()):
    ret, frame = cap.read()
    if (type(frame) == type(None)):
        break
    if (cv2.waitKey(1) & 0xFF == ord('q')) or frame.size == 0:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if counter % 30 == 0:
        print(counter)
    counter += 1

cap.release()

