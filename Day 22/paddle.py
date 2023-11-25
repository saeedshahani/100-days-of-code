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