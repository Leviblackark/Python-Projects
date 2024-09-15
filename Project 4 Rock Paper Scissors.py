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

user_choice = int(input("What do you choose? Type:"
                        "\n0 for Rock, "
                        "\n1 for Paper,"
                        "\n2 for Scissors.\n"))
if user_choice < 0 or user_choice >= 3:
    print("The number you have typed is invalid, You lose")
else:
    print("Works")
