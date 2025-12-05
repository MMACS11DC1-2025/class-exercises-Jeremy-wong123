import turtle
t = turtle.Turtle()
def draw_tree(level, branch_length):
    if level > 0:
        t.forward(branch_length)
        t.left(40)
        draw_tree(level-1, branch_length/1.61)

        t.right(80)
        draw_tree(level-1, branch_length/1.61)

        t.left(40)
        t.back(branch_length)

    else:
        t.color('green')
        t.stamp()
        t.color('brown')

t.speed(0)
t.penup()
t.goto(0,-180)
t.left(90)
t.pendown()
t.color('brown')
t.width(3)
t.shape('triangle')
x = int(input('how much level?'))
draw_tree(x, 120)