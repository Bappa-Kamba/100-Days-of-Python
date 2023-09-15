from time import sleep
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.bgcolor('black')
screen.tracer(0)

r_paddle = Paddle((380, 0))
l_paddle = Paddle((-380, 0))
ball = Ball()
score = Scoreboard()

screen.listen()

screen.onkeypress(fun=r_paddle.up, key="Up")
screen.onkeypress(fun=r_paddle.down, key="Down")
screen.onkeypress(fun=l_paddle.up, key="w")
screen.onkeypress(fun=l_paddle.down, key="s")



game_on = True
while game_on:
    screen.update()
    sleep(ball.move_speed)
    ball.move()

    # Detect collision with top or bottom walls
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce('y')

    # Detect collision with paddles
    if ball.distance(r_paddle) < 60 and ball.xcor() >= 350:
        # print(ball.distance(r_paddle))
        ball.bounce('x')

    elif ball.xcor() > 370:
        ball.reset()
        score.increase_l_score()

    if ball.distance(l_paddle) < 50 and ball.xcor() <= -360:
        ball.bounce('x')

    elif ball.xcor() < -380:
        ball.reset()
        score.increase_r_score()

screen.exitonclick()