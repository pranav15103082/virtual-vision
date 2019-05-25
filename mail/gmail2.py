import sys
sys.path.append("C:\Users\Pranav\Desktop\\vision7")
import smtplib
from Speechmanager.speech_manager import speech as sp
from Speechmanager.TTS import tts
from email.mime.text import MIMEText
def gmailer():
    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login(your email address, your password)

    tts.say("give me reciever email id")
    recieveremail = str(sp.gstt())
    recieveremail = recieveremail + '@gmail.com'
    print(recieveremail)

    # message to be sent
    tts.say("start writing mail")
    message = ''

    while True:
        text = sp.gstt()
        text = str(text)
        print(text)
        if text.lower() == 'stop writing':
            break
        text = text+" "
        message=message+text
    print(message)

    # sending the mail
    s.sendmail(your email address, recieveremail, message)

    x = "mail sent successfully to"+recieveremail
    tts.say(x)
    # terminating the session
    s.quit()
