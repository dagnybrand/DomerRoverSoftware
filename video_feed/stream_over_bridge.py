import random
import socket, select
import cv2
from io import BytesIO
from PIL import Image
import numpy
import base64

def connect():
	#host = "192.168.188.2"
	host = "10.7.188.188"
	port = 5004

	server = socket.socket()
	server.bind((host, port))

	server.listen(4)
	connection, address = server.accept()

	print("Connection from " + str(address))
	print(host, port)
	
	filename = './testimage.jpg'
	
	cam = cv2.VideoCapture(0)
	
	encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]

	while True:
		ret, image = cam.read()
		cv2.imshow('video stream', image)
		k = cv2.waitKey(1000)
		if k != -1:
			break
		if ret == True:
			en_photo = cv2.imencode('.jpg', image)[1]
			data_encode = numpy.array(en_photo).tobytes()
			connection.send(data_encode)
		else:
			pass
		#result, imgencode = cv2.imencode('.jpg', image, encode_param)
		#data = numpy.array(imgencode)
		#stringData = base64.b64encode(data)
		#cv2.imwrite(filename, image)
		#color_coverted = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) 
		#connection.send(stringData)
		#with open(filename, "rb") as f:
		#	connection.send(f.read())
		
		#pil_image = Image.fromarray(color_coverted)
		#connection.send(pil_image)

def camerastream():	
	import cv2

	cam = cv2.VideoCapture(0)

	while True:
		ret, image = cam.read()
		cv2.imshow('Imagetest',image)
		k = cv2.waitKey(1)
		if k != -1:
			break
	cv2.imwrite(filename, image)
	cam.release()
	cv2.destroyAllWindows()
	
#camerastream()
connect()
