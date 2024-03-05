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
    #print(height, width)

    x = range(0, height, 5)
    y = range(0, width, 5)
    xCo = -10
    yCo = -10
    orange_ct = 0
    lower_orange = np.array([0, 150, 150])
    upper_orange = np.array([50, 255, 255])

    mask = cv.inRange(hsv, lower_orange, upper_orange)
    res = cv.bitwise_and(frame,frame, mask= mask)
    '''
    for i in x:
        for j in y:
            pixel_center = hsv[i, j]
            hue_value = pixel_center[0]
            if hue_value < 50:
                orange_ct += 1
                xCo = i
                yCo = j
                frame[i, j] = [255,255,255]
    '''
    #if orange_ct > 10000:
     #   cv.circle(frame, (xCo, yCo), 50, (255, 255, 255), 3)
     #   cv.circle(frame, (150, 150), 50, (255,255,255), 3)
    if xCo > 0:
        cv.circle(frame, (xCo, yCo), 50, (255, 255, 255), 3)
        
    
    cv.imshow("frame", frame)
    cv.imshow("mask", mask)
    cv.imshow("res", res)
    key = cv.waitKey(1)
    if key == ord("q"):
        break
cap.release()
cv.destroyAllWindows()