from chrome import chromelib
from validcommands import commands
from Commands import browsercommands as bc
import Speechmanager.analizer as al
from Speechmanager.speech_manager import speech as sp
import subprocess
import time
from Speechmanager.TTS import tts
from Operate import operate
from pynput.keyboard import Key, Listener , Controller
keyboard = Controller()
from Mousehover import mousehover


#starting of chrome module
def main():
    try:
        subprocess.call('start chrome',shell = True)
        commands.activatebrowsercommandset()
        chromecommander()
    except OSError:
        print('wrong command ,Such type of command doesnot exist')
        tts.say('wrong command ,Such type of command doesnot exist')

#commands for chrome
def chromecommander():
    while True:
        command = sp.gstt()
        if command:
            command = al.analize(command)
            if command:
                try:
                    print(command)

                    if command == "write" or command == 'likho':
                        chromelib.write()
                    elif command == "quit chrome" or command == 'chrome band karo':
                        tts.say('chrome closed successfully')
                        with keyboard.pressed(Key.ctrl):
                            with keyboard.pressed(Key.shift):
                                keyboard.press('q')
                                keyboard.release('q')
                        break
                    elif command == 'start mousehover' or command == 'mousehover shuru karo':
                        mousehover.main()
                    elif(command == 'stop mousehover') or command == 'mousehover band karo':
                        mousehover.stop_mousehover()
                    elif command == "go" or command == 'khojo':
                        keyboard.press(Key.enter)
                        keyboard.release(Key.enter)
                        tts.say('page loaded successfully')

                    elif len(bc.browsercommandsdict[command]) is 2:
                        operate.output2(bc.browsercommandsdict[command][0],bc.browsercommandsdict[command][1])

                    elif len(bc.browsercommandsdict[command]) is 3 :
                        operate.output3(bc.browsercommandsdict[command][0],bc.browsercommandsdict[command][1],bc.browsercommandsdict[command][2])


                    time.sleep(1)

                except ValueError:
                    print('ValueError: key is a string, but its length is not 1')
                    tts.say('ValueError: key is a string, but its length is not 1')


            else:
                print('analizer doesnot work, Check its settings')
                tts.say('analizer doesnot work, Check its settings')
        else:
            print('error in google speech recognition')
            tts.say('error in google speech recognition')
