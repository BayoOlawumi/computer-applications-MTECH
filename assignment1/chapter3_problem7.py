import turtle
win = turtle.Screen()
win.bgcolor('cyan')
win.title("Drunk Pirate Display")

drunk_pirate = turtle.Turtle()
drunk_pirate.pensize(4)
drunk_pirate.color('green')
# A loop to iterate through the angles obtained by the student
for angle in [160,-43,270,-97,-43,200,-940,17,-86]:
    # Checks if the angle is positive, then it goes anti-closewise
    if angle > 0:
        drunk_pirate.left(angle)
    # Checks if the angle is negative, then it goes closewise
    elif angle < 0:
        drunk_pirate.right(angle)
    # Moves a distance of 100 after repositioning the turtle head
    drunk_pirate.forward(100)



win.mainloop()
