# import colorgram as c
#
# extracted_colours = c.extract("hirst.jpg", 30)
# colours = []
# for colour in extracted_colours:
#     r = colour.rgb.r
#     g = colour.rgb.g
#     b = colour.rgb.b
#     new_colour = (r, g, b)
#     colours.append(new_colour)
# print(colours)
import turtle as t
import random

dots = t.Turtle()
dots.speed("fastest")
dots.hideturtle()

colours = [(226, 234, 228), (206, 161, 82), (55, 88, 129), (142, 91, 41), (221, 207, 107),
           (138, 26, 48), (133, 175, 200), (157, 47, 84), (46, 55, 102), (169, 159, 41),
           (131, 188, 145), (82, 20, 43), (36, 43, 68), (186, 93, 106), (189, 139, 163), (87, 115, 177), (87, 156, 97),
           (59, 39, 33), (79, 154, 165), (196, 81, 71), (54, 128, 122), (45, 73, 76), (162, 202, 216), (44, 75, 73),
           (78, 76, 45), (167, 207, 165), (219, 175, 187)]
t.colormode(255)
dots.penup()
y_pos = -250
dots.setposition(-250, y_pos)
dots.pendown()

for _ in range(0, 10):
    dots.goto(-250, y_pos)
    dots.pendown()
    y_pos += 50
    for _ in range(0, 10):
        dots.dot(20, random.choice(colours))
        dots.penup()
        dots.forward(50)
        dots.pendown()
    dots.penup()


screen = t.Screen()
screen.exitonclick()
