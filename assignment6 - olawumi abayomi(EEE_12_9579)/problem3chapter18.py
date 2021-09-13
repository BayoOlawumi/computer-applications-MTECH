#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      BayoOlawumi
#
# Created:     13/09/2021
# Copyright:   (c) BayoOlawumi 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import turtle
order = int(input("Please Enter the number of order"))
class Point:
    # I use my point class for convenience
    # A constructor method created here
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def mid_point(self, target):
        return Point(0.5*(self.x+target.x), 0.5*(self.y+target.y))

my_turtle = turtle.Turtle()
my_turtle.speed(0)
my_turtle.hideturtle()
my_turtle.pensize(2)
screen = turtle.Screen()
screen.bgcolor('Lightgreen')

# draw a triangle by connecting p0-p1, p1-p2, and p2-p0, respectively
def draw_triangle(t, p0, p1, p2):
    t.penup()
    t.goto(p0.x, p0.y)
    t.pendown()
    t.goto(p1.x, p1.y)
    t.goto(p2.x, p2.y)
    t.goto(p0.x, p0.y)


def my_sierpinski(t, p0, p1, p2, order):
    if order == 0:
        return
    draw_triangle(t, p0, p1, p2)
    p0_1 = p0.mid_point(p1)
    p1_2 = p1.mid_point(p2)
    p2_0 = p2.mid_point(p0)
    my_sierpinski(t, p0_1, p1, p1_2, order - 1)
    my_sierpinski(t, p0, p0_1, p2_0, order - 1)
    my_sierpinski(t, p2_0, p1_2, p2, order - 1)

startPoint = Point(-400, -350)  # coordinate of the bottom left corner
size = 800  # side length of the biggest triangle
color = "Black"
# You can change recursion depth here


my_sierpinski(my_turtle, startPoint, Point(startPoint.x+size/2, startPoint.y+size/2*3**0.5),
           Point(startPoint.x+size, startPoint.y), order)
screen.mainloop()