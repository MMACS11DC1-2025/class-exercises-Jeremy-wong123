from PIL import Image 

def green(r, g, b):
    return (r < g and g > 128 and b < g)

def blue(r, g, b):
    return (r < b and g < b and b > 128)

def red(r, g, b):
    return (r > 128 and g < r and b < r)

def yellow(r, g, b):
    return (r > b and g > b and b < 128)

def purple(r, g, b):
    return (r > g and g < 128 and b > g)

all = [green, purple, red, blue, yellow]
def water(all):
    r = all[2]
    g = all[0]
    p = all[1]
    b = all[3]
    y = all[4]
    total = r + g + b + y + p
    return b/total

def greenery(all):
    r = all[2]
    g = all[0]
    p = all[1]
    b = all[3]
    y = all[4]
    total = r + g + b + y + p
    return g/total 

def rocks(all):
    r = all[2]
    g = all[0]
    p = all[1]
    b = all[3]
    y = all[4]
    total = r + g + b + y + p
    return (y+r)/total 



        