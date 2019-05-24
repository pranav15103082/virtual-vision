import sys
sys.path.append("C:\Users\Shadab Khan\Desktop\\vision7")

from Speechmanager.speech_manager import speech as sp
import Speechmanager.analizer as al
from Speechmanager.TTS import tts
from Word import wordmain
from Mousehover import mousehover
from Speechmanager.TTS import tts
from Browser import ChromeMain
from validcommands import commands as co
import findmain as fs
import time

from Mail import gmail2

#core loop of application
class commander:
    @staticmethod
    def main():
        #while True:
            co.activatesystemcommandset()
            #google speech to text recognition
            command = sp.gstt()
            #tts.say('give your command')
            #time.sleep(5)
            #command = 'msword khole'
            tts.say(command)
            if command:
                #analize given command
                command = al.analize(command)
                print(command)
                if command == "open msword" or command == 'msword khole':
                    tts.say('msword opened successfully')
                    wordmain.main()
                elif command == "start mousehover" or command =='mousehover khole':
                    mousehover.main()
                elif command == "stop mousehover" or command == 'mousehover band karo':
                    mousehover.stop_mousehover()
                elif command == "open chrome" or command == 'chrome kholo':
                    ChromeMain.main()
                elif command=="find file" or command == 'file khojo':
                    fs.type()
                elif command =="send mail":
                    gmail2.gmailer()

                #elif command == "exit" or command == 'smapat karo':
                    #break

            else:
                tts.say('Check settings again')
                print('Check settings again')
