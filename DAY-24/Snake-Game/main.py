from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from random import randint
from time import sleep

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()

screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_on = True
while game_on:
    screen.update()
    sleep(0.1)
    snake.move_snake()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        scoreboard.increase_score()

    # Detect collision with walls
    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    # Detect collision with snake body
    for body_part in snake.snake_body[1:]:
        if snake.head.distance(body_part) < 10:
            scoreboard.reset()
            snake.reset()



screen.exitonclick()