from project9art import logo

print(logo)
bids_made = {}


def store_bid():
    name = input("What is your name?: ")
    bid = input("What is your bid?: £")
    bids_made[name] = int(bid)


correct_type = True
# continue_bidding = True
while correct_type:
    store_bid()
    all_bids = input("Are there any other bidders? Type 'yes' or 'no'\n").lower()

    if all_bids == "yes" or all_bids == "no":
        # correct_type = False

        if all_bids == 'yes':
            print("\n" * 100)

        else:
            correct_type = False
            # continue_bidding = False
            for highest_bidder in bids_made:
                winner = ""
                largest_bid = 0
                bid_amount = bids_made[highest_bidder]
                if bid_amount > largest_bid:
                    largest_bid = bid_amount
                    winner = highest_bidder
                print(f"The winner is {winner} with a bid of £{bid_amount}")

    else:
        print("Sorry you type a incorrect answer")
