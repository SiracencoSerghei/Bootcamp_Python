# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# bill = 0
#
# if height >= 120:
#     print("You can ride the rollercoster!")
#     age = int(input("What is your age? "))
#     if age < 12:
#         bill = 5
#         print("Child ticket is $5.")
#     elif age <= 18:
#         print("Youth ticket is $7.")
#         bill = 7
#     else:
#         print("Adult ticket is $12.")
#         bill = 12
#
#     wants_photo = input("Do you want a photo taken? Y/N " ).lower()
#     if wants_photo == "y":
#         bill += 3
#     print(f"Your final bill is ${bill}.")
# else:
#     print("Sorry, you have to grow taller before you can ride.")

# =====================================

# # Write a program that works out
# # whether if a given number is an odd or even number.
# #  Which number do you want to check?
# number = int(input("enter number: "))
# # 🚨 Don't change the code above 👆
#
# # Write your code below this line 👇
# odd_number = bool(number % 2 == 1)
# if odd_number:
#     print('This is an odd number.')
# else:
#     print('This is an even number.')

# =======================================

# Enter your height in meters e.g., 1.55
# height = float(input("Enter your height in meters e.g., 1.55 "))
# # Enter your weight in kilograms e.g., 72
# weight = int(input("Enter your weight in kilograms e.g., 72 "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
#
# bmi = weight / height**2
# if bmi < 18.5 :
#     print(f"Your BMI is {bmi}, you are underweight.")
# elif bmi < 25 :
#     print(f"Your BMI is {bmi}, you have a normal weight.")
# elif bmi < 30 :
#     print(f"Your BMI is {bmi}, you are slightly overweight.")
# elif bmi < 35 :
#     print(f"Your BMI is {bmi}, you are obese.")
# else :
#     print(f"Your BMI is {bmi}, you are clinically obese.")

# =====================================
"""Write a program that works out whether if a given year is a leap year.
A normal year has 365 days, leap years have 366,
with an extra day in February.
The reason why we have leap years is really fascinating,"""
# Which year do you want to check?
# year = int(input("Which year do you want to check? "))
# # 🚨 Don't change the code above 👆
#
# # Write your code below this line 👇
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year")
#         else:
#             print("Not leap year")
#     else:
#         print("Leap year")
# else:
#     print("Not leap year")

# =============================
# """Instructions
#
# Congratulations, you've got a job at Python Pizza! Your first job is to build an automatic pizza order program.
#
# Based on a user's order, work out their final bill.
#
# Small pizza (S): $15
#
# Medium pizza (M): $20
#
# Large pizza (L): $25
#
# Add pepperoni for small pizza (Y or N): +$2
#
# Add pepperoni for medium or large pizza (Y or N): +$3
#
# Add extra cheese for any size pizza (Y or N): +$1
# Example Input
#
# L
# Y
# N
#
# Example Output
#
# Thank you for choosing Python Pizza Deliveries!
# Your final bill is: $28.
#
# """
# print("Thank you for choosing Python Pizza Deliveries!")
# size = input() # What size pizza do you want? S, M, or L
# add_pepperoni = input() # Do you want pepperoni? Y or N
# extra_cheese = input() # Do you want extra cheese? Y or N
# # 🚨 Don't change the code above 👆
# # Write your code below this line 👇

# bill = 0

# if size == "S":
#     bill += 15
#     if add_pepperoni == "Y":
#         bill += 2
# elif size == "M":
#     bill += 20
#     if add_pepperoni == "Y":
#         bill += 3
# elif size == "L":
#     bill += 25
#     if add_pepperoni == "Y":
#         bill += 3
# else:
#     print("We don't have this size...")
#
# if extra_cheese == "Y":
#     bill += 1
#
# print(f"Thank you for choosing Python Pizza Deliveries! Your final bill is: ${bill}.")

# =========================================
#
# """Instructions
# 💪 This is a difficult challenge! 💪
#
# You are going to write a program that tests the compatibility between two people.
#
# To work out the love score between two people:
#
#     Take both people's names and check for the number of times the letters in the word TRUE occurs.
#
#     Then check for the number of times the letters in the word LOVE occurs.
#
#     Then combine these numbers to make a 2 digit number.
#
# For Love Scores less than 10 or greater than 90, the message should be:
#
# "Your score is *x*, you go together like coke and mentos."
#
# For Love Scores between 40 and 50, the message should be:
#
# "Your score is *y*, you are alright together."
#
# Otherwise, the message will just be their score. e.g.:
#
# "Your score is *z*."
#
# e.g.
#
# name1 = "Angela Yu"
# name2 = "Jack Bauer"
#
# T occurs 0 times
#
# R occurs 1 time
#
# U occurs 2 times
#
# E occurs 2 times
#
# Total = 5
#
# L occurs 1 time
#
# O occurs 0 times
#
# V occurs 0 times
#
# E occurs 2 times
#
# Total = 3
#
# Love Score = 53
#
# Print: "Your score is 53."
# These functions will help you:
#
# lower() count()
# Example Input 1
#
# Kanye West
# Kim Kardashian
#
# Example Output 1
#
# The Love Calculator is calculating your score...
# Your score is 42, you are alright together.
#
# Example Input 2
#
# Brad Pitt
# Jennifer Aniston
#
# Example Output 2
#
# The Love Calculator is calculating your score...
# Your score is 73.
#
# Hint
#
# You can check your values against mine using this table:
# Name 1 	Name 2 	Score
# Brad Pitt 	Jennifer Aniston 	73
# Prince William 	Kate Middleton 	67
# Ashton Kutcher 	Mila Kunis 	63
# Angela Yu 	Jack Bauer 	53
# David Beckham 	Victoria Beckham 	45
# Mario 	Princess Peach 	43
# Kanye West 	Kim Kardashian 	42"""

print("The Love Calculator is calculating your score...")
name1 = input()  # What is your name?
name2 = input()  # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

combinate_name = name1 + name2
lower_names = combinate_name.lower()
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")

first_digit = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")

second_digit = l + o + v + e

love_score = int(str(first_digit) + str(second_digit))
if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif 40 < love_score < 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")

# =====================================
