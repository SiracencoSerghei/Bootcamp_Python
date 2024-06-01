#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# passwd = ""
# for nr in range(nr_letters):
# 	passwd += letters[random.randint(0, len(letters))]
# for nr in range(nr_symbols):
# 	passwd += random.choice(symbols)
# for nr in range(nr_numbers):
# 	passwd += random.choice(numbers)
# print(passwd)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
passwd_list = []
for nr in range(nr_letters):
	passwd_list += letters[random.randint(0, len(letters))]
for nr in range(nr_symbols):
	passwd_list.append(random.choice(symbols))
for nr in range(nr_numbers):
	passwd_list += random.choice(numbers)
print(passwd_list)
random.shuffle(passwd_list)
print(passwd_list)
passwd = ""
for char in passwd_list:
	passwd += char
	
print(f"Your password is {passwd}")
