import random
from turtle import Screen, Turtle

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race? Enter a color: "
)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
winning_color = ""
result_text = ""
all_turtles = []

# Create 6 turtles
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        # 230 is 250 - half the width of the turtle.
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()

            if winning_color == user_bet:
                result_text = f"The {winning_color} turtle is the winner!\nYou've won!"
            else:
                result_text = f"The {winning_color} turtle is the winner!\nYou've lost!"

        # Make each turtle move a random amount.
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

# Display the result on the screen after the race is over
result_turtle = Turtle()
result_turtle.hideturtle()
result_turtle.penup()
result_turtle.goto(x=0, y=-150)
result_turtle.write(result_text, align="center", font=("Arial", 12, "normal"))

screen.exitonclick()
