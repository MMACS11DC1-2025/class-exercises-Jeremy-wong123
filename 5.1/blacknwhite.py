from PIL import Image
import image

file = Image.open('5.1/jelly_beans (1).jpg')
jb = file.load()

width = file.width
height = file.height

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