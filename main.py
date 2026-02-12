import pyttsx3
from deep_translator import GoogleTranslator
from colorama import Fore, init

init(autoreset=True)

engine = pyttsx3.init()
engine.setProperty('rate', 150)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def display_language_options():
    print(Fore.CYAN + "n\Available Translation Languages")
    print("1. Hindi (hi)")

    print("2. Tamil (ta)")

    print("3. Telugu (te)")

    print("4. Bengali (bn)")

    print("5. Marathi (mr)")

    print("6. Spanish (es)")

    print("7. Malayalam (ml)")

    print("8. Punjabi (pa)")

    print("0. Exit Program")

    return {

    "1": "hi",

    "2": "ta",

    "3": "te",

    "4": "bn",

    "5": "mr",

    "6": "es",

    "7": "ml",

    "8": "pa"

    }

def select_language():
    languages = display_language_options()
    choice = input(Fore.YELLOW + "n\Select target language (1-8): ").strip()

    if choice == "0":
        return None
    
    return languages.get(choice)


def main():
    print(Fore.GREEN + "\nText Based TTS Translation System Initialized\n")

    while True:
        target_language = select_language()

        if target_language is None:
            print(Fore.GREEN + "\nSystem shutdown completed.")
            break

        translator = GoogleTranslator(source='en', target=target_language)

        print(Fore.CYAN + "\nTranslation engine ready. Enter english text below.")
        print(Fore.YELLOW + "type 'lang' to change language or 'exit' to quit. \n")

        while True:
            text = input(Fore.YELLOW + ">> ").strip()
         
        if text.lower() == "exit":
            print(Fore.GREEN + "\nSystem shutdown completed.")
            return
        
        
        if text.lower() == "lang":
            print(Fore.CYAN + "\nSwitching language selection...")
            return
        
        
