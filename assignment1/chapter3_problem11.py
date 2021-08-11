import turtle
# Create a window
win = turtle.Screen()
win.bgcolor("Star Drawer")
star = turtle.Turtle()

for i in [1,2,3,4,5]:
    # Move forward by 100
    star.forward(100)
    # Turtle head makes angle in the clockwise direction
    star.right(144)
star.pendown()

win.mainloop()