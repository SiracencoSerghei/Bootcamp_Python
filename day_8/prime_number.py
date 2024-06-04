"""
Instructions

Prime numbers are numbers that can only be cleanly divided by themselves and 1.

https://en.wikipedia.org/wiki/Prime_number

You need to write a function that checks whether if the number passed into it is a prime number or not.

e.g. 2 is a prime number because it's only divisible by 1 and 2.

But 4 is not a prime number because you can divide it by 1, 2 or 4.

Here are the numbers up to 100, prime numbers are highlighted in yellow:

Example Input 1

73

Example Output 1

It's a prime number.

Example Input 2

75

Example Output 2

It's not a prime number.

"""

# Write your code below this line 👇

def prime_checker(number):
  is_prime = True
  prime_msg = "It's a prime number."
  not_prime_msg = "It's Not a prime number."
  range_num = range(2, number)
  print(list(range_num))
  for i in range_num:
	  if number % i == 0:
		  is_prime = False
  print(f"{prime_msg if is_prime else not_prime_msg}")

# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input())  # Check this number
prime_checker(number=n)
