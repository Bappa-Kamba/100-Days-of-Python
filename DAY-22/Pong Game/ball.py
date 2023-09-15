from turtle import Turtle

class Ball(Turtle):

    def __init__(self, shape="circle") -> None:
        super().__init__()
        self.shape(shape)
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
        

    def move(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x, y)

    def bounce(self, pos):
        if pos == 'x':
            self.x_move *= -1 
            self.move_speed *= 0.9           
        else:
            self.y_move *= -1

    def reset(self):
        self.move_speed = 0.1
        self.home()
        self.bounce('x')
        self.bounce('y')
        self.move()