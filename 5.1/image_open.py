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
        
        
