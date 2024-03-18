#control the robotic arm using the PS4 controller

#preparing for PWM
import RPi.GPIO as GPIO
GPIO.setwarnings(False)

#using pins 15 and 16, GPIO 22 and 23
actuator1 = 22
actuator2 = 23
dir1 = 24
dir2 = 27

GPIO.setmode(GPIO.BCM) #means we are using the GPIO numbers not pin numbers
GPIO.setup(actuator1, GPIO.OUT)
GPIO.setup(actuator2, GPIO.OUT)
GPIO.setup(dir1, GPIO.OUT)
GPIO.setup(dir2, GPIO.OUT)
a1 = GPIO.PWM(actuator1, 1000)
a2 = GPIO.PWM(actuator2, 1000)
GPIO.output(dir1, GPIO.HIGH)
GPIO.output(dir2, GPIO.HIGH)

a1.start(0)
a2.start(0)

#server code
import socket
import pickle

host = "10.7.7.136"
port = 5002

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(1)

conn, addr = s.accept()

##actuator position reading code
### DOESNT WORK YET

import board
import busio
#i2c = busio.I2C(board.SCL, board.SDA)

import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

#ads = ADS.ADS1015(i2c)
#chan1 = AnalogIn(ads, ADS.P1)
#chan2 = AnalogIn(ads, ADS.P0)



###roboclaw code
#s1 to GPIO 14
#s2 to GPIO 15
from roboclaw_3 import Roboclaw
roboclaw = Roboclaw("/dev/ttyS0", 38400)
address = 0x80
roboclaw.Open()

#servo code
from gpiozero import Servo
import pigpio

#use GPIO25
servo = 25
sval = 1500
spwm = pigpio.pi()
spwm.set_mode(servo, pigpio.OUTPUT)
spwm.set_PWM_frequency(servo, 50)

#camera code
import cv2
import numpy as np
import sys
import struct

cap = cv2.VideoCaputure(0)


###MAIN
while True:
    data= conn.recv(4096)
    if not data:
        break
    
    # data.seek(0)
    
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

    #now coding arm controls
    #actuator 1 with y axis left joystick
    a1speed = a_lefty1 * 100
    if a1speed >= 0:
        GPIO.output(dir1, GPIO.LOW)
        a1.ChangeDutyCycle(a1speed)
    else:
        GPIO.output(dir1, GPIO.HIGH)
        a1.ChangeDutyCycle(-a1speed)

    #actuator 2 with y axis right joystick
    a2speed = a_righty1 * 100
    if a2speed >= 0:
        GPIO.output(dir2, GPIO.LOW)
        a2.ChangeDutyCycle(a2speed)
    else:
        GPIO.output(dir2, GPIO.HIGH)
        a2.ChangeDutyCycle(-a2speed)

    #control rotation with x axis of right joystick
    m1speed = a_rightx1 * 127
    m1speed = int(m1speed)
    if m1speed >=0:
        roboclaw.BackwardM1(address, m1speed)
    else:
        roboclaw.ForwardM1(address, -m1speed)

    #control servo with left and right bumpers
    if b_rbumper1 == 1:
        if sval > 502:
            sval = sval - 1
            spwm.set_servo_pulsewidth(servo,sval)
        else:
            print("minimum servo value")
    if b_lbumper1 == 1:
        if sval < 2498:
            sval = sval + 1
            spwm.set_servo_pulsewidth(servo,sval)
        else:
            print("maximum servo value")

    #print("actuator positions")
    #print(chan1.value, chan1.voltage)
    #print(chan2.value, chan2.voltage)

    #camera code
    ret, frame = cap.read()
    viddata = pickle.dumps(frame)

    message_size = struct.pack("=L", len(viddata))
    conn.sendall(message_size + viddata)








conn.close()


