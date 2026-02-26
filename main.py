import speech_recognition as sr
import pyttsx3
from deep_translator import GoogleTranslator
from colorama import Fore, init
import time

init(autoreset=True)

engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

recognizer = sr.Recognizer()
microphone = sr.Microphone()

languages = {
    "hindi":"hi",
    "french":"fr",
    "spanish":"es",

}

def speak(text):
    engine.say(text)
    engine.runAndWait()
    time.sleep(0.4)

def listen():
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.6)
        audio = recognizer.listen(source)

    try:
        return recognizer.recognize_google(audio).lower()
    except:
        return ""
    
def select_language():
    speak("please say your target language. French,hindi,spanish")
    print(Fore.CYAN + "\nListening for language selection...")

    spoken_lang = listen()
    print(Fore.YELLOW + f"Detected: {spoken_lang}")

    return languages.get(spoken_lang)

def main():
    print(Fore.GREEN + "\nVoice Translation Assistant Activiated\n")
    speak("Voice Translation Activited")

    while True:
        target_language = select_language()


        if not target_language:
            speak("Invalid Language detected. please try again")
            continue 

        translator = GoogleTranslator(source="en", target=target_language)
        speak("Language selected You may now speak your sentence")

        while 




    

 