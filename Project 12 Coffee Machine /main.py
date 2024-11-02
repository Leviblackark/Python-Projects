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
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
# Coffee machine

# TODO 1: Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
#  Check the user’s input to decide what to do next

# The prompt should show every time action has completed, e.g. once the drink is
#  dispensed. The prompt should show again to serve the next customer.

# TODO 2: Report displays what's currently in resources and then reprompt (While loop)

# Display resources
# Money that the machines been collecting

# TODO 3: Turn off the Coffee Machine by entering “off” to the prompt. (Exit Loop)

# For maintainers of the coffee machine, they can use “off” as the secret word to turn off
#  the machine. Your code should end execution when this happens.

# TODO 4: Check resources Sufficient? When the user chooses a drink, the program should check if there are enough
#  resources to make that drink

# Compare what's in the resources to ingredients needed, if less, then tell the user "Sorry not enough" and reprompt
#  Access for entered order. “Sorry there is not enough water.” and for each one

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


