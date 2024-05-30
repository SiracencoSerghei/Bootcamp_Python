#
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
#
# if height >= 120:
#     print("You can ride the rollercoster!")
#     age = int(input("Whet is your age? "))
#     if age < 12:
#         print("Please pay $5.")
#     elif age <= 18:
#         print("Please pay $7.")
#     else:
#         print("please pay $12.")
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
height = float(input("Enter your height in meters e.g., 1.55 "))
# Enter your weight in kilograms e.g., 72
weight = int(input("Enter your weight in kilograms e.g., 72 "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
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
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not leap year")
    else:
        print("Leap year")
else:
    print("Not leap year")
