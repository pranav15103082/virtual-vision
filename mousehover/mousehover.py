import subprocess
from Operate import operate
from pynput.keyboard import Key, Listener , Controller
keyboard = Controller()

#starting of narrator application
def main():
    try:
        operate.output3(Key.ctrl,Key.cmd,Key.enter)
    except OSError:
        print('wrong command ,Such type of command doesnot exist')
        tts.say('wrong command ,Such type of command doesnot exist')

#command for closing nvda application
def stop_mousehover():
    try:
        operate.output2(Key.caps_lock,Key.esc)
    except OSError:
        print('wrong command ,Such type of command doesnot exist')
        tts.say('wrong command ,Such type of command doesnot exist')
