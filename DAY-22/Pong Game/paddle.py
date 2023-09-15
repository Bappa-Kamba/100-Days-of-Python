from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position) -> None:
        super().__init__()
        self.shape("square")
        self.color('white')
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)
        self.score = 0


    def up(self):
        new_y = self.ycor() + 20
        self.goto(x=self.xcor(), y=new_y)
            

    def down(self):
        new_y = self.ycor() - 20
        self.goto(x=self.xcor(), y=new_y)

    def increase_score(self):
        self.score += 1
