#
#Initially extract the pallet
#import colorgram
#
# # Extract 6 colors from an image.
# colors = colorgram.extract('image.jpg', 120)
#
# # colorgram.extract returns Color objects, which let you access
# # RGB, HSL, and what proportion of the image was that color.
#
# color_array = []
# count = 0
# for color in colors:
#     if count == 0:
#         count+=1
#         continue
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_array.append((r,g,b))

color_array = [(222, 219, 215), (225, 220, 223), (170, 145, 126), (132, 111, 102), (222, 230, 226), (222, 205, 119), (123, 90, 99), (202, 95, 76), (149, 161, 185), (81, 84, 130), (176, 147, 156), (154, 146, 87), (228, 172, 164), (148, 162, 150), (62, 23, 32), (178, 188, 214), (99, 113, 100), (179, 98, 107), (48, 47, 114), (224, 174, 181), (104, 40, 49), (136, 31, 25), (111, 118, 159), (40, 28, 74), (117, 137, 114), (96, 17, 11), (184, 196, 190), (80, 75, 40), (183, 196, 198), (57, 63, 61), (110, 135, 139), (224, 201, 27)]


# 10*10 figure spaced by 50 places and radius 20 of circle

from turtle import Turtle, Screen
import random
x_position = -270
y_position = 240



def set_position(hirst_turtle):
    global x_position
    global y_position
    hirst_turtle.penup()
    hirst_turtle.setx(x_position)
    hirst_turtle.sety(y_position)

def run():
    global  y_position
    for i in range(0,10):
        for j in range(0,10):
            hirst_turtle.forward(50)
            hirst_turtle.dot(20,random.choice(color_array))
        y_position = y_position - 50
        set_position(hirst_turtle)


hirst_turtle = Turtle()
hirst_turtle.shape("turtle")
hirst_turtle.hideturtle()
screen = Screen()
screen.colormode(255)
screen.bgcolor("white")
set_position(hirst_turtle)
run()

screen.exitonclick()
