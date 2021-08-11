import turtle
win = turtle.Screen()
win.title(" Clock Drawer ")
win.bgcolor('lightgreen')

clock = turtle.Turtle()
clock.penup()
clock.shape('turtle')
angle = 0
clock.speed(10)
for a in range(12):
    clock.left(angle)
    clock.forward(150)
    clock.stamp()
    clock.home()
    angle+=30


clock1 = turtle.Turtle()
clock1.penup()
clock1.shape('classic')
angle2 = 0
clock1.speed(10)
for b in range(12):
    clock1.left(angle2)
    clock1.forward(120)
    clock1.stamp()
    clock1.home()
    angle2+=30



win.mainloop()