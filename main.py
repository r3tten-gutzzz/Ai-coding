import requests

def get_random_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)

    if response.status_code == 200:

        joke_data = response.json()
        return f"{joke_data['setup']} - {joke_data['punchline']}"
    else:
        return "Failed to retreive joke."

def main():
    print("Welcome to random joke generator!")

    while True:
        userInput = input("Do you want to get a new joke? Y/N: ").strip().lower()
        
        if userInput in ["no", "n"]:
            print("Goodbye")
            break

        joke = get_random_joke()
        print(joke)

if __name__== "__main__":
    main()


