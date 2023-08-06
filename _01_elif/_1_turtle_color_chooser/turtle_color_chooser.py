import random
import turtle
from tkinter import simpledialog


# Returns a random color!
def get_random_color():
    return "#%06X" % (random.randint(0, 0xFFFFFF))

def draw_triangle():
    bigGuy.forward(100)
    bigGuy.left(120)
    bigGuy.forward(100)
    bigGuy.left(120)
    bigGuy.forward(100)

# ====================== DO NOT EDIT THE CODE ABOVE ===========================

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')

    bigGuy = turtle.Turtle()
    bigGuy.shape("circle")

    #bigGuy.pendown()
    bigGuy.width(10)

    message = simpledialog.askstring(title = 'Choosing a color', prompt = "What color pen would you like to draw with?")
    message = message.strip()

    if message.lower() == "red":
        bigGuy.pencolor('red')
    elif message.lower() =="orange":
        bigGuy.pencolor('orange')
    elif message.lower() =="yellow":
        bigGuy.pencolor('yellow')
    elif message.lower() =="green":
        bigGuy.pencolor('green')
    elif message.lower() =="blue":
        bigGuy.pencolor('blue')
    elif message.lower() =="purple":
        bigGuy.pencolor('purple')
    elif message.lower() =="black":
        bigGuy.pencolor('black')
    elif message.lower() =="brown":
        bigGuy.pencolor('brown')
    elif message.lower() =="pink":
        bigGuy.pencolor('pink')
    draw_triangle()


    # TODO 1) Create a new Turtle

    #      2) Make the turtle draw a shape (this will take more than one line
    #         of code)
    #      3) Set the pen width to 10
    #      4) Ask the user what color pen they would like to draw with
    #      5) Use an if/else statement to set the pen color that the user
    #         requested
    #      6) If the user doesn't enter anything, choose a random color
    #      7) Put a loop around your code so that you keep asking the user for
    #         more colors & drawing them

    # ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()