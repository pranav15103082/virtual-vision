import pyttsx3

#text to speech convertion (voice of zira)
class tts:
    @staticmethod
    def say(text):
        try:
            e = pyttsx3.init()
            e.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
            e.say(text)
            e.runAndWait()
        except RuntimeError:
            print('something wrong with output devices')
