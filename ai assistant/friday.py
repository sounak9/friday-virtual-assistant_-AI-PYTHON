import pyttsx3
import speech_recognition as sr
import datetime
import pyaudio
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

def speak(audio):
    pass
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    
    else:
        speak("Good Evening!")
    
    speak("i am friday sir. please tell me how may i help you")

def takeCommand():
    #it takes microphone input from the user and returns string output

    r = sr.Recognizer()
    r.pause_threshold = 1
    r.energy_threshold=4000
    with sr.Microphone() as source:  
        print("listening....") 
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"user said: {query}\n")
    
    except Exception as e:
        print(e)
        print("say that again please...")
        return "None"
    return query

if __name__ == '__main__':
    wishMe()  
    if 1:
        query = takeCommand().lower()

        # logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('searching wikipedia...')

            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
    
        elif 'open google' in query:
            webbrowser.open('google.com')
        
        elif 'open stack overflow' in query:
            webbrowser.open('stackoverflow.com')
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir the time is {strTime}")
        
        elif 'how are you' in query:
            speak('i am fine sir  how are you')
        
        elif 'what is your name' in query:
            speak('i am friday')
        
        elif 'who are you' in query:
            speak('i am friday and i am a virtual assistant')
        
        elif 'open code' in query:
            speak('opening code...')
            codepath = "C:\\Program Files\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        
    

