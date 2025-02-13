from turtle import Turtle
SNAKE_SIZE=20
UP=90
LEFT=180
DOWN=270
RIGHT=0
class Snake:
    snake_parts = []
    snake_size = 3
    head:Turtle
    def __init__(self,initial_size):
        self.initial_size=initial_size
        self.snake_size=initial_size

    def initialize(self):
        for i in range(0, self.snake_size):
            self.add_snake_part((-1 * i * SNAKE_SIZE, 0))
        self.head=self.snake_parts[0]

    def reset(self):
        self.snake_size = self.initial_size
        #can not remove turtle from screen. So move to a far point
        for sp in self.snake_parts:
            sp.goto(1000,1000)
        self.snake_parts=[]

    def add_snake_part(self,position):
        snake_part = Turtle("square")
        snake_part.penup()
        snake_part.setposition(position)
        snake_part.color("white")
        snake_part.pencolor("white")
        self.snake_parts.append(snake_part)

    def increase_size(self):
        self.add_snake_part(self.snake_parts[-1].position())

    def move_forward(self):
        for sp_num in range(len(self.snake_parts) - 1, 0, -1):
            sp = self.snake_parts[sp_num]
            sp_pre = self.snake_parts[sp_num - 1]
            sp.goto(sp_pre.xcor(), sp_pre.ycor())
        self.head.forward(SNAKE_SIZE)

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