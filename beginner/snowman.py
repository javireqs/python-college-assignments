# This program uses turtle graphics to create a snowman.
# Inputs: None
# Outputs: Frosty Tha Snowman
# Written by: Javier Hernandez Requena
# Date: Mar 4, 2021
# Class: CS 110A


# Import turtle
import turtle

# Main function
def main():
    turtle.hideturtle()
    drawBase(0, 0, 75)
    drawMidSection(0, 125, 50)
    drawArms(50, 135, 100, 175, 'black')
    drawArms(-50, 135, -100, 155, 'black')
    drawHead(0, 210, 35)
    drawHat(-50, 225, 100, 20, 'black')
    drawHat(-25, 245, 50, 40, 'black')

# drawBase function
def drawBase(x, y, radius):
    turtle.penup()             # Raise the pen
    turtle.goto(x, y - radius) # Position the turtle
    turtle.pendown()           # Lower the pen
    turtle.circle(radius)      # Draw a circle
    turtle.penup()             # Raise the pen

# drawMidSection function
def drawMidSection(x, y, radius):
    turtle.penup()             # Raise the pen
    turtle.goto(x, y - radius) # Position the turtle
    turtle.pendown()           # Lower the pen
    turtle.circle(radius)      # Draw a circle
    turtle.penup()             # Raise the pen

# drawArms function
def drawArms(startX, startY, endX, endY, color):
    turtle.penup()              # Raise the pen
    turtle.goto(startX, startY) # Move to starting point
    turtle.pendown()            # Lower the pen
    turtle.pencolor(color)      # Set color
    turtle.goto(endX, endY)     # Draw line
    turtle.penup()              # Raise the pen

# drawHead function
def drawHead(x, y, radius):
    turtle.penup()              # Raise the pen
    turtle.goto(x, y - radius)  # Position the turtle
    turtle.pendown()            # Lower the pen
    turtle.circle(radius)           # Draw a circle
    turtle.penup()                  # Raise the pen
    drawEyes(10, 215, 5)            # Draw eye
    drawEyes(-10, 215, 5)           # Draw eye
    drawMouth(-20, 200, 20, 205)    # Draw mouth

# drawEyes function
def drawEyes(x, y, radius):
    turtle.penup()              # Raise the pen
    turtle.goto(x,y - radius)   # Position the turtle
    turtle.pendown()            # Lower the pen
    turtle.circle(radius)       # Draw circle
    turtle.penup()              # Raise the pen

# drawMouth function
def drawMouth(startX, startY, endX, endY):
    turtle.penup()                  # Raise the pen
    turtle.goto(startX, startY)     # Position the turtle
    turtle.pendown()                # Lower the pen
    turtle.goto(endX, endY)         # Draw line
    turtle.penup()                  # Raise the pen

# drawHat function    
def drawHat(x, y, width, length, color):
    turtle.penup()                  # Raise the pen
    turtle.goto(x, y)               # Position the turtle
    turtle.fillcolor(color)         # Grab color
    turtle.pendown()                # Lower the pen
    turtle.begin_fill()             # Starts to draw rectangle
    for count in range(2):          # For loop to draw L shape twice
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(length)
        turtle.left(90)
    turtle.end_fill()               # Ends the rectangle
    
# Main function
main()                              # Call main function
