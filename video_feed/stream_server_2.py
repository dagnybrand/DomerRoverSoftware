# https://stackoverflow.com/questions/30988033/sending-live-video-frame-over-network-in-python-opencv#comment97581958_30988516

import cv2
import numpy as np
import socket
import sys
import pickle
import struct

#HOST = "10.7.7.136"
#HOST = 'localhost'
HOST = "169.254.139.218"
     
PORT = 50010

cap=cv2.VideoCapture(-1, cv2.CAP_V4L)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#print('Socket created')

s.bind((HOST, PORT))
#print('Socket bind complete')
s.listen(10)
#print('Socket now listening')

conn, addr = s.accept()

while True:
    ret,frame=cap.read()

    #reducing image quality
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 10]
    result, encimg = cv2.imencode('.jpg', frame, encode_param)
    
    # Serialize frame
    data = pickle.dumps(encimg)

    # Send message length first
    message_size = struct.pack("=L", len(data)) ### CHANGED

    # Then data
    conn.sendall(message_size + data)
