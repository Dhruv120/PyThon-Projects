import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

print("Initializing David")

master  = "Dhruv Dholariya"
engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice' , voices[0].id)
def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    print(hour)

    if hour>= 0 and hour <12 :
        speak("good mornig" + master)

    elif hour >=12  and hour< 18 :
        speak("good afternoon" + master)

    else :
        speak("good evening " + master)       
 
    speak("Hello.." )
    speak ("I am david , your virtual assistant")
    speak("I am created by Mr Dhruv Dholariya ")
    speak("I came to know that Mr Dhruv Dholariya is your friend . He is my father")
    speak ("how can i help you ?")


# def tc():
#     r= sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Speak Now")
#         audio = r.listen(source)

#     try:
#         print("Recognizing...")
#         query = r.recognize_google(audio , language= 'en-in')
#         print(f"User Said : {query} \n") 

#     except Exception as e:
#         print("Please repeat")       



speak("Initializing David......")    
wishme()
# tc()