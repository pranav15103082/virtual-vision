from pynput.keyboard import Key, Listener , Controller
keyboard = Controller()

def output1(key1):
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)


def output2(key1,key2):
    #time.sleep(2)
    with keyboard.pressed(key1):
        keyboard.press(key2)
        keyboard.release(key2)

def output3(key1,key2,key3):
    #time.sleep(2)
    with keyboard.pressed(key1):
        with keyboard.pressed(key2):
            keyboard.press(key3)
            keyboard.release(key3)
