from PIL import Image 

def green(r, g, b):
    return (r < 128 and g > 128 and b < 128)

def blue(r, g, b):
    return (r < 128 and g < 128 and b > 128)

def red(r, g, b):
    return (r > 128 and g < 128 and b < 128)

def yellow(r, g, b):
    return (r > 128 and g > 128 and b < 128)

