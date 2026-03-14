from groq import generate_responses

def reinforcement_learning_activity():
    print("\n==== REINFORCEMENT LEARNING ACTIVITY===\n")
    prompt = input("Enter a prompt for the AI model: ").strip()
    if not prompt:
        print("Please enter a prompt to run the activity")
        return
    
    initial_response = generate_responses(prompt, temperature=0.3, max_tokens=1024)
    print(f"\nInitial AI Response: {initial_response}")

    try: 
        rating = int(input("Rate the response from 1 to 5: ").strip())
        if rating < 1 or rating >5:
            print("Invalid rating. Using 3")
            rating = 3
    except ValueError:
         print("Invalid rating. Using 3")
         rating = 3

    feedback = input("Provide feedback for improvement: ").strip()
    improved_response = f"{initial_response} (Imporved with your feedback: {feedback})"
    print(f"\nImproved AI response: {improved_response}")

def role_based_prompt_activity():
    print("\n=== ROLE-BASED PROMPTS ACTIVITY ===\n")
    category = input("Enter a category: ").strip()
    item = input(f"Enter a specific {category} topic: ").strip()

    if not category or not item:
        print("Please fill in both fields to run the activity")
        return
    
    teacher_prompt = f"you are a teacher. Explain {item} in simple terms"
    expert_prompt = f"you are an expert in {category}. Explain {item} in a detailed, technical answer"

    teacher_response = generate_responses(teacher_prompt, temperature=0.3, max_tokens=1024)
    expert_response = generate_responses(expert_prompt, temperature=0.3,max_tokens=1024)

    print(f"\n----- Teachers Perspective ----\n{teacher_response}")
    print(f"\n----- Expert's perspective -----\n{expert_response}")

reinforcement_learning_activity()
role_based_prompt_activity()


        