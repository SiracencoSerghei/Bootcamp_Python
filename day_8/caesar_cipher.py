# # =====================================

# # TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

# def encrypt(text, shift):
#     cipher_text = ""
#     for ch in text:
#         position = alphabet.index(ch)
#         new_position = (position + shift) % 26
#         cipher_text += alphabet[new_position]
#     print(cipher_text)
#     return cipher_text

# # TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
# # e.g.
# # plain_text = "hello"
# # shift = 5
# # cipher_text = "mjqqt"
# # print output: "The encoded text is mjqqt"

# ##HINT: How do you get the index of an item in a list:
# # https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

# ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

# # TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.

# # =============================

# # TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.


# def decrypt(text, shift):
#     cipher_text = ""
#     for ch in text:
#         position = alphabet.index(ch)
#         new_position = (position - shift) % 26
#         cipher_text += alphabet[new_position]
#     print(f"decrypt text is {cipher_text}.")
#     return cipher_text


# # TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.
# # e.g.
# # cipher_text = "mjqqt"
# # shift = 5
# # plain_text = "hello"
# # print output: "The decoded text is hello"


# # TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
# # encrypt(plain_text, shift_amountshift)

# if direction == "encode":
#     encrypt(text, shift)
# elif direction == "decode":
#     decrypt(text, shift)
# else:
#     print("You not enter the correct....")

# ========================================
from art import logo
from alphabet import alphabet

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1

    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift_amount) % 26
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"Here's the {cipher_direction} result: {end_text}.")


if __name__ == "__main__":

    should_continue = True
    while should_continue:
            
        print(logo)

        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

        caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
        go_again = input("Do you want to continue? Y/N ").lower()
        if not go_again == 'y':
            should_continue = False
            print("Good Bye!")
