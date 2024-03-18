from roboclaw_3 import Roboclaw
from time import sleep

if __name__ == "__main__":
    address = 0x80
    #address = 128
    roboclaw = Roboclaw("/dev/ttyS0", 38400)
    roboclaw.Open()

    accel = 100000
    speed = 500000
    deccel = 100000
    position = 100000

    while True:
        roboclaw.SpeedAccelDeccelPositionM1(address, accel, speed, deccel, position, 1)
        sleep(5)
        print('changing')
        roboclaw.SpeedAccelDeccelPositionM1(address, accel, speed, deccel, 0, 1)
        sleep(5)
        print('changing 2')
