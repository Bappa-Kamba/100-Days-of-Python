from turtle import Turtle
import os


ALIGNMENT = "center"
FONT = ("Arial", 12, "normal")

file_path = os.path.abspath("DAY-24/Snake-Game/data.txt")

def read_high_score():
    with open(file_path, mode='r') as file:
        high_score = file.read()
    return high_score

def write_high_score(score):
    with open(file_path, mode='w') as file:
        file.write(score)


class Scoreboard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.high_score = int(read_high_score())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-20, 275)
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            write_high_score(str(self.high_score))

        self.score = 0
        self.display_score()
        

    # def game_over(self):
    #     self.home()
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.score += 1
        self.display_score()