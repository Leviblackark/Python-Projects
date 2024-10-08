alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(original_text, shift_amount):
    code = ""

    for instance in original_text:
        # find the index of instance within alphabet
        location_number = alphabet.index(instance)
        # current index of current letter + the amount you want to shift
        position = location_number + shift_amount
        # Keeps within the range
        position %= len(alphabet)
        # call the new location of that letter and save within code
        code += alphabet[position]
    print(f"Here is the encoded result: {code}")


def decrypt(original_text, shift_amount):
    decode = ""
    for instance in original_text:
        # combined the index and the amount to shift
        shifted_index = alphabet.index(instance) - shift_amount
        shifted_index %= len(alphabet)
        decode += alphabet[shifted_index]

    print(f"Here is the decoded result: {decode}")


encrypt(original_text=text, shift_amount=shift)
decrypt(original_text=text, shift_amount=shift)