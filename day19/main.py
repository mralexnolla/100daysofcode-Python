# import colorgram
#
# color = colorgram.extract('image.jpg', 100)
#
# rgb_colors = []
# for i in range(len(color)):
#     g = color[i].rgb.g
#     r = color[i].rgb.r
#     b = color[i].rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)


tim = Turtle()
tim.shape('turtle')
tim.color("green", "red")
tim.speed('fastest')

color_list = [(236, 224, 80), (197, 7, 71), (195, 164, 13), (201, 75, 15), (231, 54, 132), (110, 179, 216),
              (217, 163, 101), (27, 105, 168), (35, 186, 109), (19, 29, 168), (13, 23, 66), (212, 135, 177),
              (233, 223, 7), (199, 33, 132), (13, 183, 212), (230, 166, 199), (126, 189, 162), (8, 49, 28),
              (40, 132, 77), (128, 219, 232), (58, 12, 25), (67, 22, 7), (114, 90, 210), (146, 216, 199), (179, 17, 8),
              (233, 66, 34), (11, 97, 52), (169, 181, 232), (241, 169, 155), (252, 7, 40), (10, 84, 100), (63, 98, 8),
              (14, 51, 250), (250, 11, 8)]

tim.setheading(225)
tim.penup()
tim.forward(300)
tim.setheading(0)

number_of_dots = 100

for i in range(1, number_of_dots):
    tim.dot(15, random.choice(color_list))
    tim.penup()
    tim.forward(20)

    if i % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(200)
        tim.setheading(0)



screen = Screen()
screen.exitonclick()
