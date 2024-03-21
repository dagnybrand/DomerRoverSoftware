from serial import Serial
from time import sleep

if __name__ == "__main__":
    serial_port = "/dev/ttyS0"
    baudrate = 38400

    roboclaw = Serial(serial_port, baudrate, timeout=1)

    while True:
        roboclaw.write(chr(94))
        sleep(2)
        roboclaw.write(chr(64))
        sleep(2)
