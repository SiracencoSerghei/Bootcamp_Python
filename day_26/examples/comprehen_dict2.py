"""You are going to use Dictionary Comprehension to create a dictionary called weather_f that takes each temperature in degrees Celsius and converts it into degrees Fahrenheit.

To convert temp_c into temp_f use this formula:

(temp_c * 9/5) + 32 = temp_f

Do NOT Create a dictionary directly. Try to use Dictionary Comprehension instead of a Loop.

The eval() function will help us convert the string input into a Python dictionary, provided that the inputs are already formatted with the correct syntax.
Example Input

{"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

Example Output

{'Monday': 53.6, 'Tuesday': 57.2, 'Wednesday': 59.0, 'Thursday': 57.2, 'Friday': 69.8, 'Saturday': 71.6, 'Sunday': 75.2}

Hint

    Use the keyword method for starting the Dictionary comprehension and fill in the relevant parts.

    You can get each of the items from a dictionary using the .items() method: https://www.w3schools.com/python/ref_dictionary_items.asp
"""

weather_c = eval(input())
# 🚨 Don't change code above 👆


# Write your code 👇 below:
# {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

# temp_f = (temp_c * 9/5) + 32
weather_f = {
    day: ((temperature * 9 / 5) + 32) for day, temperature in weather_c.items()
}

print(weather_f)
