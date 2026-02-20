import speech_recognition as sr
import pyttsx3
import datetime
import time
import sys
import webbrowser
import os

engine = pyttsx3.init()
engine.setProperty("rate", 145)

listener = sr.Recognizer()

tasks = []

def speak(text):
    print("Assistant:",text)
    engine.say(text)
    engine.runAndWait()
    time.sleep(0.4)

def listen():
    with sr.Microphone() as source:
        listener.adjust_for_ambient_noise(source, duration=0.5)
        audio = listener.listen(source)
    try:
        text = listener.recognize_google(audio)
        print("User:",text)
        return text.lower()
    except:
        return ""
    
def add_task(task):
    tasks.append(task)
    return "Task added sucessfully"

def list_tasks():
    if not tasks:
        return "You have no tasks"
    return "Your tasks are"

def clear_tasks():
    if not tasks:
        return "You have no tasks"
    return "Your tasks are: "+", ".join(tasks)

def generate_reply(command):

    if "exit" in command or "stop" in command:
        speak("Session terminated. have a productive day")
        exit()

    if "time" in command:
        return f"The current time is {datetime.datetime.now().strftime('%I:%M %p')}"
    
    if "date" in command or "today" in command:
        return f"Today's date is {datetime.datetime.now().strftime('%I:%M %p')}"
    
    if "add task" in command:
        task = command.replace("add task").strip()
        if task:
            return add_task(task)
        return "Please say the task name"
    
    if "list tasks" in command:
        return list_tasks()
    
    if "clear tasks" in command:
        return clear_tasks()
    
    if "search" in command:
        query = command.replace("search", "").strip()
        if query:
            webbrowser.open(f"https://www.google.com/search?q={query}")
            return f"Searching for {query}"
        return "Please say what you want to search"
    
    if "open youtube" in command:
        webbrowser.open("httpps://youtube.com")
        return "Opening Youtube"
    
    if "open google" in command:
        webbrowser.open("httpps://google.com")
        return "Opening google"
    

    return "Commands not recognized. Please try again"

def main():
    speak("Smart assistant is ready Awaiting you command")

    while True:
        command = listen()
        if command:
            reply = generate_reply(command)
            speak(reply)

if __name__ == "__main__":
    main()


    


        
        
    

    
    
    
