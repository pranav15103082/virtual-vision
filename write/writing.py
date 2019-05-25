from Speechmanager.speech_manager import speech as sp
from pynput.keyboard import Key,Controller
from Speechmanager.TTS import tts
import time
keyboard = Controller()

#function for simply typing
def write():
    while True:
        command = sp.gstt()
        tts.say(command)
        #tts.say('give your command')
        #time.sleep(4)
        if command == "stop writing" or command == 'likhna band karo':
            tts.say('writing stopped')
            break
        elif command == "new line" or command == 'nayi rekha':
            new_line()
        elif command == "caps lock" or command == 'bade akshar':
            tts.say('capslock pressed')
            caps_lock()

        elif command == "full stop" or command == 'purnviram':
            keyboard.type(".")
        elif command == "comma" :
            keyboard.type(",")
        elif command == "hyphen":
            keyboard.type("-")
        elif command:
            keyboard.type(command+" ")
        #tts.say('give your command')
        #time.sleep(4)
        else:
            tts.say('error in speech recognition')
        time.sleep(4)

def new_line():
    with keyboard.pressed(Key.shift):
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

def caps_lock():
    keyboard.press(Key.caps_lock)
    keyboard.release(Key.caps_lock)
