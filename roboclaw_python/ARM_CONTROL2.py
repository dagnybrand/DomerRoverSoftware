from pynput.keyboard import Key,Listener

def on_press(key):
    print('{0} pressed'.format(key))
def on_release(key):
    print('{0} release'.format(key))
    if key == Key.esc:
        return False
with Listener(on_press=onpress, onrelease=onrelease) as listener:
    listener.join()

#set m1 parameters
accel = 10000
speed = 10000
deccel = 10000
position = 0

from roboclaw_3 import Roboclaw
from time import sleep

address = 0x80
roboclaw = Roboclaw("/dev/ttyS0", 38400)
roboclaw.Open()

while True:
    if 'j' in key:
        position += -100
        print(position)
        roboclaw.SpeedAccelDeccelPositionM1(address, accel, speed, deccel, position, 1)
    if 'l' in key:
        position += 100
        print(position)
        roboclaw.SpeedAccelDeccelPositionM1(address, accel, speed, deccel, position, 1)
        
        
