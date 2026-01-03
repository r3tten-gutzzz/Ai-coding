from transformers import pipeline
from colorama import Fore, Style, init 

init(autoreset=True)

classifier = pipeline(

task="sentiment-analysis",

model="distilbert-base-uncased-finetuned-sst-2-english"

)
total_count = 0
positive_count = 0
negative_count = 0

print(Fore.CYAN + Style.BRIGHT + "\nAI SENTIMENT ANALYSIS SYSTEM")
print(Fore.CYAN + "-" * 35)
print(Fore.YELLOW + "Enter any sentence to analyze sentiment")
print(Fore.YELLOW + "Type 'Exit' to terminate the system\n")

while True:
    user_input = input(Fore.WHITE + "Input Text: ").strip()

    if user_input.lower() =="exit":
        print(Fore.CYAN + "\nSession Summary")
        print(Fore.CYAN + "-" * 35)
        print(Fore.GREEN + f"Total Inputs  : {total_count}")
        print(Fore.GREEN + f"Positive      : {positive_count}")
        print(Fore.RED + f"Negative       : {negative_count}")
        print(Fore.CYAN + "\nSystem closed succesfully.\n")
        break

    if not user_input:
        print(Fore.RED + "Input cannot be empty\n")
        continue

    result = classifier(user_input)[0]
    label = result["label"]
    confidence = round(result["score"] * 100, 2)

    total_count += 1

    if confidence >= 85:
        strength = "strong"
    elif confidence >= 65:
        strength = "Moderate"
    else: 
        strength = "weak"
    
    if label == "POSITIVE":
        positive_count += 1 
        color = Fore.GREEN
    else:
        negative_count += 1
        color = Fore.RED
    
    print(Fore.CYAN + "\nAnalaysis result")
    print(Fore.CYAN + "-" * 35)
    print(Fore.GREEN + f"Sentement : {label}")
    print(Fore.GREEN + f"Confidence     : {confidence}")
    print(Fore.RED + f"Strength level     : {strength}")






