import turtle

# Declaration of variables and creation of objects
square_drawer = turtle.Turtle()
win = turtle.Screen()
win.bgcolor("lightgreen")
square_drawer.width(2)
square_drawer.color("brown")

# The function named successive_drawer draws the each square
def successive_drawer(f_size):
    for b in range(4):
        square_drawer.forward(f_size)
        square_drawer.left(90)

# The main program
# Drawing of the 5 square
size = 0
# Iterating through each square
for a in range(5):
    # adjusting the size
    size = size + 20
    # Calling the function
    successive_drawer(size)
    square_drawer.penup()
    square_drawer.sety(-size/2)
    square_drawer.setx(-size/2)
    square_drawer.pendown()

win.mainloop()