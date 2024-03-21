import serial

class Arduino:

    def __init__(self):
        self.ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
        self.ser.reset_input_buffer()
        
    def send_signal(self, instr):
        self.ser.write(instr)
