from turtle import Turtle, Screen
import random


is_race_on = False
screen = Screen()
screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title = "Make your bet", prompt = "Which turtle will win the race? Enter a colour: ")
colours = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
y = -70
for turtle_index in range(0, 6):
    turtle = Turtle(shape = "turtle")
    turtle.color(colours[turtle_index])
    turtle.penup()
    turtle.goto(x = -230, y = y)
    y += 30
    all_turtles.append(turtle)
if user_bet:
    is_race_on = True
while is_race_on:
    for turtle_ in all_turtles:
        if turtle_.xcor() > 230:
            is_race_on = False
            winning_colour = turtle.pencolor()
            if winning_colour == user_bet:
                print(f"You've won! The {winning_colour} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_colour} turtle is the winner!")
        rand_distance = random.randint(0, 10)
        turtle_.forward(rand_distance)
screen.exitonclick()