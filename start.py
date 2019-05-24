from threading  import Thread
from Speechmanager.speech_manager import speech as sp
import time
from Speechmanager.TTS import tts
#background thread
def background():
  while(True):
      print("in background thread\n")
      command = sp.gstt()
      #tts.say('give your command')
      #time.sleep(4)
      #command = 'suno'
      if command=="listen" or command == 'suno':
        t=Thread(target=assistant,args="")
        t.start()
        t.join()

#application thread
def assistant():
    print("in assistant")
    from index import mainloop
    re=mainloop()
print("starting background thread\n")
b=Thread(target=background,args="")
b.start()
b.join()
