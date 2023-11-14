## NIELIT Calicut python Training session
## ADVAIT GURUNATH CHAVAN
## Exercise No 15
"""Using numinput() and textinput() 
1. Create a program named exercise15.py 
2. Use the numinput() function to get an x coordinate and a y coordinate.
Store each coordinate in a variable. 
3. Use the textinput() function to ask the user for their name.
Store the name in a variable. 
4. Draw the entered name at the x and y coordinate the user entered."""
import turtle

#Setting up the screen
window = turtle.Screen()
window.title("Turtle Graphics Window Exercise 15 ADVAIT GURUNATH CHAVAN")
window.setup(width=800, height=600)
window.bgpic("grid.gif")

# Function to draw the entered name at the specified coordinates
def draw_name(x, y, name):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.write(name, font=("Arial", 12, "normal"))

def main():
    # Use numinput() to get x and y coordinates
    x_coordinate = turtle.numinput("Input", "Enter x coordinate:")
    y_coordinate = turtle.numinput("Input", "Enter y coordinate:")

    # Use textinput() to get the user's name
    user_name = turtle.textinput("Input", "Enter your name:")

    # Draw the entered name at the specified coordinates
    draw_name(x_coordinate, y_coordinate, user_name)

    # Close the turtle graphics window on click
    turtle.exitonclick()

if __name__ == "__main__":
    main()
