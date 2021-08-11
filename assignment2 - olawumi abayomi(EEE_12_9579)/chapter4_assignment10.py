import turtle
# Create a window
win = turtle.Screen()
win.bgcolor("lightgreen")
star = turtle.Turtle()
star.width(2)
star.color("brown")
star.speed(3)

def star_drawer():
    for i in range(5):
        # Move forward by 100
        star.forward(100)
        # Turtle head makes angle in the clockwise direction
        star.right(144)
    star.penup()


position = 72

for a in range(5):
    star.pendown()
    star_drawer()
    star.left(position)
    star.penup()
    star.fd(140)
    star.pendown()
    star.seth(0)
    position+=72

win.mainloop()