import speech_recognition as sr
from word import wordlib
from validcommands import commands
from Commands import mswordcommands as bc
import Speechmanager.analizer as al
from Speechmanager.speech_manager import speech as sp
import subprocess
import time
from Speechmanager.TTS import tts
from Write import writing
from Operate import operate
# Record Audio
r = sr.Recognizer()

boldActivator = False
underlineActivator = False
italicActivator = False

#starting of msword module
def main():
    try:
        subprocess.call('start winword',shell = True)
        commands.activatemswordcommandset()
        wordcommander()
    except OSError:
        print('wrong command ,Such type of command doesnot exist')
        tts.say('wrong command ,Such type of command doesnot exist')

#funtion for stoping msword
def stopword():
    try:
        subprocess.call('taskkill /im winword.exe /f',shell = True)
        import index
        index.mainloop()
    except OSError:
        print('wrong command ,Such type of command doesnot exist')
        tts.say('wrong command ,Such type of command doesnot exist')

def wordcommander():
    while True:
        command = sp.gstt()
        #tts.say('give your command')
        #time.sleep(4)
        #command = 'likho'

        if command:
            command = al.analize(command)
            if command:
                try:
                    #print(command)
                    if command == 'close msword' or command == 'msword band karo':
                        tts.say('msword closed successfully')
                        break

                    elif command == "read" or command == 'padho':
                        with keyboard.pressed(Key.ctrl):
                            keyboard.press('a')
                            keyboard.release('a')
                        with keyboard.pressed(Key.alt):
                            keyboard.press('s')
                            keyboard.release('s')

                    elif command == "write" or command == 'likho':
                        writing.write()

                    #tts.say('give your command')
                    #time.sleep(4)
                    #command = 'msword band karo'

                    elif len(bc.mswordcommandsdict[command]) is 1:
                        operate.output1(bc.mswordcommandsdict[command][0])

                    elif len(bc.mswordcommandsdict[command]) is 2:
                        operate.output2(bc.mswordcommandsdict[command][0],bc.mswordcommandsdict[command][1])

                    elif len(bc.mswordcommandsdict[command]) is 3 :
                        operate.output3(bc.mswordcommandsdict[command][0],bc.mswordcommandsdict[command][1],bc.mswordcommandsdict[command][2])

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
    #stop msword
    stopword()
