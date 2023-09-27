from turtle import Turtle

# Set some constants
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        segments = Turtle(shape="square")
        segments.color("white")
        segments.penup()
        segments.goto(position)
        self.snake.append(segments)

    def reset(self):
        for segment in self.snake:
            segment.goto(1000, 1000)  # Go off-screen
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]

    def extend(self):
        self.add_segment(self.snake[-1].position())

    def move(self):
        for seg_num in range(len(self.snake) - 1, 0, -1):  # start, stop, step
            new_x = self.snake[seg_num - 1].xcor()
            new_y = self.snake[seg_num - 1].ycor()
            self.snake[seg_num].goto(new_x, new_y)
        self.head.forward(DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:  # Prevent moving directly opposite direction
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
