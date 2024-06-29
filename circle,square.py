from turtle import *

# Constants
a = 100  # Length of the side of square
b = 90   # Angle for turning in square (90 degrees)

# Create a turtle object
t = Turtle()
t.speed(0)  # Set the turtle's speed (0 is the fastest)

# Draw a square
def square():
    for _ in range(4):
        t.forward(a)
        t.right(b)

# Draw a circle
def circle():
    for _ in range(360):
        t.forward(5)
        t.right(3.14)

# Function to ask user for input
def ask():
    while True:
        ans = input("Do you want to draw a square or circle? ").lower()
        if ans == "square":
            return 1
        elif ans == "circle":
            return 2
        else:
            print("Error: Please enter 'square' or 'circle'.")

# Main loop to draw shapes based on user input
while True:
    shape = ask()
    t.clear()  # Clear the previous drawings

    if shape == 1:
        for _ in range(10):
            square()
    elif shape == 2:
        for _ in range(10):
            circle()
    
    t.hideturtle()  # Hide the turtle after drawing

done()  # Keeps the window open until manually closed
