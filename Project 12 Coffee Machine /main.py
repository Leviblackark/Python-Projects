# Coffee machine
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    # 300 200 100
    "water": 100,
    "milk": 100,
    "coffee": 100,
}


def check_resources(value, pot):
    """it formats resources and current account of machine """
    # value = Value of the dictionary
    water = "Water: " + str(value["water"]) + "ml"
    milk = "Milk: " + str(value["milk"]) + "ml"
    coffee = "Coffee: " + str(value["coffee"]) + "g"

    # Money
    account = "Money: $" + str(pot)

    print(f"{water}\n{milk}\n{coffee}\n{account}")


def compare_resources(ingredients, machine_hold):
    """Checks if resource is available and if not tells the user what's out"""
    out_of = []

    for key_word in machine_hold:
        # Each key word inside resources loop and checked against the MENU if inside
        if key_word in ingredients:
            # print("Yes")
            if machine_hold[key_word] < ingredients[key_word]:
                out_of.append(key_word)
    # To only print one statement for what's out saved outside the loop
    if len(out_of) > 1:
        convert = " and ".join(out_of)
        print(f"Sorry there is not enough {convert}.")
    else:
        print(f"Sorry there is not enough {out_of[0]}.")


# TODO 1: Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
#  Check the user’s input to decide what to do next

# The prompt should show every time action has completed, e.g. once the drink is
#  dispensed. The prompt should show again to serve the next customer.

money = 0
coffee_machine = True

while coffee_machine:
    # Prompt
    response = input("What would you like? (espresso/latte/cappuccino): ").strip().lower()

    # TODO 2: Report displays what's currently in resources and then reprompt (While loop)
    #  Turn off the Coffee Machine by entering “off” to the prompt

    if response == "report":
        # Display resources
        check_resources(resources, money)

    elif response == "off":
        coffee_machine = False

    # TODO 4: Check resources Sufficient? When the user chooses a drink, the program should check if there are enough
    #  resources to make that drink
    # Compare what's in the resources to ingredients needed, if less, then tell the user "Sorry not enough" and reprompt
    #  Access for entered order. “Sorry there is not enough water.” and for each one

    elif  response == "latte":
        # MENU["latte"]["ingredients"]
        compare_resources(ingredients=MENU["latte"]["ingredients"], machine_hold=resources)
    elif response == "espresso":
        compare_resources(ingredients=MENU["espresso"]["ingredients"], machine_hold=resources)
    elif response == "cappuccino":
        compare_resources(ingredients=MENU["cappuccino"]["ingredients"], machine_hold=resources)

    # TODO 5: Process Coins. If there are sufficient resources to make the drink selected, then the program should
    #  prompt the user to insert coins.

    # Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01

    # Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
    #  pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52

# TODO 6: Check Transaction Successful?
#  Check that the user has inserted enough money to purchase the drink they selected.

# “Sorry that's not enough money. Money refunded.”  if not enough and then reprompt

# if the user has inserted enough money, then the cost of the drink gets added to the
#  machine as the profit and this will be reflected the next time “report” is triggered

# If the user has inserted too much money, the machine should offer change.
# "Here is $2.45 dollars in change.” The change should be rounded to 2 decimal places.

# TODO 7: If successful deducted from resources

# Here's your(name of drink) enjoy!
# prompt
