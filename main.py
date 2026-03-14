from groq import generate_response

def run_activity():
    print("ZERO-SHOT, ONE-SHOT & FEW-SHOT LEARNING ACTIVITY")

    category = input("Enter a category (e.g,animal, food, city)").strip()
    item = input(f"Enter a specific {category} to classify: ").strip()

    if not category or not item:
        print("Please fill in both fields to run this activity")
        return 
    
    zero_shot = f"Is {item} a {category}? Answer yes or no"
    print("\n ----ZERO-SHOT LEARNING -----")
    print(f"Response: {generate_response(zero_shot, temperature=0.3, max_tokens= 1024)}")

    one_shot = f"""Example:
Category: fruit
item: apple
Answer: yes,apple is a fruit.

now you try:
Category: fruit
item: apple
Answer:"""
    print("\n ----ONE-SHOT LEARNING -----")
    print(f"Response: {generate_response(one_shot, temperature=0.3, max_tokens=1024)}")

    few_shot = f"""Example 1:
Category: fruit
item: apple 
answer: Yes,apple is a fruit

Now you try:
Category: {category}
item: {item}
Answer:"""
run_activity()





    





    


