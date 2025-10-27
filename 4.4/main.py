import turtle
import random
t = turtle.Turtle()

def web(x):
    t.penup()
    t.forward(10 * x)
    t.left(360/6)
    t.pendown()
    t.forward()

web(3)