import turtle
import random
t = turtle.Turtle()

def snow(x):
  for i in range(x):
    t.forward(10 * x)
    t.right(60)
    if (x>6):
      snow(x/y)
    t.forward(10)
    t.goto(6 * x)

snow(12)