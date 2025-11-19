

def is_green(r,g,b):
    return r <- 25 and 230 < g <= 255 and 0 <= b < 25

def color(r, g, b):
    if r >= 0 and r < 25 and g > 230 and g <= 255 and b >= 0 and b < 25:
        return 'green'
    else:
        return 'other'