from turtle import Turtle
from random import randint, choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    
    def __init__(self):
        self.all_cars = []
        self.move_distance = STARTING_MOVE_DISTANCE


    def create_car(self):
        chance = randint(1, 6)
        if chance == 1 :
            new_car = Turtle()
            new_car.shape('square')
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.seth(180)
            new_car.color(choice(COLORS))
            new_car.goto(300, randint(-230, 250))
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.fd(self.move_distance)

    def speed_up(self):
        self.move_distance += MOVE_INCREMENT

