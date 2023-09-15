import turtle as t
from random import choice, randint

t.colormode(255)
screen = t.Screen()

tim = t.Turtle()
tim.speed(0)
tim.penup()
tim.ht()

color_list = [(222, 163, 66), (19, 45, 87), (136, 61, 84),
              (177, 60, 44), (126, 40, 61), (21, 86, 61), (59, 48, 37),
              (250, 194, 42), (13, 117, 146), (57, 146, 72), (229, 86, 36), (231, 172, 190),
              (57, 71, 39), (197, 102, 134), (197, 125, 150), (156, 191, 185), (30, 67, 58),
              (166, 204, 202), (62, 26, 45), (145, 165, 181), (6, 79, 111),
              (35, 44, 99), (71, 153, 84), (120, 41, 33), (170, 203, 205), (223, 178, 169)
]

tim.setheading(225)
tim.forward(325)
tim.setheading(0)

for num in range(10):
    for _ in range(10):
        tim.dot(20, choice(color_list))
        tim.fd(50)
    if num % 2 == 0:
        tim.left(90)
        tim.fd(50)
        tim.left(90)
        tim.fd(50)
    else:
        tim.right(90)
        tim.fd(50)
        tim.right(90)
        tim.fd(50)

    

screen.exitonclick()