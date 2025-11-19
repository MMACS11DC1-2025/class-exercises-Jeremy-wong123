from PIL import Image
import image

file = Image.open('5.1/jelly_beans (1).jpg')
jb = file.load()
yel = []

width = file.width
height = file.height

for x in range(width):
    for y in range(height):
        r = jb[x,y][0]
        g = jb[x,y][1]
        b = jb[x,y][2]

        if image.colour(r, g, b) == 'yellow':
            new = jb[x, y]
            xy = (x,y)
            file.putpixel(xy, jb)

file.save('output.png', "png")
