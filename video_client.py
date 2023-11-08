import cv2
import matplotlib.image as img
import socket
from io import BytesIO
from PIL import Image
from PIL import ImageFile
import os
import numpy
import base64

ImageFile.LOAD_TRUNCATED_IMAGES = True

host = "10.7.188.188"
port = 5004

client = socket.socket() # initialize object
client.connect((host, port))

while True:
	en_photo = client.recv(921600)
	image = numpy.asarray(bytearray(en_photo), dtype='uint8')
	image = cv2.imdecode(image, cv2.IMREAD_COLOR)
	#image_arr = numpy.frombuffer(en_photo, numpy.uint8)
	#print(len(en_photo))
	#if len(en_photo) != 0:
#		image = cv2.imdecode(image_arr, cv2.IMREAD_COLOR)
#		if type(image) is type(None):
#			continue
#	else:
#		continue
	#stringData = client.recv(1<<16).decode("utf-8")
	#data = numpy.frombuffer(base64.b64decode(stringData), numpy.uint8)
	#image = cv2.imdecode(data, cv2.IMREAD_COLOR)
#	with open('./test_image.png', "wb") as f:
#		bytes = client.recv(10000000)
#		f.write(bytes)
#	if os.path.exists('./test_image.png'): 
#		im = Image.open('./test_image.png')
#		open('./test_image.png', 'w').close()
#		im.show()
	if type(image) is not type(None):
		cv2.imshow('Video stream', image)
		k = cv2.waitKey(1000)
		if k != -1:
			break
