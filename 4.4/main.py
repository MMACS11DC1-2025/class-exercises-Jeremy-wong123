import turtle
import random
t = turtle.Turtle()
b = turtle.Screen()
t.speed(0)
b.bgcolor('black')
totalcall = 0
def tree():
  t.color('green')
  for i in range(3):
    t.forward(50)
    t.left(120)
  t.forward(13)
  t.right(120)
  t.forward(75)
  t.left(120)
  t.forward(100)
  t.left(120)
  t.forward(75)
  t.backward(75)
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
roy = ['red', 'orange', 'yellow']
bwc = ['blue', 'white', 'cyan']
www = ['white', 'white', 'white']
#dictionary to house the color pallete for turtle
naughtylist = {'roy': roy, 'bwc': bwc, 'www': www}
#sees if the user is good or bad
version = input('HO HO HO ! Merry Christmas! Have you been a good boy?(good, bad, ehh)').lower()
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
  return totalcall

for b in range(15):
  t.color(random.choice(pallete))
  #randomizes where the flake will be each iteration
  x = random.choice(range(400))-200
  y = random.choice(range(400))-200
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
print(totalcall)
#AT CLASS
#Ask how I could improve the random coordinates
#ask how I could modify the range to go from negatives
#RECURSION Q
#Ask what returning meaningful values mean
#Ask what prints the total count of recursive calls means
#What resembles good usage of dictionaries(get a 2)

#PLAN 
#to draw a snowing weather 
#maybe draw a tree in the background 
#use a dictionary for snowcolors(white, blue, cyan)

#TIMELINE 
#SUN:
#   Develop the recursion function and basis for program
#   Develop meaningful questions about assignment in class
#MON:
#   Spend half time studying, half time coding(40/40 Min)
#TUE:
#   Spend more time studying, less time coding(40/20min)
#WED:
#   Spend half time studying, half time coding(40/40 Min)
#THU:
#   Spend more time studying, less time coding(40/20min)