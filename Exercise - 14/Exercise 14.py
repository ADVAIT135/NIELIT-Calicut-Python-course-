## NIELIT Calicut python Training session
## ADVAIT GURUNATH CHAVAN
## Exercise No 14
"""Exercise 14 Draw a Red Square -> Create a program that uses turtle graphics to create an 800x600 pixel window. Create a new turtle variable. 
Then use your new turtle variable to draw a red square with coordinates matching the one below using the turtle’s penup(), pendown(),
forward(), left(), and right() functions."""

import turtle
# Set up the window
window = turtle.Screen()
window.title("Turtle Graphics Window Exercise 14 ADVAIT GURUNATH CHAVAN")
window.setup(width=800, height=600)
window.bgpic("grid.gif")

# Create a turtle object
my_turtle = turtle.Turtle()

# Move to the starting position
my_turtle.penup()
my_turtle.goto(130, -90)
my_turtle.pendown()

# Set the pen color to red
my_turtle.pencolor("red")

# Draw a red square
for _ in range(4):
    my_turtle.forward(100)
    my_turtle.left(-90)

# Close the window when clicked
window.exitonclick()
