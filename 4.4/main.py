import turtle
import random

t = turtle.Turtle()
b = turtle.Screen()
t.color('blue')
t.speed(0)
b.bgcolor('black')
#function to draw a side
def flake(length, depth):
  #base case, draw forward until depth is 0
  if depth == 0:
    t.forward(length)
  else:
    #recursion, draw forward again or turn right 
    #& draw forward & turn left & turn right
    #until depth is 0
    flake(length/3, depth-1)
    t.right(60)
    flake(length/3, depth-1)
    t.left(120)
    flake(length/3, depth-1)
    t.right(60)
    flake(length/3, depth-1)

for b in range(50):
  #randomizes where the flake will be each iteration
  x = random.choice(range(100))
  y = random.choice(range(100))
  #randomizes length and depth of each flake
  length = random.choice(range(50))
  depth = random.choice(range(5))
  #seemlessly move froom coord to coord drawing 
  #different flakes in different places
  t.penup()
  t.goto(x, y)
  t.pendown()
  #to draw an actual flake
  for i in range(6):
    flake(length, depth)
    t.right(60)
#AT CLASS
#Ask how I could improve the random coordinates
#ask how I could modify the range to go from negatives

#PLAN 
#to draw a snowing weather 
#maybe draw a tree in the background 
#use a dictionary for snowcolors(white, blue, cyan)
