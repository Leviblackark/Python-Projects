# Black Jack Game Project
import random
from art import logo

# Simplified version ACE = 11,  10 has a chance of winning four times, the desk stays the same, computer is the dealer


def hand():
    """Random card from deck of card"""
    # Infinite deck (unchanging)
    card = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    index = random.randint(0, 12)
    return card[index]


def score(count):
    """Calculate total"""
    return sum(count)


def black_jack(listed):
    """returns a 1 if an ace and 10 is in the list, 0 if not"""
    if 11 in listed and 10 in listed:
        return 1
    else:
        return 0


def adjust_for_ace(count):
    """Adjust the value of ace from 11 to 1 if the total score exceeds 21"""
    # Both over 21 and 11 inside list would have to be true
    while score(count) > 21 and 11 in count:
        # location
        ace_index = count.index(11)
        # Change value
        count[ace_index] = 1
    # Return the changed list and then save it back inside itself
    return count


start = True

while start:
    print(logo)

    # TODO: Deal both user and computer a starting hand of 2 random card values.
    # store the values of what cards are held
    user_count = []
    dealer_count = []
    # start game
    play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

    # If input is neither 'y' nor 'n', ask again
    while play_game != "y" and play_game != "n":
        print("Sorry invalid entry")
        play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

    if play_game == "y":

        #  deal two cards
        for first_hand in range(1, 3):
            # user
            user_count.append(hand())
            # dealer
            dealer_count.append(hand())

        # Tests
        # print(user_count)
        # print(dealer_count)

        # TODO: Calculate the user's and computer's scores based on their card values.
        # add up user score, then convert the users numbers into string so it doesn't show a list
        current_score = score(count=user_count)
        converted_display = ", ".join(map(str, user_count))

        # add up the dealer score, then don't convert but display the first number
        dealers_tally = score(count=dealer_count)
        unconcealed_card = dealer_count[1]

        # TODO: Reveal computer's first card to the user.
        print(f"Your cards: {converted_display}, current score: {current_score}")
        print(f"Dealer's first card: {unconcealed_card}, ✖️")

        # TODO: Detect when computer or user has a blackjack. (Ace + 10 value card)

        # TODO: If computer gets blackjack, then the user loses (even if the user also has a blackjack).
        #  If the user gets a blackjack, then they win (unless the computer also has a blackjack).
        if black_jack(listed=user_count) == 1:
            if black_jack(listed=dealer_count) == 0:
                print(f"BLACKJACK YOU WIN 😁 {current_score}")
            # Check if the Dealer also has a back jack
            else:  # black_jack(listed=dealer_count) == 1:
                print("YOU LOSE 🤕, DEALER BLACKJACK OVERRIDE")
                dealer_reveal = ", ".join(map(str, dealer_count))
                print(f"Dealers cards: {dealer_reveal} Score: {dealers_tally}")
            continue  # Restarts the game loop for a new game

        # TODO: If an ace is drawn, count it as 11. But if the total goes over 21, count the ace as 1 instead.
        # Replace 11 with 1 if score is over 21 and 11 is present. Save back into list
        user_count = adjust_for_ace(user_count)
        # new score
        current_score = score(user_count)

        # If the score is over 21
        if current_score > 21:
            converted_display = ", ".join(map(str, user_count))
            print(f"Bust! Your score: {current_score}, Your cards: {converted_display}")
            dealers_tally = score(count=dealer_count)
            dealers_display = ", ".join(map(str, user_count))
            print(f"Dealers score: {dealers_tally}, dealers reveal {dealers_tally}")

        # TODO: Ask the user if they want to get another card.
        another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower

        # Check for the correct input and reprompt if needed
        # while another_card != "y" and another_card != "n":
        #     print("Sorry invalid entry")
        #     another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower

        while another_card == "y":
            # add a new card to the user, hand() = random number, append into targeted list
            user_count.append(hand())
            user_count = adjust_for_ace(user_count)

            # display update
            current_score = score(user_count)
            converted_display = ", ".join(map(str, user_count))

            print(f"Your cards: {converted_display}, current score: {current_score}")
            print(f"Dealer's first card: {unconcealed_card}, ✖️")

            if current_score > 21:
                print(f"Busted! Your score: {current_score}. You lose.")
                continue  # Restarts the game loop for a new game

            another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower


# TODO: Once the user is done and no longer wants to draw any more cards, let the computer play.
#  The computer should keep drawing cards unless their score goes over 16.

# TODO: Compare user and computer scores and see if it's a win, loss, or draw.
# TODO: Print out the player's and computer's final hand and their scores at the end of the game.
# TODO: After the game ends, ask the user if they'd like to play again. Clear the console for a fresh start.