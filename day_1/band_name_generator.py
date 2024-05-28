print("She said: 'Hello' and then left.")
print("Alternatively you can just \"escape\" the quote")

print("Hello " + input("What is your name?").strip()+"!")

num1 = int(input("num1 "))
num2 = int(input("num2 "))

print(f"result = {num1 * num2}")

# input() will get user input in console
# Then print() will print the word "Hello" and the user input
print("Hello " + input("What is your name?"))

inp = input()
print(f"{inp} = {len(inp)} characters")
print(len(input()))

# There are two variables, a and b from input
a = input()
b = input()
# 🚨 Don't change the code above ☝️
####################################
# Write your code below this line 👇
# Create a third variable to help switch the values
# c = a
# a = b
# b = c
a, b = b, a


# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)

# ==================

# 1. Create a greeting for your program.

# 2. Ask the user for the city that they grew up in.

# 3. Ask the user for the name of a pet.

# 4. Combine the name of their city and pet and show them their band name.

# 5. Make sure the input cursor shows on a new line:

# Solution: https://replit.com/@appbrewery/band-name-generator-end

print("Hello to my programm")
city = input("Which city did you grow up in?\n")
pet = input("What is the name of you pet? \n")
band_name = f"{city} {pet}"
print(f"Your band name could be {band_name}")
print("Good bye")