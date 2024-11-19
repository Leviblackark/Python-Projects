import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
           'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B',
           'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

# Identify how the amount letters, numbers, symbols are going to be used
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Select random selection from the list

letter_choice = []
symbols_choice = []
numbers_choice = []

for mixed_letter in letters:
    letter_choice += random.choice(letters)
# Randomly selection amount from a mixed list
amount_of_letters = random.sample(letter_choice, nr_letters)
# print(amount_of_letters)


# Mix all the symbols
for mixed_symbol in symbols:
    symbols_choice += random.choice(symbols)
# Randomly select the symbols you need
amount_of_symbols = random.sample(symbols_choice, nr_symbols)
# print(amount_of_symbols)

# mix the numbers
for mixed_number in numbers:
    numbers_choice += random.choice(numbers)
amount_of_numbers = random.sample(numbers_choice, nr_numbers)
# print(amount_of_numbers)

# Join the list
password = amount_of_letters + amount_of_symbols + amount_of_numbers
# print(password)

# Shuffle the list
random.shuffle(password)
# print(password)

# Turn the list into a string
password_string = ' '.join(password)
# print(password_string)

print(f"Your generated password is: {password_string}")
