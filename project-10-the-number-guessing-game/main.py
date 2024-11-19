import random
# TODO: Welcome them to the game, input that you are thinking of a number between 1 to 100
from art import logo
print(logo)

print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100")

# TODO: Generated a random number and display it while you making the game


def random_number():
    """Returns a random number"""
    generated_number = random.randint(1, 101)
    return generated_number


number = random_number()
# Display number to text code
# print(f"The correct answer is: {number}")

# TODO: Start the game by asking “easy” or “hard”
#  Easy = 10 and hard = 5 let the user know  how many guesses.  Ask to make a guess
game_difficulty = 0

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

# Tests the entry is correct and prompts if wrong
while difficulty != "easy" and difficulty != "hard":
    print("Sorry incorrect entry")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

# Sets how many changes you have left in the game based on choice of difficulty
if difficulty == "easy":
    game_difficulty = 10
else:
    game_difficulty = 5

print(f"You have {game_difficulty} attempts remaining to guess the number.")

# TODO: When the guess is made, compare to the random number, if below, print too low if above print too high
#  Too high \n guess again. and display what attempts are left

while game_difficulty > 0:
    users_guess = int(input("Make a guess: "))

    #  Check if the guess is too low or to high or guessed correctly
    if users_guess == number:
        print(f"You got it! the answer was {number}")
        break
    elif number > users_guess:
        print("TOO LOW\nGuess Again! ")
    else:
        print("TOO HIGH\nGuess Again!")

    # If the program didn't break then reduce amount of attempts
    game_difficulty -= 1

    print(f"You have {game_difficulty} attempts remaining to guess the number.")
    if game_difficulty == 0:
        print("You've ran out of guesses, you lose! 🫡")
