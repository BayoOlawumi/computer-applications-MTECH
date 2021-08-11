import turtle

# Declaration of variables and creation of objects
turt = turtle.Turtle()
win = turtle.Screen()
win.bgcolor("lightgreen")
turt.width(2)
turt.color("brown")
turt.speed(10)
size = 150

def draw_square(t, sz):
    for b in range(4):
        t.forward(sz)
        t.left(90)

def draw_grid(t, sz):
    for i in range(4):
        # Calling the function draw_square
        draw_square(t, sz)
        t.left(90)


angle = 0
for i in range(5):
    draw_grid(turt, size)
    turt.left(18)

win.mainloop()