from turtle import Screen, Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self, screen):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.screen = screen

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        for seg_num in range((len(self.segments) - 1), 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
        # if self.is_at_border():
        #     # Move all segments to the opposite side of the screen
        #     for segment in self.segments:
        #         segment.goto(-segment.xcor(), -segment.ycor())

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def is_at_border(self):
        # Get the current screen dimensions
        screen_width = self.screen.window_width() / 2
        screen_height = self.screen.window_height() / 2

        # Check if the head is at the border based on its current heading
        if self.head.heading() == UP and self.head.ycor() >= screen_height:
            return True
        elif self.head.heading() == DOWN and self.head.ycor() <= -screen_height:
            return True
        elif self.head.heading() == LEFT and self.head.xcor() <= -screen_width:
            return True
        elif self.head.heading() == RIGHT and self.head.xcor() >= screen_width:
            return True

        return False

    def run_game(self):

        screen = Screen()
        screen.setup(width=600, height=600)
        screen.bgcolor("black")
        screen.title("My Snake Game")
        # screen.tracer(0)

        snake = Snake()
        # food = Food()

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
