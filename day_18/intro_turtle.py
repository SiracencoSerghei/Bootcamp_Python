##### Turtle Intro ######
import random

# from turtle import Turtle, Screen
#
# # Create screen object
# screen = Screen()
#
# timmy_the_turtle = Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red")
# timmy_the_turtle.penup()
# timmy_the_turtle.goto(0, 0)
# timmy_the_turtle.pendown()
# timmy_the_turtle.shapesize(2, 2)
#
# jimmy_the_turtle = Turtle()
# jimmy_the_turtle.shape("turtle")
# jimmy_the_turtle.color("blue")
# jimmy_the_turtle.penup()
# jimmy_the_turtle.goto(15, 15)
# jimmy_the_turtle.pendown()
# jimmy_the_turtle.shapesize(1, 1.5)

# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(200)
# timmy_the_turtle.left(120)
# timmy_the_turtle.backward(100)
# timmy_the_turtle.setheading(0)

# jimmy_the_turtle.circle(50,)
# jimmy_the_turtle.right(60)
# jimmy_the_turtle.left(120)
# timmy_the_turtle.backward(200)

######## Challenge 1 - Draw a Square ############

# timmy_the_turtle.backward(100)
# timmy_the_turtle.left(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
#
# jimmy_the_turtle.circle(100, 100, 6)

######## Challenge 2 - Dashed line ############
# class CustomTurtle(Turtle):
#     def dashed_line(self, length=100, dash_length=10):
#         for _ in range(length // dash_length):
#             self.pendown()
#             self.forward(dash_length)
#             self.penup()
#             self.forward(dash_length)
#
#     def normal_line(self, length=100):
#         self.pendown()
#         self.forward(length)
#         self.penup()
#
# # Create timmy_the_turtle with CustomTurtle class and set its attributes
# timmy_the_turtle = CustomTurtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red")
# timmy_the_turtle.penup()
# timmy_the_turtle.goto(0, 0)
# timmy_the_turtle.pendown()
# timmy_the_turtle.shapesize(2, 2)
#
# # Create jimmy_the_turtle with CustomTurtle class and set its attributes
# jimmy_the_turtle = CustomTurtle()
# jimmy_the_turtle.shape("turtle")
# jimmy_the_turtle.color("blue")
# jimmy_the_turtle.penup()
# jimmy_the_turtle.goto(15, 15)
# jimmy_the_turtle.pendown()
# jimmy_the_turtle.shapesize(1, 1.5)
#
# ######## Challenge 2 - Draw a Square ############
#
# timmy_the_turtle.backward(100)
# timmy_the_turtle.left(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
#
# jimmy_the_turtle.circle(100, 100, 6)
#
# # Draw a dashed line with timmy_the_turtle
# timmy_the_turtle.dashed_line()
#
# # Draw a normal line with timmy_the_turtle
# timmy_the_turtle.normal_line(100)

######## Challenge 3 - Multi - side ############
# import turtle as t
#
# # Create screen object
# screen = t.Screen()
# tim = t.Turtle()
#
colours = [
    "CornflowerBlue",
    "DarkOrchid",
    "IndianRed",
    "DeepSkyBlue",
    "LightSeaGreen",
    "wheat",
    "SlateGray",
    "SeaGreen",
]

# def drow_shape(num_sides, side_length):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(side_length)
#         tim.right(angle)
#
# for shape_side_n in range(3, 11):
#     tim.color(random.choice(colours))
#     drow_shape(shape_side_n, 100)


######## Challenge 4 Random direction ############
# import turtle as t
#
# # Create screen object
# screen = t.Screen()
# tim = t.Turtle()
# directions = [0, 90, 180, 270]
# tim.pensize(15)
# tim.speed("fastest")
#
# for _ in range(200):
#     tim.color(random.choice(colours))
#     tim.forward(30)
#     tim.setheading(random.choice(directions))


######## Challenge 5 Spirograph ############
import turtle as t

tim = t.Turtle()
t.colormode(255)
# tim.pensize(15)
tim.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)


# Create screen object
screen = t.Screen()
screen.exitonclick()
