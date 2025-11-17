from PIL import Image

image_green = Image.open("5.1/kid-green.jpg").load()
image_beach = Image.open("5.1/beach.jpg").load()

w = image_beach.width
h = image_beach.height

def is_green(r, g, b):
    if r >= 0 and r < 25 and g > 230 and g <= 255 and b >= 0 and b < 25:
        return True
    else:
        return False
print(image_green[0,0])

def color(r, g, b):
    hal = []
    for i in range(3):
        col = int(r)
        hal.append(col)
    return hal

pixel = image_green[0, 0]
r = pixel[0]
g = image_green[0,0][1]
b = image_green[0,0][2]

#print(is_green(r, g, b))
#print(color(r, g, b))

def bw(w, h):
    for i in range(w):
        for b in range(h):
            r = image_beach[i, b][0]
            g = image_beach[i, b][1]
            bl = image_beach[i, b][2]
            if r >= 128:
                r = 255
            else: 
                r = 0
            if g >= 128:
                g = 255
            else:
                g = 0
            if b >= 128:
                b = 255
            else: 
                b = 0
            image_output.putpixel()
        
        
