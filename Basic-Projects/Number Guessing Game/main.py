import random
import time

print("===============================================")
print("      Welcome to the Number Guessing Game!      ")
print("===============================================")
time.sleep(1)
print("I'm thinking of a number between 1 and 100.")
time.sleep(1)
number_to_guess = random.randint(1, 100)
difficulty = input("\nChoose a difficulty. Type 'easy' or 'hard': ").lower()
if difficulty == 'easy':
    attempts = 10
else:
    attempts = 5

for attempt in range(attempts):
    chances = attempts - attempt
    print(f"\nYou have {chances} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    time.sleep(0.5)
    if guess < number_to_guess:
        print("🔻 Too low. Try a higher number!")
    elif guess > number_to_guess:
        print("🔺 Too high. Try a lower number!")
    else:
        print(f"\n🎉 You got it! The answer was {number_to_guess}. Congratulations!")
        break

    if chances - 1 == 0:
        print("\n😢 You've run out of guesses, you lose.")
        print(f"The correct number was {number_to_guess}.")
        time.sleep(1)
        print("Better luck next time!")


