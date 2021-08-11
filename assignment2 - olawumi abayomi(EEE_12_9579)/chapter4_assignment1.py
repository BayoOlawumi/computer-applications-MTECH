import turtle

# Declaration of variables and creation of objects
square_drawer = turtle.Turtle()
win = turtle.Screen()
win.bgcolor("lightgreen")
square_drawer.width(2)
square_drawer.color("brown")
position = [40,80,120,160]

# The function named non_fruitful
def non_fruitful():
    for b in range(4):
        square_drawer.forward(20)
        square_drawer.left(90)
    square_drawer.forward(20)

# The main program
# Drawing of the 4 square
for a in range(4):
    # Calling the function
    non_fruitful()
    square_drawer.penup()
    square_drawer.setx(position[a])
    square_drawer.pendown()

win.mainloop()