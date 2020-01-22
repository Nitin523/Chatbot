import pyttsx3
import datetime
import speech_recognition as sr 
import wikipedia
import webbrowser
import os
import random
import time
import calendar
import datetime

#edited



engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')

# print(voices[1].id)

engine.setProperty('voice', voices[1].id)



def speak(audio):

    engine.say(audio)

    engine.runAndWait()



def wishMe():

    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:

        speak("Good morning nitin")

    elif hour>=12 and hour<4:

        speak("Good afternoon Nitin")

    else:

        speak("Good Evening Nitin")



    speak("I am your Assistant, Happy Soul version 1.0")
    speak(" ")
    
    

def takeCommand():

    # takes my command from microphone and gives text

    r =sr.Recognizer()

    with sr.Microphone() as source:

        print("listening...")

        r.pause_threshold = 1

        audio = r.listen(source)

    try:

        print("recognizing...")

        query = r.recognize_google(audio, language ='en-in')

        print("You said : ", query)

    except Exception as e:

        print(e)

        speak("Sorry Nitin , can you repeat that again?")

        return "None"
        time.sleep(10)                                        #edited

    return query


def findDay(date): 
    born = datetime.datetime.strptime(date, '%d%m%Y').weekday() 
    return (calendar.day_name[born])

a="ELECTRONICS ENGINEERING"
b="DATA STRUCTURE"
c="DISCRETE STRUCTURES & THEORY OF LOGIC"
d="TECHNICAL COMMUNICATION"
e="PDP"
f="PDP"
g="SYSTEM SECURITY"
h="LIBRARY"
i="DATA STRUCTURE"
j="C.O.A"
k="A1 DISCRETE STRUCTURE & LOGIC LAB/ A2 DATA STRUCTURES USING C LAB"
l="A1 DISCRETE STRUCTURE & LOGIC LAB/ A2 DATA STRUCTURES USING C LAB"
m="A1 MINI PROJECT/ A2 C.O.A LAB"
n="A1 MINI PROJECT/ A2 C.O.A LAB"
o="SYSTEM SECURITY"
p="LIBRARY"
q="DISCRETE STRUCTURES & THEORY OF LOGIC"
r="DATA STRUCTURE"
s="C.O.A"
t="C.O.A"
u="PDP"
v="ELECTRONICS ENGINEERING"
w="A1 C.O.A LAB/ A2 MINI PROJECT"
x="A1 C.O.A LAB/ A2 MINI PROJECT"
A="TECHNICAL COMMUNICATION"
B="ELECTRONICS ENGINEERING"
C="A1 DATA STRUCTURE/ A2 C.O.A"
D="A1 C.O.A/ A2 DATA STRUCTURE"
E="A1 DATA STRUCTURES USING C LAB/ A2 DISCRETE STRUCTURE & LOGIC LAB"
F="A1 DATA STRUCTURES USING C LAB/ A2 DISCRETE STRUCTURE & LOGIC LAB"
G="C.O.A"
H="LIBRARY"
I="DISCRETE STRUCTURES & THEORY OF LOGIC"
J="DATA STRUCTURE"
K="ELECTRONICS ENGINEERING"
L="DISCRETE STRUCTURES & THEORY OF LOGIC"
M="ELECTRONICS ENGINEERING"
N="TECHNICAL COMMUNICATION"
O="SYSTEM SECURITY"
P="LIBRARY"


if __name__ == "__main__":

    wishMe()

    while True:

        speak("How can i help you Nitin ?")

        query = takeCommand().lower()

        if 'wikipedia' in query:                                        #wikipedia working

                speak("searching in wikipedia")

                query = query.replace("wikipedia", "")

                results = wikipedia.summary(query, sentences = 2)

                speak("According to wikipedia")

                print(results)

                speak(results)


       
        elif 'open youtube' in query:

            webbrowser.open("youtube.com")

            speak("youtube is opened")

        elif 'open google' in query:

            webbrowser.open("google.com")

            speak("google is opened")

        elif 'open gmail' in query:                      #edited

            webbrowser.open("gmail.com")

            speak("gmail is opened")

        elif 'play video' in query:                           #predited

            music_dir ='D:\\Movie'

            songs = os.listdir(music_dir)

            print(songs)
            
            os.startfile(os.path.join(music_dir,songs[16]))

            speak("Video is being played buddy")

        elif 'play music' in query:                              #Edited random music

            music_dire ='D:\\New songs'

            songse = os.listdir(music_dire)

            print(songse)

            t=random.randint(1,101)
            
            os.startfile(os.path.join(music_dire,songse[t]))

            speak("Music is being played buddy")

        elif ' what is the time' in query:                      

            strTime = datetime.datetime.now().strftime("%H:%M:%S")

            speak(f"the time is {strTime}")

        elif 'open code' in query:                             #source code comand edited

            codepath = "D:\\chatbot.txt"

            os.startfile(codepath)

        elif 'open calendar' in query:
                    speak("what are you looking for...")
                    speak("you have two choices...")
                    speak("1 find day on the given date.")
                    speak("2 Display calender for a month in any year")
                    speak("Enter your choice")
                    ch=int(input())
                    if (ch==2):
                        yy =int(input("Enter year:"))
                        mm = int(input("Enter month:"))
                    # display the calendar
                        print(calendar.month(yy,mm))      
                    # Driver program
                    else:
                        date =input("Enter the date in ddmmyyyy format:")
                        print(findDay(date))
        elif 'time table' in query:
                    while(1):
                        print("\n1.MONDAY")
                        print("\n2.TUESDAY")
                        print("\n3.WEDNESDAY")
                        print("\n4.THURSDAY")
                        print("\n5.FRIDAY")
                        print("\n6.EXIT")
                        speak("ENTER YOUR CHOICE")
                        ch=int(input())
                        if ch==1:
                            print("LEC.\t""SUB.")
                            #print("SUB.")
                            print("1\t",a)
                            #print(a)
                            print("2\t",b)
                            #print(b)
                            print("3\t",c)
                            #print(c)
                            print("4\t",d)
                            #print(d)
                            print("5\t",e)
                            #print(e)
                            print("6\t",f)
                            #print(f)
                            print("7\t",g)
                            #print(g)
                            print("8\t",h)
                            #print(h)
                            break
                        elif ch==2:
                            print("LEC.\t""SUB.")
                            #print("SUB.\n")
                            print("1\t",i)
                            #print(i)
                            print("2\t",j)
                            #print(j)
                            print("3\t",k)
                            #print(k)
                            print("4\t",l)
                            #print(l)
                            print("5\t",m)
                            #print(m)
                            print("6\t",n)
                            #print(n)
                            print("7\t",o)
                            #print(o)
                            print("8\t",p)
                            #print(p)
                            break
                        elif ch==3:
                            print("LEC.\t""SUB.")
                            #print("SUB.")
                            print("1\t",q)
                            #print(q)
                            print("2\t",r)
                            #print(r)
                            print("3\t",s)
                            #print(s)
                            print("4\t",t)
                            #print(t)
                            print("5\t",u)
                            #print(u)
                            print("6\t",v)
                            #print(v)
                            print("7\t",w)
                            #print(w)
                            print("8\t",x)
                            #print(x)
                            break
                        elif ch==4:
                            print("LEC.\t""SUB.")
                            #print("SUB.\n")
                            print("1\t",A)
                            #print(A)
                            print("2\t",B)
                            #print(B)
                            print("3\t",C)
                            #print(C)
                            print("4\t",D)
                            #print(D)
                            print("5\t",E)
                            #print(E)
                            print("6\t",F)
                            #print(F)
                            print("7\t",G)
                            #print(G)
                            print("8\t",H)
                            #print(H)
                            break

        elif 'stop' in query:                                        #stop function

            speak("see you soon Nitin please visit again to me ")

            exit()

        else :
        
            webbrowser.open(query)
            time.sleep(10)                                              #edited
            
