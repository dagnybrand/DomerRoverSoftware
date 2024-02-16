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

    for i in x:
        for j in y:
            pixel_center = hsv[i, j]
            hue_value = pixel_center[0]
            if hue_value < 50:
                orange_ct += 1
    
    if orange_ct > 10000:
        cv.circle(frame, (300, 300), 50, (255, 255, 255), 3)
        
    
    cv.imshow("frame", frame)
    key = cv.waitKey(1)
    if key == ord("q"):
        break
cap.release()
cv.destroyAllWindows()
