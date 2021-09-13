import turtle

my_turtle = turtle.Turtle()
my_turtle.speed(0)
my_turtle.hideturtle()
screen = turtle.Screen()
screen.bgcolor('Lightgreen')
my_turtle.pencolor("blue")
my_turtle.pensize(4)


def koch(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        koch(t, order - 1, size / 3)
        t.left(angle)


def shape(t, order, size, sides):
    for i in range(sides):
        koch(t, order, size)
        t.right(360 / sides)


size = 400
my_turtle.penup()
my_turtle.goto(-size / 2, size / 2)
my_turtle.pendown()
shape(my_turtle, 3, size, 3)
screen.mainloop()