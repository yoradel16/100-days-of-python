import random
from Assets import project_logos

EASY_LEVEL = 10
HARD_LEVEL = 5

def higher_or_lower(num, guess_num):
    if guess_num > num:
        return "Too high"
    elif guess_num < num:
        return  "Too low"
    elif guess_num == num:
        return "You guessed the number!"


def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard: ").lower().strip()
    if difficulty == "easy":
        return EASY_LEVEL
    elif difficulty == "hard":
        return HARD_LEVEL
    else:
        print("Invalid input. Choose from easy and hard.")


"""Game Proper"""
print(project_logos.number_guesser)
print("Welcome to the number guessing game.\nI'm thinking of a number between 1 and 10.")
number = random.randint(1,100)
attempts = set_difficulty()

while attempts != 0:
    guess = int(input("Make a guess: "))
    if (higher_or_lower(number,guess)) == "You guessed the number!":
        print("You guessed it right!")
        break
    else:
        attempts = attempts - 1
        print(higher_or_lower(number, guess))
        print(f"You have {attempts} left. Try again.")

if attempts == 0:
    print(f"You have used all your attempts.\nThe number you're trying to guess is {number}")