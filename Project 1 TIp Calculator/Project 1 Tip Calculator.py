print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? £"))
tip = int(input("What percentage tip would you like to give? 10 12 15? "))
people = int(input("How many people to split the bill? "))

# 150
# 12 tip
# 12 / 100 = 0.12
# 150 * 0.12 + 150 or 150 * 1.12
amount = 0
amount += (bill * (tip / 100) + bill)
bill_split = (amount / people)
bill_split = '{:.2f}'.format(round(bill_split, 2))

print(f"Each person should pay: £{bill_split}")
