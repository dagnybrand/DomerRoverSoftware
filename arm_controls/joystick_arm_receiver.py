# receive joystick data
import socket
import pickle

# host = "10.7.7.136"
host = "localhost"
port = 5002

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)

conn, addr = s.accept()

while True:
    data = conn.recv(4096)
    if not data:
        break

    joystick_data = pickle.loads(data)

    a_lt1 =         joystick_data[0]
    a_rt1 =         joystick_data[1]
    b_lbumper1 =    joystick_data[2]
    b_rbumper1 =    joystick_data[3] 
    a_leftx1 =      joystick_data[4]
    a_lefty1 =      joystick_data[5]
    a_rightx1 =     joystick_data[6]
    a_righty1 =     joystick_data[7]
    b_leftIn1 =     joystick_data[8]
    b_rightIn1 =    joystick_data[9]  
    b_x1 =          joystick_data[10] 
    b_circle1 =     joystick_data[11] 
    b_square1 =     joystick_data[12]  
    b_triangle1 =   joystick_data[13] 
    b_padUp1 =      joystick_data[14]  
    b_padDown1 =    joystick_data[15]  
    b_padLeft1 =    joystick_data[16] 
    b_padRight1 =   joystick_data[17]


conn.close()