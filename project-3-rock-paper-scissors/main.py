import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# images Store in a list
game_images = [rock, paper, scissors]
# print(game_images[1])

# Rock wins against Scissors 0 wins 2, Rock against Rock 0 draw 0
# Scissors  wins against Paper 2 to 0, Scissors against Scissors 2 draw 2
# Paper wins against Rock 1 wins 0, Paper against Paper 1 draw 1
user_choice = int(input("What do you choose? Type:"
                        "\n0 for Rock, "
                        "\n1 for Paper,"
                        "\n2 for Scissors.\n"))
if user_choice < 0 or user_choice >= 3:
    print("The number you have typed is invalid, You lose")
else:
    print("Your Choice 🤤")
    # Print the corresponding images to the numbers
    if user_choice == 0:
        print(game_images[0])
    elif user_choice == 1:
        print(game_images[1])
    else:
        print(game_images[2])

    print("Computer's Choice 😎")
    # Create random number and use that for the machines choice
    number_index = random.randint(0, 2)
    print(game_images[number_index])

    # Compair Results to decide a winner

    if user_choice == 0 and number_index == 2:
        print("You Win!")
    # One instance when the user is greater
    elif user_choice == 2 and number_index == 0:
        print("You Lose!")
    # Not all instance where computers choice is greater
    elif number_index > user_choice:
        print("You Lose")
    # Not all instance where the user is greater
    elif user_choice > number_index:
        print("You Win!")
    elif user_choice == number_index:
        print("You Draw!")
    else:
        print("You Lose!")



