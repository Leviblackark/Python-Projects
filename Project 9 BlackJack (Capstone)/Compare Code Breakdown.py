import random
from art import logo


def deal_card():
    """Draws a random cards from list"""
    cards = [11, 2, 3, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    # calculates the total and checking if its equal to 21 and the checking that there two cards in the list
    if sum(cards) == 21 and len(cards) == 2:
        # returns a 0 implying that's the case
        return 0

    if 11 in cards and sum(cards) > 21:
        # removes the occurrence of an item when is occurs
        cards.remove(11)
        #  adds 1 back to list and takes the user back down when the score is return
        # this doesn't seem to change the main list but affects the score instead
        cards.append(1)

    # returns the decks total so it could continue
    return sum(cards)


def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw 🪿"
    elif c_score == 0:
        return "Lose, opponent has Blackjack 🙄 "
    elif u_score == 0:
        return "Win with a Blackjack 😎"
    elif u_score > 21:
        return "You went over. You lose 😮‍💨"
    elif c_score > 21:
        return "Opponent went over. You win 🫡"
    elif u_score > c_score:
        return "You Win 😜"
    else:
        # user_score was lest than computer score
        return "You Lose 🫤"


def play_game():
    print(logo)
    user_cards = []
    computer_card = []
    #  Because Computer_score is inside the first while, we create a test with the second while loop
    #  and it's undefined. fix this but assigning a value that's not 0 because its used in return for another test
    computer_score = -1
    user_score = -1
    is_game_over = False

    for _ in range(2):
        # += is shorthand for the .extend function
        # What ever you put in the brackets it has to be  a list itself
        # Reduce lines of code by calling the function
        user_cards.append(deal_card())
        computer_card.append(deal_card())

    # make the game repeat  itself. Setting up the boolean changes before putting in a while loop
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_card)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first cards: {computer_card[1]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            #  Determining when the game should end while your writing the code , marking the points as you go
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if user_should_deal == "y":
                #  deal another card if yes
                user_cards.append(deal_card())
            else:
                # Ending the game as no more cards are wanted
                is_game_over = True

    # we want to keep drawing cards for the computer
    # Computer_score is only created after the first while loop. to avoid issues assign a value
    while computer_score != 0 and computer_score < 17:
        computer_card.append(deal_card())
        # making sure the computer is updated on the latest score
        computer_score = calculate_score(computer_card)

    print(f"Your final hand: {user_cards}, final core: {user_score}")
    print(f"Computer's final hand: {computer_card}, final score: {computer_score}")
    print(compare(user_score, computer_score))

    while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
        print("\n")
        # calling the function inside the function allows it to behave like a while loop
        play_game()


play_game()
