import socket

#host = "169.254.139.218"
host = "10.7.7.136"
port = 5000

server = socket.socket()
server.bind((host,port))

server.listen(4)
connection,address = server.accept()

print("Connection from " + str(address))
print(host,port)

#set m1 parameters
accel = 2500
speed = 5000
deccel = 2500
position = 0
position2 = 0

from roboclaw_3 import Roboclaw
from time import sleep
from gpiozero import Servo
import pigpio


#define servo pin

#some varying servo code
#servo = Servo(25)
servo = 25
sval = 1500
pwm = pigpio.pi()
pwm.set_mode(servo, pigpio.OUTPUT)
pwm.set_PWM_frequency(servo, 50)

address = 0x80
address2 = 0x81
roboclaw = Roboclaw("/dev/ttyS0", 38400)
roboclaw.Open()
#roboclaw2 = Roboclaw("/dev/ttyAMA1", 38400)
#roboclaw2.Open()

while True:
    data = connection.recv(1024).decode()
    if not data:
        break
    print(data)
    print("From connection: " + str(data))

    if 'j' in data:
        position += -500 * data.count('j')
        print('m1 ' + str(position))
        roboclaw.SpeedAccelDeccelPositionM1(address, accel, speed, deccel, position, 1)
    if 'l' in data:
        position += 500 * data.count('l')
        print('m1'+ str(position))
        roboclaw.SpeedAccelDeccelPositionM1(address, accel, speed, deccel, position, 1)
    if 'i' in data:
        position2 += 500 * data.count('i')
        print('m2 ' + str(position2))
        roboclaw.SpeedAccelDeccelPositionM2(address, accel, speed, deccel, position2, 1)
    if 'k' in data:
        position2 += -500 * data.count('k')
        print('m2 ' + str(position2))
        roboclaw.SpeedAccelDeccelPositionM2(address, accel, speed, deccel, position2, 1)
    if 'n' in data:
        if sval > 502:
            sval = sval - 3 * data.count('n')
            pwm.set_servo_pulsewidth(servo, sval)
        else:
            print("minimum servo value exceeded")
        

        #if sval <= -1:i
        #    sval += 0.05 * data.count('n')
        #    if sval < 1:
        #        servo.value = sval
        #    print('s1' + str(sval))
       # else:
       #     print("servo value exceeded, go other direciton")
    if 'm' in data:
        #should be better code here then below, safe vlaues from 500-2500
        if sval < 2498:
            sval = sval + 3 * data.count('m')
            pwm.set_servo_pulsewidth(servo, sval)
        else:
            print("maximum servo value exceeded")

        #if sval > -1:
        #    sval += -.05 * data.count('m')
        #    if sval > -1:
        #        servo.value = sval
        #    print('s1' + str(sval))
            
       # else:
       #     print("servo value exceeded, go other direction")

   # if 'o' in data:
   #     roboclaw2.BackwardM2(address2, 60)
   #     print('actuator backward')
   # if 'p' in data:
    #    roboclaw2.ForwardM2(address2, 60)
   #     print('actuator forward')
 #   if 'x' in data:
  #      roboclaw2.ForwardM2(address2, 0)
        


    

connection.close()
