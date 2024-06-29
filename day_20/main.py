import time
from turtle import Screen

from snake import Snake


def run_game():
    screen = Screen()
    screen.setup(width=800, height=800)
    screen.bgcolor("black")
    screen.title("My Snake Game")
    screen.tracer(0)

    snake = Snake(screen)  # Pass the screen object to the Snake class

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        if snake.is_at_border():
            continue
        snake.move()

    screen.exitonclick()


run_game()
