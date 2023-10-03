from turtle import Turtle

TURTLE_SHAPE = "square"
COLOR = 'white'
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0 

class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        x_cor = 0
        for _ in range(3):
            snake_segment = Turtle(shape=TURTLE_SHAPE)
            snake_segment.color(COLOR)
            snake_segment.penup()
            snake_segment.goto((x_cor), 0)
            x_cor = snake_segment.xcor() - 20
            self.snake_body.append(snake_segment)

    def extend_snake(self):
        snake_segment = Turtle(shape=TURTLE_SHAPE)
        snake_segment.color(COLOR)
        snake_segment.penup()
        pos = self.snake_body[-1].pos()
        snake_segment.goto(pos)
        self.snake_body.append(snake_segment)
        

    def move_snake(self):
        snake = self.snake_body
        for part_num in range(len(snake) - 1, 0, -1):
            new_x_cor = snake[part_num - 1].xcor()
            new_y_cor = snake[part_num - 1].ycor()
            snake[part_num].goto(new_x_cor, new_y_cor)
        snake[0].fd(20)

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