# Takes in keyboard inputs as long as the key is pressed - not just when key is released
# Sends inputs to arduino in the form of numbers
# Only works if keyboard is directly connected to raspberry pi. Should only be used to test; not final product

import keyboard
from pi_to_arduino import Arduino

arduino = Arduino()

while True:
    if (keyboard.is_pressed("w")):
        arduino.send_signal(b"1")
    elif (keyboard.is_pressed("a")):
        arduino.send_signal(b"3")
    elif (keyboard.is_pressed("s")):
        arduino.send_signal(b"2")
    elif (keyboard.is_pressed("d")):
        arduino.send_signal(b"4")
