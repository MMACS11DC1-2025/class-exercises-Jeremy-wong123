from PIL import Image
import image

image_green = Image.open("5.1/kid-green.jpg").load()
image_beach = Image.open("5.1/beach.jpg").load()

w = image_beach.width
h = image_beach.height
image_output = Image.open("kid-green.jpg")
def bw(w, h):
    for i in range(w):
        for b in range(h):
            r = image_green[i, b][0]
            g = image_green[i, b][1]
            bl = image_green[i, b][2]
            
            if image.is_green(r,g,bl):
                beach_colour = image_beach[i, b]
                image_output.putpixel((i,b), beach_colour) 
    image_output.save("output.png", "png")
        
        
