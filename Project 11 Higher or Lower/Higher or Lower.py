# Higher or Lower (who has more follower)
# TODO:  Display the logo and the separator ‘VS’
import art
import random
from game_data import data


def get_choice():
    """Accepts only 'a' or 'b'"""
    prompt = True
    while prompt:
        try:
            choice = input("Who has more followers? Type 'A' or 'B': ").strip().lower()

            # Check if the input is valid
            if choice not in ('a', 'b'):
                raise ValueError("Invalid input. Please type 'a' or 'b'")
            else:
                prompt = False
                return choice

        # Save ValueError in to x and print all the loop to continue
        except ValueError as x:
            print(x)


print(art.logo)


# TODO: Generate  two random numbers for the items in the list
score = 0
game = True
while game:
    index = []
    while len(index) < 2:
        list_index = random.randint(0, 49)  # 50 items 0-49
        # if the random number is not the same then add the list
        if list_index not in index:
            index.append(list_index)

    # TODO: Access the dictionary at the two numbers in the list
    #  Display there date

    # Accessing the dictionary
    option_1 = data[index[0]]
    option_2 = data[index[1]]

    # Display date
    # TODO: The score appears at the top, the second selections and then it gets restarted with this at the top
    if score > 0:
        print(f"You're Right! Current score: {score}")
    print(f"Compare A: {option_1["name"]}, {option_1["description"]}, {option_1["country"]}")
    print(art.vs)
    print(f"Compare B: {option_2["name"]}, {option_2["description"]}, {option_2["country"]}")

    # TODO: create a prompt to ask who has more follow
    #  try-except block with a while loop, if state to exit

    answer = get_choice()

    # TODO: check the data in dictionary and see which ones higher
    #  compare see which one is higher and then check if it equal to perhaps to get the right winner.

    # access dictionary (option_1 = A Option_1 = B)
    if answer == "a":
        # access follower_count
        if option_1["follower_count"] > option_2["follower_count"]:
            # print("YOU WIN ")
            # increase score
            score += 1
        else:
            # The end the program or ask to rest and show score
            print(f"Sorry, that was wrong. Final score: {score} ")
            game = False

    else:
        # answer "b" run test
        if option_2["follower_count"] > option_1["follower_count"]:
            # print("TEST WIN")
            # increase score
            score += 1
        else:
            # The end the program or ask to rest and show score
            print(f"Sorry, that was wrong. Final score: {score} ")
            game = False
