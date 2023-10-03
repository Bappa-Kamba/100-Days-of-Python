from turtle import Turtle, Screen
from random import randint
from time import sleep

screen = Screen()
screen.setup(width=800, height=600)
user_bet = screen.textinput(title="Turtle Race Bet", 
                            prompt="What turtle are you rooting for? Enter a color: ").lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
start_race = False


x_cor = -380
y_cor = -100

for color in colors:
    t = Turtle(shape="turtle")
    t.color(color)
    t.penup()
    t.goto(x=x_cor, y=y_cor)
    y_cor += 40
    turtles.append(t)

if user_bet:
    start_race = True

while start_race:
    for turtle in turtles:
        rand_distance = randint(0, 10)
        turtle.fd(rand_distance)
        if turtle.xcor() > 380:
            start_race = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You've won! The {winner} turtle won the race!")
            else:
                print(f"You've lost! The {winner} turtle won the race!")


screen.exitonclick()