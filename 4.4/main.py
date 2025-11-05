import turtle
import random
t = turtle.Turtle()
b = turtle.Screen()
t.speed(0)
b.bgcolor('black')
totalcall = 0
def tree():
  #function to draw a christmas tree
  
  #draws the starting triangle of the tree
  t.color('green')
  for i in range(3):
    t.forward(50)
    t.left(120)
    
  #draws 2nd layer of the tree(trapezoid)
  t.forward(13)
  t.right(120)
  t.forward(75)
  t.left(120)
  t.forward(100)
  t.left(120)
  t.forward(75)
  t.backward(75)
  
  #draws the stem of tree(rectangle)
  t.left(60)
  t.forward(13)
  t.left(120)
  t.forward(88)
  t.right(120)
  t.forward(163)
  t.right(120)
  t.forward(88)
  t.backward(88)
  t.right(60)
  
  #draws the stem of tree(rectangle)
  t.forward(54)
  t.color('brown')
  t.right(90)
  t.forward(100)
  t.left(90)
  t.forward(54)
  t.left(90)
  t.forward(100)
tree()
#list to house the colors for the turtle
ROY = ['red', 'orange', 'yellow']
BWC = ['blue', 'white', 'cyan']
WWW = ['white']
#dictionary to house the color pallete for turtle
naughtylist = {'roy': ROY, 'bwc': BWC, 'www': WWW}
#sees if the user is good or bad
version = input('HO HO HO ! Merry Christmas! Have you been a good boy?(good, bad, ehh)').lower()

#changes the color pallete
if version == 'good':
  pallete = naughtylist['bwc']
elif version == 'ehh':
  pallete = naughtylist['www']
else:
  pallete = naughtylist['roy']
#function to draw a side
def flake(length, depth):
  totalcall = 0
  #base case, draw forward until depth is 0
  if depth == 0:
    t.forward(length)
  else:
    totalcall += 1
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
    
    return depth

for b in range(15):
  t.color(random.choice(pallete))
  #randomizes where the flake will be each iteration
  x = random.choice(range(350))-175
  y = random.choice(range(350))-175
  #randomizes length and depth of each flake
  length = random.choice(range(50))+25
  depth = random.choice(range(2))+2
  #seemlessly move froom coord to coord drawing 
  #different flakes in different places
  t.penup()
  t.goto(x, y)
  t.pendown()
  #to draw an actual flake
  for i in range(3):
    flake(length, depth)
    t.left(120)
    totalcall += depth
  #returns the ammount of times flake function was called
print('Function was called ' + str(totalcall) + ' times')