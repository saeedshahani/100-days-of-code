from turtle import Turtle
from ball import Ball
MOVE_DISTANCE = 20

class Paddle(Turtle):
    def __init__(self, placement: str) -> None:
        super().__init__()
        self.placement = placement
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(placement)
    
    def move(self, direction: int) -> None:
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE * direction)

    def up(self) -> None:
        if self.ycor() + MOVE_DISTANCE <= 240:
            self.move(direction=1)

    def down(self) -> None:
        if self.ycor() - MOVE_DISTANCE >= -240:
            self.move(direction=-1)

# class AutoPaddle(Paddle):
#     def __init__(self, placement: str) -> None:
#         super().__init__(placement)
#         self.ball_x: int = 0
#         self.ball_y: int = 0

#     def react_to_ball(self, ball: Ball) -> None:
#         x_factor = ball.xcor() / self.ball_x
#         y_factor = ball.ycor() / self.ball_y
#         if x_factor >= 0:
#             pass
#         self.ball_x = ball.xcor()
#         self.ball_y = ball.ycor()