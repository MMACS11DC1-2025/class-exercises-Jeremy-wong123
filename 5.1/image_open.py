from PIL import Image
import image

image_green = Image.open("5.1/kid-green.jpg").load()
image_beach = Image.open("5.1/beach.jpg").load()
image_output = Image.open("5.1/kid-green.jpg")
w = image_output.width
h = image_output.height

for i in range(w):
    for b in range(h):
        r = image_green[i, b][0]
        g = image_green[i, b][1]
        bl = image_green[i, b][2]
            
        if image.is_green(r, g, bl):
            beach_colour = image_beach[i, b]
            xy = (i, b)
            image_output.putpixel(xy, beach_colour) 
image_output.save("output.png", "png")
        
        
'''
for i in range(w):
    for b in range(h):
        r = image_green[i,b][0]
        g = image_green[i,b][1]
        b = image_green[i,b][2]
        if image.is_green(r, g, b):
        beachcolor = image_beach[i, b]
        xy = (i, b)
        image_output.putpixel(xy, beach _colour)
    image_output.save("output.png", "png")




for x in range(width):
    for y in range(height):
        r = jb[x,y][0]
        g = jb[x,y][1]
        b = jb[x,y][2]

        if image.yellow(r, g, b) == 'yellow':
            newpixel = (255, 255, 255)
            xy = (x,y)
            file.putpixel(xy, newpixel)

file.save('output.png', "png")

for x in range(width):
    for y in range(height):
        r = jb[x, y][0]
        g = jb[x, y][1]
        b = jb[x, y][2]
            
        if image.is_light(r, g, b):
            newp = (255, 255, 255)
            xy = (x, y)
        else:
            newp = (0, 0, 0)
            xy = (x, y)
        file.putpixel(xy, newp) 
file.save("output.png", "png")
'''