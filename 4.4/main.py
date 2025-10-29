import turtle
import random
t = turtle.Turtle()

def snow(x, ):
  if x > 0:
    for i in range(6):
      t.penup()
    	t.forward(x)
    	t.right(60)
      t.color('blue')
    	t.stamp()
      forward
    	snow(x - 1)
  else:
    t.color('blue')
    t.stamp()

snow(6)