from gpiozero import Servo
from time import sleep

servo = Servo(25)
val = 0

while True:
    servo.value = val
    sleep(0.1)
    val = val + .1

