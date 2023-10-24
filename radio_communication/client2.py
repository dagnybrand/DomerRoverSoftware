import socket
from getkey import getkey, keys

#host = "169.254.147.106" # pi
host = socket.gethostname() # home computer
port = 5000

client = socket.socket()
client.connect((host, port))

while True:
    key = getkey()
    if (key == 'x'):
        break
    encoded = key.encode()
    client.send(encoded)
    #data = client.recv(1024).decode()


    #print('Received from server: ' + data)

client.close()
