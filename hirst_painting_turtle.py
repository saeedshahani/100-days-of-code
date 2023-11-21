# import colorgram
#
# rgb_colours = []
# colours = colorgram.extract('image.jpg', 30)
# for colour in colours:
#     r = colour.rgb.r
#     g = colour.rgb.g
#     b = colour.rgb.b
#     new_colour = (r, g, b)
#     rgb_colours.append(new_colour)
#
# print(rgb_colours)

import turtle as t
import random

colour_list = [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53),
               (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48),
               (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155),
               (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203), (150, 115, 120), (202, 185, 190),
               (40, 72, 82), (46, 73, 62), (47, 66, 82)]

t.colormode(255)
tx = t.Turtle()
tx.hideturtle()
tx.speed(0)
tx.setheading(225)
tx.penup()
tx.forward(300)
tx.setheading(0)
for _ in range(10):
    for __ in range(10):
        tx.dot(20, random.choice(colour_list))
        tx.forward(50)
    tx.setheading(90)
    tx.forward(50)
    tx.setheading(180)
    tx.forward(50*10)
    tx.setheading(0)
screen = t.Screen()
screen.exitonclick()