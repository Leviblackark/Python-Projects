import random
from project7art import stages, logo
from project7words import word_list

# Set lives to 6 this will decrease everytime the guess is wrong
lives = 6

# Randomly choose a word from the list
print(logo)
chosen_word = random.choice(word_list)
print(chosen_word)

# Create the placeholder each character in the random word
placeholder = ""
length = len(chosen_word)

for position in range(0, length):
    placeholder += "_"
print("Word to guess: " + placeholder)

# game_over to exit the while loop
game_over = False
store_letters = []

while not game_over:
    # the users guessed letter
    print(f"**************************** {lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if guess in store_letters:
        print(f"You already guessed {guess}")

    display = ""  # What will be displayed after user has giving the guess

    # turn it into a list to run the check
    list_word = list(chosen_word)
    # Check the occurrence
    for position in list_word:
        # for each letter in list that is equal to guess
        if guess == position:
            # places the letter instead of a placeholder
            display += position  # display = display + position
            store_letters.append(guess)
        elif position in store_letters:
            display += position
        else:
            display += "_"
    print("Word to guess: " + display)
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word.\nYou lose a life.")
        if lives == 0:
            game_over = True
            print(f"*********************** IT WAS {chosen_word} YOU LOSE**********************")

    if "_" not in display:
        gamer_over = True
        print("****************************YOU WIN****************************")

    # Each time the lives decreases display the image. if it doesn't change the image stays the same
    print(stages[lives])
