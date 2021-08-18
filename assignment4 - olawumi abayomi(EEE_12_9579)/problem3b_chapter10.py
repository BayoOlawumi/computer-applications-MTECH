#-------------------------------------------------------------------------------
import turtle

turtle.setup(700,600)
wn = turtle.Screen()
wn.title("Traffic light! - Press Space to change state")
wn.bgcolor("Lightgreen")
tess = turtle.Turtle()
pen = turtle.Turtle()
pen.penup()
pen.hideturtle()
pen.setpos(100,100)
pen.write("Automatic Traffic Control System", font=("Calibri", 13, "bold"))


tess_green = turtle.Turtle()
tess_orange = turtle.Turtle()
tess_red = turtle.Turtle()





def draw_housing2():
    """ Draw a nice housing to hold the traffic lights"""
    tess.pensize(3)
    tess.color("black", "darkgrey")
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.circle(40,180)
    tess.forward(200)
    tess.end_fill()


draw_housing2()

tess_red.hideturtle()
tess_orange.hideturtle()
tess_green.showturtle()

# Turn tess into a big green circle
tess_green.shape("circle")
tess_green.shapesize(3)
tess_green.fillcolor("green")

tess_red.shape("circle")
tess_red.shapesize(3)
tess_red.fillcolor("red")

tess_orange.shape("circle")
tess_orange.shapesize(3)
tess_orange.fillcolor("orange")

# Set position of circles
tess_green.setpos(40,40)
tess_red.setpos(40,120)
tess_orange.setpos(40,200)



# A traffic light is a kind of state machine with three states
# Green,Orange, Red. We number these states 0,1,2
# When the machine changes state, we change tess' position and
# her fillcolor

# This variable hold the current state of the machine
state_num = 0

def advance_state_machine():
    global state_num
    if state_num == 0:      #Transition from state 0 to state 1
        tess_red.hideturtle()
        tess_orange.hideturtle()
        tess_green.showturtle()
        state_num = 1
    elif state_num ==1:      #Transition from state 1 to state 2
        tess_red.showturtle()
        tess_orange.hideturtle()
        tess_green.hideturtle()
        state_num = 2
    else:
        tess_red.hideturtle()
        tess_orange.showturtle()
        tess_green.hideturtle()
        state_num = 0

    wn.ontimer(advance_state_machine, 800)

pen.setpos(120,70)
pen.write("This is preferable!", font=("Calibri", 10))
advance_state_machine()
wn.listen()
wn.mainloop()
