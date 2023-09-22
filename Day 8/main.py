from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
      shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            if new_position >= len(alphabet):    # Cycles to start of list
                new_position -= len(alphabet)
            elif new_position < 0:    # Cycles through to end of list
                new_position += len(alphabet)
            end_text += alphabet[new_position]
        else:
            # Keep numbers and symbols as is
            end_text += char
    print(f"Here's the {cipher_direction}d result: {end_text}")

# Import and print the logo from art.py when the program starts.
print(logo)

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift %= 26
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    ask = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if ask == 'no':
        print("Goodbye")
        break