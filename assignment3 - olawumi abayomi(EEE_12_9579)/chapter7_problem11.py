import turtle
win = turtle.Screen()
win.bgcolor('cyan')
win.title("Drunk Pirate Display")

drunk_pirate = turtle.Turtle()
drunk_pirate.pensize(1)
drunk_pirate.color('green')
# A loop to iterate through the angles obtained by the student
for angle, distance in [(160,20),(-43,10),(270,8),(-43,12)]:
    # Checks if the angle is positive, then it goes anti-closewise
    if angle > 0:
        drunk_pirate.left(angle)
    # Checks if the angle is negative, then it goes closewise
    elif angle < 0:
        drunk_pirate.right(angle)
    # Moves a distance  after repositioning the turtle head
    drunk_pirate.forward(distance)



win.mainloop()
