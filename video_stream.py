import random
import socket, select
import cv2
from io import BytesIO
from PIL import Image

def connect():
	#host = "192.168.188.2"
	host = "10.7.188.188"
	port = 5000

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
		result, frame = cv2.imencode('.jpg', frame, encode_param)
		#cv2.imwrite(filename, image)
		#color_coverted = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) 
		connection.send(frame)
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
