'''
PROJECT IDEAS

1. A program that analyzes a set of planets
    - Analyzes and compares it to Earth
    - Judges based on color(blue = ocean, white= clouds, green/red/yellow = land)
    - Uses a breef description of the planet
        (if the planet is classified as a gas giant land identification is exempt)
    -outputs a ranking of the 10 planets including a score out of 5
'''
import time
t0 = time.time()
from PIL import Image
import functions

file = Image.open('6.7/earth.jpg')
planet = file.load()
width = file.width
height = file.height
yellow = 0
green = 0
blue = 0
red = 0
purple = 0
for i in range(width):
    for j in range(height):
        r = planet[i,j][0]
        g = planet[i,j][1]
        b = planet[i,j][2]
        if functions.yellow(r, g, b):
            yellow += 1
        elif functions.blue(r, g, b):
            blue += 1
        elif functions.red(r, g, b): 
            red += 1
        elif functions.purple(r, g, b):
            purple += 1
        elif functions.green(r, g, b):
            green += 1
t1 = time.time()
all = [green, purple, red, blue, yellow]
print(functions.greenery(all))





