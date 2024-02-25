from __future__ import division
import sys
import cv2 as cv
#to show the image
from matplotlib import pyplot as plt
import numpy as np
from math import cos, sin

# utilizes default camera/webcam driver
cap = cv.VideoCapture(0)

# iterate through multiple frames, in a live video feed
while True:
    ret, frame = cap.read()
    if not ret:
        break
    # turning the frame to HSV color space
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    height, width, _ = frame.shape

    x = range(0, height, 10)
    y = range(0, width, 10)

    orange_ct = 0
    lower_orange = np.array([0, 150, 150])
    upper_orange = np.array([50, 255, 255])

    for i in x:
        for j in y:
            pixel_center = hsv[i, j]
            if all(pixel_center > lower_orange) and all(pixel_center < upper_orange):
                orange_ct += 1
    
    if orange_ct > 100:
        cv.putText(frame, 'ORANGE DETECTED', (50, 50), color=(255, 255, 255), fontFace= cv.FONT_HERSHEY_SIMPLEX, fontScale=1 )
        
    
    cv.imshow("frame", frame)
    key = cv.waitKey(1)
    if key == ord("q"):
        break
cap.release()
cv.destroyAllWindows()