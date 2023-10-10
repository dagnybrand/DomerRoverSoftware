import socket

host = "169.254.147.106"
port = 5000

client = socket.socket()
client.connect((host, port))

message = input("Enter message: ")

while message.lower().strip() != 'exit':
    encoded = message.encode()
    client.send(encoded)
    data = client.recv(1024).decode()


    print('Received from server: ' + data)

    message = input("enter message: ")

client.close()
