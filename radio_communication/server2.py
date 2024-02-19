import socket
from pi_to_arduino import Arduino

host = socket.gethostname()
port = 5000

server = socket.socket()
server.bind((host, port))

server.listen(4)
connection, address = server.accept()

print("Connection from " + str(address))
print(host, port)

arduino = Arduino()

while True:
    data = connection.recv(1024).decode()
    if not data:
        break

    if data == '1' or data == '2' or data == '3' or data == '4':
        arduino.send_signal(data.encode())

    print("From connection: " + str(data))

    #data = input("Enter server response: ")
    #connection.send(data.encode())

connection.close()
