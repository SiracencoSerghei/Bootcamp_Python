"""Instructions
Issue

We've got some buggy code. Try running the code. The code will crash and give you an IndexError. This is because we're looking through the list of fruits for an index that is out of range.
Bad Output

Objective

Use what you've learnt about exception handling to prevent the program from crashing. If the user enters something that is out of range just print a default output of "Fruit pie".
Example Input

["Apple", "Pear", "Orange"]

Example Output

 Fruit pie

IMPORTANT: The exception handling should NOT allow each fruit to be printed when there is an exeption. e.g. it should not print out Apple pie, Pear pie and Orange pie, when there is an exerception it should only print "Fruit pie".
Hint

    You'll need to catch the IndexError exception.

    You'll need the try, except and else keywords.
"""
import json

fruits_input = input()
fruits = json.loads(fruits_input)
# 🚨 Do not change the code above

# TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
	try:
		fruit = fruits[index]
		print(fruit + " pie")
	except IndexError:
		print("Fruit pie")
	else:
		print(fruit + " pie")
	finally:
		print("Ciao")

# 🚨 Do not change the code below
make_pie(4)
