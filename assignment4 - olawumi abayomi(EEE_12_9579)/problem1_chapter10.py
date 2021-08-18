import turtle
import random

turtle.setup(400,500)
wn = turtle.Screen()
wn.title("Handling Keypresses!")
wn.bgcolor("Lightgreen")
tess = turtle.Turtle()

# Set an initial size for tess
global initial_pensize
initial_pensize = 2
tess.pensize(initial_pensize)
tess_head = ['circle', 'arrow', 'turtle','triangle','classic','arrow']
bg_colors = ['orange','blue','red','yellow','green','red','black']

"""
    User defined Function
"""
def h1():
    tess.forward(30)

def h2():
    tess.left(45)

def h3():
    tess.right(45)

def tess_to_red():
    tess.pencolor('red')

def tess_to_green():
    tess.pencolor('green')

def tess_to_blue():
    tess.pencolor('blue')

# Increase tess size by pressing +
def increase_tess_size():
    global initial_pensize
    if initial_pensize < 20:
        initial_pensize+=1
        tess.pensize(initial_pensize)
    else:
        return initial_pensize

# Decrease size by pressing -
def decrease_tess_size():
    global initial_pensize
    if initial_pensize ==1:
        return initial_pensize
    else:
        initial_pensize-=1
        tess.pensize(initial_pensize)

# Randomly change background color
def change_bg_color():
    new_color = random.choice(bg_colors)
    wn.bgcolor(new_color)

# Change Tess Head randomly
def change_tess_head():
    new_head = random.choice(tess_head)
    tess.shape(new_head)

def h4():
    wn.bye()


wn.onkey(h1, 'Up')
wn.onkey(h2, "Left")
wn.onkey(h3,"Right")
wn.onkey(h4,"q")
wn.onkey(tess_to_red, 'r')
wn.onkey(tess_to_green, 'g')
wn.onkey(tess_to_blue, 'b')

# Increase Pensize using + and decrease using -
wn.onkey(decrease_tess_size, "-")
wn.onkey(increase_tess_size, '+')

# Change backgroundcolor using b
wn.onkey(change_bg_color, 'b')

# Change Turtle Head
wn.onkey(change_tess_head, 'h')



wn.listen()
wn.mainloop()