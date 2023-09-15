from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 290


class Player(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)
        self.finish_line = FINISH_LINE_Y

    def move(self):
        self.fd(MOVE_DISTANCE)

    def reset(self):
        self.goto(STARTING_POSITION)

