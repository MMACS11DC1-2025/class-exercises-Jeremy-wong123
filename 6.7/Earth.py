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


scoreofplanets = []
for i in range(len(name)):
    green_score = abs(earth_green - greenlist[i])
    ocean_score = abs(earth_ocean - oceanlist[i])
    rock_score = abs(earth_rock - rocklist[i])
    planetscore = int((ocean_score + green_score + rock_score)/3)
    scoreofplanets.append(planetscore)

sortedlist = []
for i in range(len(scoreofplanets)):
    closest = scoreofplanets[i]
    index = i
    for j in range(i+1, len(scoreofplanets)):
        if scoreofplanets[j] > closest:
            closest = scoreofplanets[j]
            sortedlist.append(closest)
        

#print('The planet closest to earth is {} with an average difference of {:.0f}'.format())

'''
Questions for Mr.Chin:


### Algorithms and Efficiency (Unit 6)
#### Task 4: Selection Sort
- [ ] Implement the Selection Sort algorithm function yourself 
(not using built-in libraries for sorting) to sort the master list based on the 
calculated Feature Density Score (highest to lowest) (12 pts)

- [ ] Output the top 5 results using list slicing (3 pts)
#### Task 5: Binary Search

- [ ] Implement the Binary Search algorithm function yourself to search the 
sorted list for a specific target score (10 pts)

- [ ] Performance analysis: include a section in your README describing your code 
profiling: give an example of the report and discuss what parts of the program 
take the longest

- [ ] Captured feature involves a real-world use-case. References a real paper, 
report, or dataset supporting decisions for detecting feature (4 points)


'''
