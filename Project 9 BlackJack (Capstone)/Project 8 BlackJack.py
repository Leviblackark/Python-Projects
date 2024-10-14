# Black Jack Game Project
import random
from art import logo

print(logo)

# Simplified version ACE = 11,  10 has a chance of winning four times, the desk stays the same, computer is the dealer

# TODO: Deal both user and computer a starting hand of 2 random card values.
user_count = []
dealer_count = []


def hand():
    """Random card from deck of card"""
    # Infinite deck (unchanging)
    card = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    index = random.randint(0, 12)
    return card[index]


play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

start = True

# If input is neither 'y' nor 'n', ask again
while play_game != "y" and play_game != "n":
    print("Sorry invalid entry")
    play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

if play_game == "y":

    #  Create loop that hands out the first hand
    for first_hand in range(1, 3):
        user_count.append(hand())
        dealer_count.append(hand())

    print(user_count)
    print(dealer_count)

# TODO: Detect when computer or user has a blackjack. (Ace + 10 value card).

# TODO: If computer gets blackjack, then the user loses (even if the user also has a blackjack).
#  If the user gets a blackjack, then they win (unless the computer also has a blackjack).

# TODO: Calculate the user's and computer's scores based on their card values.
# TODO: If an ace is drawn, count it as 11. But if the total goes over 21, count the ace as 1 instead.
# TODO: Reveal computer's first card to the user.
# TODO: Game ends immediately when user score goes over 21 or if the user or computer gets a blackjack.
# TODO: Ask the user if they want to get another card.

# TODO: Once the user is done and no longer wants to draw any more cards, let the computer play.
#  The computer should keep drawing cards unless their score goes over 16.

# TODO: Compare user and computer scores and see if it's a win, loss, or draw.
# TODO: Print out the player's and computer's final hand and their scores at the end of the game.
# TODO: After the game ends, ask the user if they'd like to play again. Clear the console for a fresh start.
