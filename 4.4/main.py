import turtle
import random
t = turtle.Turtle()
xcoor = random.choice(range(200))
ycoor = random.choice(range(200))
def snow(x, y):
  xcoor = 0
  ycoor = 0
  if y > 0:
    for i in range(200):
      t.goto(xcoor, ycoor)
      for i in range(6):
        xcoor = random.choice(range(200))
        ycoor = random.choice(range(200))
        t.forward(y)
        t.right(60)
        t.color('blue')
        t.stamp()
        t.penup()
    snow(x/0.5, y/0.5)
  else:
    t.color('blue')
    t.stamp()

snow(6, 0.1)