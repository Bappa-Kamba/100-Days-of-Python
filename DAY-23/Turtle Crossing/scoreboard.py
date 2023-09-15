from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-290, 260)
        self.display_level()

    
    def display_level(self):
        self.clear()
        self.write(f'Level: {self.level}', font=FONT)

    def update_level(self):
        self.level += 1
        self.display_level()

    def game_over(self):
        self.home()
        self.write('GAME OVER', align='center', font=FONT)
        


