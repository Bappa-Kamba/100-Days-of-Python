import turtle as t
from turtle import Turtle, Screen
from random import choice, randint

t.colormode(255)

tim = Turtle()
tim.speed(0)


directions = [0, 90, 180, 270]


def draw_shape(sides):
    angle = 360/int(sides)

    for _ in range(sides):
        tim.fd(100)
        tim.right(angle)
    tim.color(random_color())


def random_color():
    random_color = (randint(0, 255), randint(0, 255), randint(0, 255))
    return random_color


def draw_spirograph(size):
    for i in range(360 //size):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size)

for i in range(3, 11):
    draw_shape(i)

screen = Screen()
screen.exitonclick()