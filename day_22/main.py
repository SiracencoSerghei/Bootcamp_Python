import time
from turtle import Screen, Turtle

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(l_paddle.go_up, "Up")
screen.onkey(l_paddle.go_down, "Down")

screen.onkey(r_paddle.go_up, "Page_Up")
screen.onkey(r_paddle.go_down, "Page_Down")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        # needs to bounce
        ball.bounce_y()

    # detect collision with l_paddle
    if (
        ball.distance(r_paddle) < 50
        and ball.xcor() > 320
        or ball.distance(l_paddle) < 50
        and ball.xcor() < -320
    ):
        ball.bounce_x()

    # detect when the ball is out of the paddle:
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        scoreboard.update_scoreboard()
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        scoreboard.update_scoreboard()


screen.exitonclick()
