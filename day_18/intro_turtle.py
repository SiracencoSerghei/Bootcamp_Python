##### Turtle Intro ######

from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")
timmy_the_turtle.penup()
timmy_the_turtle.goto(0, 0)
timmy_the_turtle.pendown()
timmy_the_turtle.shapesize(2, 2)

jimmy_the_turtle = Turtle()
jimmy_the_turtle.shape("turtle")
jimmy_the_turtle.color("blue")
jimmy_the_turtle.penup()
jimmy_the_turtle.goto(15, 15)
jimmy_the_turtle.pendown()
jimmy_the_turtle.shapesize(1, 1.5)

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

timmy_the_turtle.backward(100)
timmy_the_turtle.left(90)
timmy_the_turtle.forward(100)
timmy_the_turtle.right(90)
timmy_the_turtle.forward(100)
timmy_the_turtle.right(90)
timmy_the_turtle.forward(100)

jimmy_the_turtle.circle(100, 100, 6)

######## Challenge 2 - Dashed line ############

from turtle import Turtle, Screen

class CustomTurtle(Turtle):
    def dashed_line(self, length=100, dash_length=10):
        for _ in range(length // dash_length):
            self.pendown()
            self.forward(dash_length)
            self.penup()
            self.forward(dash_length)

    def normal_line(self, length=100):
        self.pendown()
        self.forward(length)
        self.penup()

# Create screen object
screen = Screen()

# Create timmy_the_turtle with CustomTurtle class and set its attributes
timmy_the_turtle = CustomTurtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")
timmy_the_turtle.penup()
timmy_the_turtle.goto(0, 0)
timmy_the_turtle.pendown()
timmy_the_turtle.shapesize(2, 2)

# Create jimmy_the_turtle with CustomTurtle class and set its attributes
jimmy_the_turtle = CustomTurtle()
jimmy_the_turtle.shape("turtle")
jimmy_the_turtle.color("blue")
jimmy_the_turtle.penup()
jimmy_the_turtle.goto(15, 15)
jimmy_the_turtle.pendown()
jimmy_the_turtle.shapesize(1, 1.5)

######## Challenge 1 - Draw a Square ############

timmy_the_turtle.backward(100)
timmy_the_turtle.left(90)
timmy_the_turtle.forward(100)
timmy_the_turtle.right(90)
timmy_the_turtle.forward(100)
timmy_the_turtle.right(90)
timmy_the_turtle.forward(100)

jimmy_the_turtle.circle(100, 100, 6)

# Draw a dashed line with timmy_the_turtle
timmy_the_turtle.dashed_line()

# Draw a normal line with timmy_the_turtle
timmy_the_turtle.normal_line(100)


screen.exitonclick()
