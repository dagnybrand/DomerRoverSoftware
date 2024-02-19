# https://stackoverflow.com/questions/30988033/sending-live-video-frame-over-network-in-python-opencv#comment97581958_30988516

import pickle
import socket
import struct

import cv2

#HOST = "10.7.188.188"
#HOST = 'localhost'
#PORT = 5000
HOST = "169.254.139.218"
PORT = 50010

clientsocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientsocket.connect((HOST,PORT))

data = b'' ### CHANGED
payload_size = struct.calcsize("=L") ### CHANGED

while True:

    # Retrieve message size
    while len(data) < payload_size:
        data += clientsocket.recv(4096)

    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack("=L", packed_msg_size)[0] ### CHANGED

    # Retrieve all data based on message size
    while len(data) < msg_size:
        data += clientsocket.recv(4096)

    frame_data = data[:msg_size]
    data = data[msg_size:]

    # Extract frame
    frame = pickle.loads(frame_data)

    # Display
    cv2.imshow('frame', frame)
    cv2.waitKey(1)
