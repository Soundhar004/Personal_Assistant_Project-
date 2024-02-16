import pyttsx3
import speech_recognition as sr
import webbrowser as wb
import os
import AppOpener as ap
import time
import datetime as dt 
#from pocketsphinx import LiveSpeech as sr

main="hi hello"
start=pyttsx3.init("sapi5")
two_voices=start.getProperty("voices")
start.setProperty('voice',two_voices[1].id)

#start.say("i can convert the text into the speech")
#start.runAndWait()

def speak(z):
    start.say(z)
    start.runAndWait()

a=" Hi soundher...how are you"
speak(a)    




def user_speech():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Hi ! How can I help you")
        speak("Hi ! How can I help you")
        print("Listening....")
        r.pause_threshold=1.5
        r.adjust_for_ambient_noise(source,duration=1)
        
        audio=r.listen(source)
        try:
            print("Just wait a minute...")
            r_audio=r.recognize_google(audio,language="en-US")
            global user_q
            user_q = r_audio.lower()
            print(r_audio)
            speak(r_audio)
        except Exception:
            print("Please try again..")

user_speech() 

if "open google" in user_q:
    wb.open("Google.com")
    

elif "open microsoft edge" in user_q:
    path="C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
    os.startfile(path)

elif "open whatsapp web"  in user_q:
    wb.open("https://www.bing.com/ck/a?!&&p=b2d533c307597a6dJmltdHM9MTY5MzM1MzYwMCZpZ3VpZD0yMzMwZjRjZC01MzcxLTY0ZDctMjBiZS1lN2FmNTJkNzY1MTYmaW5zaWQ9NTIxMg&ptn=3&hsh=3&fclid=2330f4cd-5371-64d7-20be-e7af52d76516&psq=whatsapp&u=a1aHR0cHM6Ly93ZWIud2hhdHNhcHAuY29tLw&ntb=1")

elif main in user_q and "open brave" in user_q:
    path="C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
    os.startfile(path) 

elif "open file explorer" in user_q:
    os.system("file ")

elif "open notepad" in user_q:
    os.system("notepad")

elif "open spotify" in user_q:
    ap.open("spotify")

elif "time" in user_q:
    time=dt.datetime.now().strftime("%H:%M:%S")
    print(time)
    speak(time)
else:
    print("just wait for upgrade...")
    speak("just wait for upgrade...")    
    






