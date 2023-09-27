# from turtle import *  # Asterisk could be confusing if complex code as it's hard to determine the origin of the function
# import turtle as t
# tim = t.Turtle()
import turtle as t
from turtle import Screen
import random
# from turtle import Turtle, Screen
# import random


# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("DarkBlue")
# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)

# tim = Turtle()
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()


# def shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
#
# colours = ["pale green", "cornflower blue", "pale turquoise", "firebrick", "medium purple", "hot pink",
#            "light salmon", "slate blue", "khaki"]
# for n in range(3, 11):
#     tim.color(random.choice(colours))
#     shape(n)
tim = t.Turtle()


# def random_colour():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     colour = (r, g, b)
#     return colour
#
#
# t.colormode(255)
# tim.speed("fastest")
# tim.pensize(10)
# angle = [0, 90, 180, 270]
# turn_around = ["left", "right"]
# for i in range(200):
#
#     tim.color(random_colour())
#     tim.forward(30)
#     tim.color(random_colour())
#     tim.setheading(random.choice(angle))


t.colormode(255)


def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour = (r, g, b)
    return colour

# SPIROGRAPH
# tim.speed("fastest")
# angle = 10
# steps = int(360/angle)
# for _ in range(steps):
#     tim.circle(100)
#     tim.color(random_colour())
#     tim.right(angle)
tim.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_colour())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)



# Hold screen until click
screen = Screen()
screen.exitonclick()
