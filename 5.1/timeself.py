#import time
#t = time.time()
from PIL import Image 
import image

#t1 = time.time()
file = Image.open('5.1/mountain.jpg')
jbimg = file.load()

width = file.width
height = file.height
light = 0
dark = 0
yellow = 0
blue = 0
red = 0
purple = 0 
green = 0
pal = []
best = 0 
for i in range(width):
    for j in range(height):
        r = jbimg[i,j][0]
        g = jbimg[i,j][1]
        b = jbimg[i,j][2]
        if image.yellow(r, g, b):
            yellow += 1
        elif image.blue(r, g, b):
            blue += 1
        elif image.red(r, g, b): 
            red += 1
        elif image.is_green(r, g, b):
            green += 1
        elif image.purple(r, g, b):
            purple += 1
        if image.is_light(r, g, b):
            light += 1
        else:
            dark += 1
pal.append(yellow)    
pal.append(red)
pal.append(green)      
pal.append(blue) 
pal.append(purple)  
for i in range(len(pal)):
    if i > best:
        best = i
if 



