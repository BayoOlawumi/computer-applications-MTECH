import turtle

def draw_bar(t,height):
    t.begin_fill()
    t.left(90)
    t.forward(height)
    t.write(" "+str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()
    t.forward(10)

win = turtle.Screen()
win.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color('blue','red')
tess.pensize(3)

xs = [48,117,200,240,160,260,220]

for a in xs:
    if a>200:
        tess.color('blue','red')
    elif a>=100 and a<=200:
        tess.color('blue','yellow')
    elif a<100:
        tess.color('blue','green')
    draw_bar(tess, a)

win.mainloop()