

import turtle
win = turtle.Screen()
win.bgcolor("lightgreen")
win.title(" Polygon Drawer ")

# Equilateral
equilateral = turtle.Turtle()
# Make the line thicker
equilateral.pensize(3)
equilateral.color('green')
for a in [1,2,3]:
    equilateral.forward(60)
    equilateral.left(120)


# Square
square = turtle.Turtle()
square.pensize(3)
square.color('blue')
for a in [1,2,3,4]:
    square.forward(60)
    square.left(90)

# Hexagon
hexagon = turtle.Turtle()
hexagon.pensize(3)
hexagon.color('red')
for a in [1,2,3,4,5,6]:
    hexagon.forward(60)
    hexagon.left(60)


# Octagon
octagon = turtle.Turtle()
octagon.pensize(3)
octagon.color('black')
for a in [1,2,3,4,5,6,7,8]:
    octagon.forward(60)
    octagon.left(45)



win.mainloop()










