#  String

print("Hello"[4])

print("123" + "456")

# Integer

print(123 + 456)

print(123_456_7890)

# Float

print(3.14159)

# Boolean
print(True)
print(False)


# ==========================


# len(123)  # TypeError: object of type 'int' has no len()
print(type(123))

# num_char = len(input("What is your name? "))
# # print("Your name has " + num_char + " characters.")  # TypeError: can only concatenate str (not "int") to str
# print(type(num_char))
# print("Your name has " + str(num_char) + " characters.")

print(70 + float("370.25"))
print(str(70)+str(100))
# ====================================

"""Write a program that adds the digits in a 2 digit number. 
e.g. if the input was 35, 
then the output should be 3 + 5 = 8"""
#
# two_digit_number = input("Input two digit number: ")
# # 🚨 Don't change the code above 👆
# ####################################
# # Write your code below this line 👇
#
# # output = int(str(two_digit_number)[0]) + int(str(two_digit_number)[1])
#
# # output = sum([int(digit) for digit in str(two_digit_number)])
# # output = (int(two_digit_number) // 10) + (int(two_digit_number) % 10)
# output = sum(map(int, str(two_digit_number)))
# print(output)

# =======================================

# Numbers === PEMDASlr () ** * / + - left to right

# ===========================================

# # 1st input: enter height in meters e.g: 1.65
# height = input("height: ")
# # 2nd input: enter weight in kilograms e.g: 72
# weight = input("weight: ")
# # 🚨 Don't change the code above 👆
#
# # Write your code below this line 👇
# # bmi = int(float(weight) / float(height) ** 2)
# bmi = float(weight) // float(height) ** 2
# print(bmi)
# ==================================================

"""I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.

Create a program using maths and f-Strings that tells us how many weeks we have left, if we live until 90 years old.

It will take your current age as the input and output a message with our time left in this format:

You have x weeks left.

Where x is replaced with the actual calculated number of weeks the input age has left until age 90.

Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.
Example Input

56

Example Output

You have 1768 weeks left.
"""
# age = input()
# # 🚨 Don't change the code above 👆
# # Write your code below this line 👇
#
# years = 90 - int(age)
# weeks = years * 52
# print(f"You have {weeks} weeks left.")

# ===========================================

#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
"""Example Input

Welcome to the tip calculator!
What was the total bill? $124.56
How much tip would you like to give? 10, 12, or 15? 12
How many people to split the bill? 7"""

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
bill_with_tip = tip / 100 * bill + bill  #  bill * (1 + tip/100)
print(bill_with_tip)
bill_by_person = round(bill_with_tip / people, 2)
print(f"Each person should pay: ${bill_by_person:.2f}")

