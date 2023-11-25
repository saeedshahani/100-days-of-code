from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

paddle_left = Paddle((-380,0))
paddle_right = Paddle((380,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle_left.up, "Up")
screen.onkey(paddle_left.down, "Down")
screen.onkey(paddle_right.up, "w")
screen.onkey(paddle_right.down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    #Detect collision with wall
    if not -280 < ball.ycor() < 280:
        ball.bounce_y()
    #Detect collision with paddles
    if (
        ball.distance(paddle_left) < 50 and ball.xcor() < -340) or (
        ball.distance(paddle_right) < 55 and ball.xcor() < 340):
        ball.bounce_x()
    #Detect if paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.point_left()
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.point_right()
    #Move right paddle automatically
    #paddle_right.react_to_ball(ball)

screen.exitonclick()