from groq import generate_responses


def prompt_engineering_activity():
    print("Welcome to the Ai prompt Engineering Tutorial !!")

    vague = input("Enter a vague prompt: ")
    print("\nAi's response to vague prompt:")
    print("generate_response(vague)")

    specific = input("\nNow, make it more specific: ")
    print("\n Ai's response to specific prompt:")
    print(generate_responses(specific))

    context = input("\n Now,add context to your specific prompt:")
    print("n\Ai's response to contextual prompt:")
    print(generate_responses(context))

    print("\n--- Reflection ---")
    print("1) How did AI's response change when the prompt was made for specific?")
    print("2) how did the Ai's resonse improve with the added context?")
    print("3) which prompt produced the most relevant and tailored response? why?")


if __name__ == "__main__":
    prompt_engineering_activity()