import speech_recognition as sr
from TTS import tts

r = sr.Recognizer()
sample_rate = 48000
chunk_size = 2048

class speech:
        # Speech recognition using Google Speech Recognition
    @staticmethod
    def gstt():
        try:
            with sr.Microphone(sample_rate = sample_rate,chunk_size = chunk_size) as source:
                print("say something")
                tts.say('give your command')
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
                if audio:
                    return r.recognize_google(audio)
                # for testing purposes, we're just using the default API key
                # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
                # instead of `r.recognize_google(audio)`
                else:
                    return ""

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
