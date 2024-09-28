alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesar(original_text, shift_amount, encode_decode):
    code = ""
    # 3 + ( 5 * -1) is the same as 3 - 5
    if encode_decode == "decode":
        shift_amount *= -1

    for instance in original_text:
        # find the index of instance within alphabet
        location_number = alphabet.index(instance)
        # current index of current letter + the amount you want to shift
        position = location_number + shift_amount
        # Keeps within the range
        position %= len(alphabet)
        # call the new location of that letter and save within code
        code += alphabet[position]

    print(f"Here is the {encode_decode}d result: {code}")


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

caesar(original_text=text, shift_amount=shift, encode_decode=direction)
