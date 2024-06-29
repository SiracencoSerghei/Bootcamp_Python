"""Instructions

You are going to write a program that will select a random name from a list of names.
The person selected will have to pay for everybody's food bill.

Important: You are not allowed to use the choice() function.

NOTE: In this exercise, you are working collaboratively with another programmer.
They already dealt with input() and writing the code needed to get hold of the names in the input area,
so you don't need to worry about that.

The other programmer has written the code to separate the names in the input area into individual names
and puts them inside a List called names.
For their code to work correctly,
you must enter all the names in the input area followed by comma then space. e.g. name, name, name

You can try printing names to see what it looks like
(but remember to remove that code when you submit the assignment).

Assume that names works like this:

input area: x, y, z,
names = ["x", "y", "z"]

Example Input

Angela, Ben, Jenny, Michael, Chloe

Note: notice that there is a space between the comma and the next name.
Example Output

Michael is going to buy the meal today!

Hints

    You might need the help of the len() function. https://stackoverflow.com/questions/1712227/how-do-i-get-the-number-of-elements-in-a-list

    Remember that Lists start at index 0!

"""

# You are working in a team of developers.
# Another developer has written the code to import the names in the inputs
# You can run the code to see what this names list looks like.
# Then change the names in the input to see how it imports the names.
# print(names)
# we have: ['Angela', 'Ben', 'Jenny', 'Michael', 'Chloe']
# 🚨 Remember to remove the print statement above when you submit.
import random

names = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]
people_quantity = len(names)
print(f"we are in {people_quantity} people.")
chosen_person = names[random.randint(0, (people_quantity - 1))]
print(f"{chosen_person.capitalize()} is going to buy the meal today!")

states_of_usa = [
    "Alabama",
    "Alaska",
    "Arizona",
    "Arkansas",
    "California",
    "Colorado",
    "Connecticut",
    "Delaware",
    "Florida",
    "Georgia",
    "Hawaii",
    "Idaho",
    "Illinois",
    "Indiana",
    "Iowa",
    "Kansas",
    "Kentucky",
    "Louisiana",
    "Maine",
    "Maryland",
    "Massachusetts",
    "Michigan",
    "Minnesota",
    "Mississippi",
    "Missouri",
    "Montana",
    "Nebraska",
    "Nevada",
    "New Hampshire",
    "New Jersey",
    "New Mexico",
    "New York",
    "North Carolina",
    "North Dakota",
    "Ohio",
    "Oklahoma",
    "Oregon",
    "Pennsylvania",
    "Rhode Island",
    "South Carolina",
    "South Dakota",
    "Tennessee",
    "Texas",
    "Utah",
    "Vermont",
    "Virginia",
    "Washington",
    "West Virginia",
    "Wisconsin",
    "Wyoming",
]
print(states_of_usa[1])
print(states_of_usa.index("Pennsylvania"))
