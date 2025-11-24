

def is_green(r,g,b):
    return r <= 25 and 230 < g <= 255 and 0 <= b < 25

def color(r, g, b):
    if r >= 0 and r < 25 and g > 230 and g <= 255 and b >= 0 and b < 25:
        return 'green'
    else:
        return 'other'
    
def yellow(r, g, b):
    if r > 150 and g > 150 and b < 150:
        return 'yellow'
    else:
        return 'other'
    
def red(r, g, b):
    if r > 230 and g >= 0 and g < 150 and b >= 0 and b < 150:
        return 'red'
    else:
        return 'other'
    
def blue(r, g, b):
    if r >= 0 and r < 150 and g >= 0 and g < 150 and b > 230:
        return 'blue'
    else:
        return 'other'
    
def purple(r, g, b):
    if r > 150 and g < 150 and b > 150:
        return 'purple'
    else:
        return 'other'

def is_light(r, g, b):
    if ((r + g + b)/3) >= 128:
        return True
    else:
        return False