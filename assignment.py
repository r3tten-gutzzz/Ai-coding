import random
number = random.randint(1, 100)

print("Welcome to guess the number!!")
print("Try to guess the number i am thinking about!!")

guess = int(input("Enter your guess: "))

attempts = 0
actual_number = 9

try:
    guess = int(input("Enter your guess: "))
except ValueError:
    print("Invalid input!!")


attempts += 1

if guess == actual_number:
    print("congrats! you have gotten it correct")
    print(f"Total attempts: {attempts}")


if guess < number:
    print("Too low")
elif guess > number:
    print("Too high")
else:
    print("correct")



