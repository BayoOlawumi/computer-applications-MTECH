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


# Turn tess into a big green circle
tess_green.shape("circle")
tess_green.shapesize(3)


tess_red.shape("circle")
tess_red.shapesize(3)


tess_orange.shape("circle")
tess_orange.shapesize(3)


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
    # Green
    if state_num == 0:      #Transition from state 0 to state 1
        tess_orange.fillcolor("black")
        tess_green.fillcolor("black")
        tess_green.fillcolor("green")
        wn.ontimer(advance_state_machine, 3000)
        state_num = 1

    # Red
    elif state_num ==1:      #Transition from state 1 to state 2
        tess_orange.fillcolor("black")
        tess_green.fillcolor("black")
        tess_red.fillcolor("red")
        wn.ontimer(advance_state_machine, 2000)
        state_num = 2

    # Green and Orange
    elif state_num ==2:      #Transition from state 2 to state 3 (Green + Orange)
        tess_orange.fillcolor("orange")
        tess_green.fillcolor("green")
        tess_red.fillcolor("black")
        wn.ontimer(advance_state_machine, 1000)
        state_num = 3

    # Orange
    else:
        tess_red.fillcolor("black")
        tess_green.fillcolor("black")
        tess_orange.fillcolor("orange")
        wn.ontimer(advance_state_machine, 1000)
        state_num = 0

pen.setpos(120,70)
pen.write("This is praticable!", font=("Calibri", 10))
advance_state_machine()
wn.listen()
wn.mainloop()
