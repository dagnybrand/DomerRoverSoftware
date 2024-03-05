from __future__ import division
import sys
import cv2 as cv
#to show the image
from matplotlib import pyplot as plt
import numpy as np
from math import cos, sin

import threading
from queue import Queue

def thread_fn(hsv, x0, xf, y0, yf, kernel_size):
    totals = [0, 0, 0]
    for x in range(x0, xf):
        for y in range(y0, yf):
            pixel_center = hsv[y, x]
            totals[0] = pixel_center[0]
            totals[1] = pixel_center[1]
            totals[2] = pixel_center[2]


    avgs = []
    avgs.append(totals[0] / (kernel_size*kernel_size))
    avgs.append(totals[1] / (kernel_size*kernel_size))
    avgs.append(totals[2] / (kernel_size*kernel_size))
    return x0, y0, avgs


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

    orange = False
    orange_loc = []
    lower_orange = np.array([0, 150, 150])
    upper_orange = np.array([50, 255, 255])

    kernel_size = 25
    step = 25
    ct = 0

    queue = Queue()

    for y in range(0, height, step):
        for x in range(0, width, step):
            threads = list()
            xf = x + kernel_size - 1 if x + kernel_size - 1 < width else width
            yf = y + kernel_size - 1 if y + kernel_size - 1 < height else height
            t = threading.Thread(target=lambda q, hsv, x0, xf, y0, yf, kernel_size: q.put(thread_fn(hsv, x0, xf, y0, yf, kernel_size)), args=(queue, hsv, x, xf, y, yf, kernel_size))
            threads.append(t)
            t.start()

    
    for t in threads:
        t.join()

    while not queue.empty():
        x0, y0, avgs = queue.get()
        if all(avgs > lower_orange) and all(avgs < upper_orange):
            orange = True
            orange_loc.append([x0, y0])

    if orange:
        cv.putText(frame, 'ORANGE DETECTED', (50, 50), color=(255, 255, 255), fontFace= cv.FONT_HERSHEY_SIMPLEX, fontScale=1 )


    cv.imshow("frame", frame)
    key = cv.waitKey(1)
    if key == ord("q"):
        break
cap.release()
cv.destroyAllWindows()