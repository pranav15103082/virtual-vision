import filesearch as fs
from Speechmanager.TTS import tts
from Speechmanager.speech_manager import speech as sp

def type():
    tts.say('enter file name')
    faltu=sp.gstt()
    #filename=input('enter file name')
    fs.find('use.txt')
