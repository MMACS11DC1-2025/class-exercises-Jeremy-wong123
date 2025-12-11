'''
PROJECT IDEAS

1. A program that analyzes a set of planets
    - Analyzes and compares it to Earth
    - Judges based on color(blue = ocean, white= clouds, green/red/yellow = land)
    - Uses a breef description of the planet
        (if the planet is classified as a gas giant land identification is exempt)
    -outputs a ranking of the 10 planets including a score out of 5
'''
import time
t0 = time.time()
from PIL import Image
import functions
t1 = time.time()

earth_green = 8
earth_ocean = 29
earth_rock = 61
#Earth's values

greenlist = []
oceanlist = []
rocklist = []
#list of planet values

tstart = time.time()
planets = ['6.7/planets/Kepler-22b.jpeg', '6.7/planets/titan.jpg', '6.7/planets/uranus.webp', '6.7/planets/venus.jpg', '6.7/planets/jupiter.png', '6.7/planets/saturn.jpg', '6.7/planets/sun.jpg', '6.7/planets/mars.jpg', '6.7/planets/magma.jpg', '6.7/planets/notearth.jpg']
name = ['kepler-22b', 'titan', 'uranus', 'venus', 'jupiter', 'saturn', 'sun', 'mars', 'magma', 'notearth']
for a in range(len(planets)):
    yellow = 0
    green = 0
    blue = 0
    red = 0
    purple = 0
    tplanet = time.time()    
    file = Image.open(planets[a])
    planet = file.load()
    width, height = file.width, file.height
    for i in range(width):
        for j in range(height):
            r = planet[i,j][0]
            g = planet[i,j][1]
            b = planet[i,j][2]
            if functions.yellow(r, g, b):
                yellow += 1
            elif functions.blue(r, g, b):
                blue += 1
            elif functions.red(r, g, b): 
                red += 1
            elif functions.purple(r, g, b):
                purple += 1
            elif functions.green(r, g, b):
                green += 1
    all = [green, purple, red, blue, yellow]
    greenery = functions.greenery(all) * 100 
    ocean = functions.water(all) * 100
    rocks = functions.rocks(all) * 100
    tdone = time.time()
    greenlist.append(greenery)
    oceanlist.append(ocean)
    rocklist.append(rocks)

bestgreen = []
bestocean = []
bestrock = []
rankofplanets = []
for j in range(len(name)):
    planetid = j
    for i in range(len(name)):
        green_score = abs(earth_green - greenlist[i])
        ocean_score = abs(earth_ocean - oceanlist[i])
        rock_score = abs(earth_rock - rocklist[i])
        bestgreen.append(green_score)
        bestocean.append(ocean_score)
        bestrock.append(rock_score)


    for i in range(len(name)):
        smallgreen = bestgreen[i]
        smallocean = bestocean[i]
        smallrocks = bestrock[i]
        smallindex = i

        for b in range(i+1, len(name)):
            if bestgreen[b] < smallgreen:
                smallgreen = bestgreen[b]
            


twhole = time.time()
    #print('{} has {:.0f}% greenery'.format(name[a], greenery) + '\t' + '{:.0f}% Ocean'.format(ocean) + '\t' + '{:.0f}% rocks'.format(rocks))
    #print('{} took {:.3f} seconds to process \n'.format(name[a], tdone-tplanet))




