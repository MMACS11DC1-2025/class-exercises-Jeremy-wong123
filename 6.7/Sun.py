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
print('Beginning program... \n \n')
from PIL import Image
import functions
t1 = time.time()


#sun's values
#99.89% yellow


#list of planet values

print('Processing images... \n \n')
tstart = time.time()
stars = ['6.7/stars/notsun.webp', '6.7/stars/vega.jpg', '6.7/stars/alpha_centauri_a.jpg', '6.7/stars/epilison.jpg', '6.7/stars/Mr_Chin.jpg', '6.7/stars/Naos.png', '6.7/stars/tau_ceti.webp', '6.7/stars/sirius_a.jpg', '6.7/stars/proxima_centauri.jpg', '6.7/stars/antares.avif']
names = ['notsun', 'vega', 'alpha_centauri_a', 'epilison', 'Mr_Chin', 'Naos', 'tau_ceti', 'sirius_a', 'proxima_centauri', 'antares']
stardata = []
secondstardata = []
for a in range(len(stars)):
    yellow = 0.01
    blue = 0.01
    red = 0.01
    orange = 0.01
    white = 0.01
    tstar = time.time()    
    file = Image.open(stars[a])
    star = file.load()
    width, height = file.width, file.height
    for i in range(width):
        for j in range(height):
            r = star[i,j][0]
            g = star[i,j][1]
            b = star[i,j][2]
            if functions.yellow(r, g, b): 
                yellow += 1
            if functions.red(r, g, b):
                red += 1
            if functions.orange(r, g, b):
                orange += 1
            if functions.blue(r, g, b):
                blue += 1
            if functions.white(r, g, b):
                white += 1
            
    all = [red, orange, yellow, white, blue]

    startype = functions.startype(all)
    stardata.append(startype)
    secondstardata.append(functions.starclass(startype[0]))
    output =  '''
    name:{} 
    colour:{}
    colour percentage: {:2.f}
    class: {}
    similarity to sun: {}
    Temp: {}
    {}
    \n
    '''.format(names[a], stardata[a], stardata[a+1], secondstardata[a][0], secondstardata[a][1], secondstardata[a][2])
print(output)

#Heat range of staars
#red: 2000-3500k, M
#orange: 3900-5300k K
#yellow: 5000-6500k G
#white: 10,000k-25,000k A 
#blue: 25,000k- 50,000k O

    

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
#Future Idea: A star detector
    #Describes the start determining it's age & star type including it's similarity to our sun
    #Based off of colour