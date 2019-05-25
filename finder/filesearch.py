import speech_recognition as sr
import os
import win32com.client as wincl
speak=wincl.Dispatch("SAPI.SpVoice")
def get_drives():
     response=os.popen("wmic logicaldisk get caption")
     list1=[]
     total_file=[]
     for line in response.readlines():
         line=line.strip("\n")
         line=line.strip("\r")
         line=line.strip(" ")
         if(line=="Caption"or line==""):
             continue
         list1.append(line)
     return list1
def findfile(filename):
     n=1
     ans=[]
     drive=["C:\\","D:\\","E:\\","F:\\"]
     for x in drive:
          print(x)
          try:
               os.chdir(x+'\\')
               os.system("dir "+filename+" /s/p >e:new1.txt")
               file=open("e:/new1.txt","r")
               for line in file:
                    print(n)
                    if (n+1)%5 is 0:
                        str=line.split(' ')
                        if(str[1]=="Director"):
                            ans.append(str[3])
                            print(str[3])
                    n+=1
          except:
                     pass
          print("ans:")
          leng=len(ans)
          if(leng>1):
                    speak.Speak("%d Files found"%(leng))
                    for i in ans:
                     speak.Speak(i)
          elif(leng==1):
                    os.chdir("c:")
                    ss=ans[0][:len(ans[0])-1]+"/"+filename
                    os.system(ss)
          else:
                    speak.Speak("no files found")
findfile("sphinx.txt")
