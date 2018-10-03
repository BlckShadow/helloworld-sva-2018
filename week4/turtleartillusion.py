import turtle
import random

win_turtles = turtle.Turtle()

colors =['red', 'purple', 'blue', 'green', 'orange', 'yellow', 'indigo', 'violet', 'lime', 'aqua']

def drawing_square(win_turtles):
    for i in range(1,5):
        win_turtles.forward(200)
        win_turtles.right(90)
        win_turtles.right(180)


def drawing_ArtScreen():
    win = turtle.Screen()
    win.bgcolor("black")

    pattern = turtle.Turtle()
    pattern.shape("turtle")

    pattern.speed(5)
    pattern.pensize(1)


for i in range(1,10000):
    drawing_square(pattern)
    pattern.right(10)
    pattern.color(colors[i%10])
    win.exitonclick()

drawing_ArtScreen()