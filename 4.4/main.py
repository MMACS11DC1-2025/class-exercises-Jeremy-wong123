import turtle
import random
t = turtle.Turtle()
b = turtle.Screen()
t.speed(0)
b.bgcolor('black')
totalcall = 0
#>-----------------------------------------------<

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
bad = ['red', 'orange', 'yellow']
good = ['blue', 'white', 'cyan']
ehh = ['white']

#dictionary to house the color pallete for turtle
naughtylist = {'red_orange_yellow': bad, 'blue_cyan_white': good, 'white': ehh}
#sees if the user is good, ehh or bad
version = input('HO HO HO ! Merry Christmas! Have you been a good boy?(good, bad, ehh)').lower()
#>-----------------------------------------------<


#changes the color pallete based on user input
if version == 'good':
  pallete = naughtylist['blue_cyan_white']
elif version == 'ehh':
  pallete = naughtylist['white']
else:
  pallete = naughtylist['red_orange_yellow']
#>-----------------------------------------------<


#function to draw a side of a snowflake
def flake(length, depth):
  call = 1
  #base case, draw forward until depth is 0
  
  if depth == 0:
    t.forward(length)
    # variable to house the total number of times the flake is called
    return call
  
  else:
  #recursion, draw forward again or turn right 
  #& draw forward & turn left & turn right
  #until depth is 0
    call += flake(length/3, depth-1)
    t.right(60)
    call += flake(length/3, depth-1)
    t.left(120)
    call += flake(length/3, depth-1)
    t.right(60)
    call += flake(length/3, depth-1)
    return call
#>-----------------------------------------------<


#this wiill draw 15 snowflakes randomly with random colors from a 
#color pallete
for b in range(15):
  #sets the turtle pen to a random color in pallete
  t.color(random.choice(pallete))
  
  #randomizes where the flake will be, each iteration
  x = random.choice(range(350))-175
  y = random.choice(range(350))-175
  
  #randomizes length and depth of each flake
  #creating flakes with different sizes and ammount of recursion
  length = random.choice(range(50))+25
  depth = random.choice(range(2))+2
  
  #move from coord to coord drawing 
  #different flakes in different places
  t.penup()
  t.goto(x, y)
  t.pendown()
  
  #to draw an actual snowflake, flake function need to be called
  #3 times with turtle turning 120 after each iteration
  for i in range(3):
    totalcall += flake(length, depth)
    t.left(120)

#returns the ammount of times flake function was called
print(totalcall)


'''
import turtle
import random
t = turtle.Turtle()
b = turtle.Screen()
t.speed(0)
b.bgcolor('black')
totalcall = 0
#>-----------------------------------------------<

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
bad = ['red', 'orange', 'yellow']
good = ['blue', 'white', 'cyan']
ehh = ['white']

#dictionary to house the color pallete for turtle
naughtylist = {'red_orange_yellow': bad, 'blue_cyan_white': good, 'white': ehh}
#sees if the user is good, ehh or bad
version = input('HO HO HO ! Merry Christmas! Have you been a good boy?(good, bad, ehh)').lower()
num = input('How many snowflakes do you want? ')
#>-----------------------------------------------<


#changes the color pallete based on user input
if version == 'good':
  pallete = naughtylist['blue_cyan_white']
elif version == 'ehh':
  pallete = naughtylist['white']
else:
  pallete = naughtylist['red_orange_yellow']
#>-----------------------------------------------<


#function to draw a side of a snowflake
def flake(length, depth):
  call = 1
  #base case, draw forward until depth is 0
  
  if depth == 0:
    t.forward(length)
    # variable to house the total number of times the flake is called
    return call
  
  else:
  #recursion, draw forward again or turn right 
  #& draw forward & turn left & turn right
  #until depth is 0
    call += flake(length/3, depth-1)
    t.right(60)
    call += flake(length/3, depth-1)
    t.left(120)
    call += flake(length/3, depth-1)
    t.right(60)
    call += flake(length/3, depth-1)
    return call
#>-----------------------------------------------<


#this wiill draw 15 snowflakes randomly with random colors from a 
#color pallete
for b in range(num):
  #sets the turtle pen to a random color in pallete
  t.color(random.choice(pallete))
  
  #randomizes where the flake will be, each iteration
  x = random.choice(range(350))-175
  y = random.choice(range(350))-175
  
  #randomizes length and depth of each flake
  #creating flakes with different sizes and ammount of recursion
  length = random.choice(range(50))+25
  depth = random.choice(range(2))+2
  
  #move from coord to coord drawing 
  #different flakes in different places
  t.penup()
  t.goto(x, y)
  t.pendown()
  
  #to draw an actual snowflake, flake function need to be called
  #3 times with turtle turning 120 after each iteration
  for i in range(3):
    totalcall += flake(length, depth)
    t.left(120)

#returns the ammount of times flake function was called
print(totalcall)
'''