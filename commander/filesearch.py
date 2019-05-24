import speech_recognition as sr
import os
import win32com.client as wincl
r = sr.Recognizer()

speak=wincl.Dispatch("SAPI.SpVoice")
def get_drives():
    response = os.popen("wmic logicaldisk get caption")
    list1 = []
    total_file = []
    for line in response.readlines():
        line = line.strip("\n")
        line = line.strip("\r")
        line = line.strip(" ")
        if (line == "Caption" or line == ""):
            continue
        list1.append(line)
    return list1

def find(filename):
    #cc=gstt()
    #print(cc)
    n=1
    ans=[]
    drive=get_drives()
    for i in drive:
        print(i)
    for x in drive:
        print(x)
        try:
            os.chdir(x+'/')
            os.system("dir "+filename+" /s/p > g:/new1.txt")
            print('here')
            file=open("g:/new1.txt",'r')

            for line in file:
                #print(n)
                if ((n+1) %5) is 0 :
                    str = (line.split(' '))
                    if(str[1] == "Directory"):
                        ans.append(str[3])
                        print(str[3])
                n+=1
        except:
            pass
    print("ans:")
    leng = len(ans)

    if (leng > 1):
        index=1
        index_to_file_map={}
       # print(leng)

        speak.Speak("%d Files found"%(leng))
       #+ " files found")
        for i in ans:
            speak.Speak(i)
            speak.Speak("Is It Your File")
            command=gstt()
            print(command)
            if(command=='yes'):
                os.chdir("c:")
                ss = ans[0][:len(ans[0]) - 1] + "/" + filename
                print(ss)
                os.system(ss)
                break

        '''
        for i in ans:
            index_to_file_map[index]=i
            index+=1
        print(index_to_file_map[1])
        '''

    elif (leng == 1):
        os.chdir("c:")
        ss = ans[0][:len(ans[0]) - 1] +"/"+ filename
        print(ss)
        os.system(ss)
    else:
        speak.Speak("No files found")



def gstt():
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
        return r.recognize_google(audio)
