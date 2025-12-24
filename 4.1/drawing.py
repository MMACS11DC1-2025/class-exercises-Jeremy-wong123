"""
Make An Interactive Drawing or Animation 
Explore the turtle drawing package to create an interactive drawing.
It should use a while loop.
Your program should also include at least one function you’ve made yourself 
"""
import turtle
t = turtle.Turtle()
user = int(input('How big do you want you spiral?'))
def spiral(x):
	for i in range(50):
    	t.forward(i * 2)
    	t.right(360/x)
spiral(user)
