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
name = []
stardata = []
for a in range(len(stars)):
    yellow = 0
    blue = 0
    red = 0
    orange = 0
    white = 0
    tstar = time.time()    
    file = Image.open(stars[a])
    star = file.load()
    width, height = file.width, file.height
    colouredPixedls = 0
    for i in range(width):
        for j in range(height):
            r = star[i,j][0]
            g = star[i,j][1]
            b = star[i,j][2]
            totalred = 0
            totalgreen = 0
            totalblue = 0
            # if the pixel is not black, add 1 to the colouredPixels
            #add the rgb values into a total variable
            #if its black it zeros 
            if not functions.black(r, g, b):
                totalred += r
                totalgreen += g
                totalblue += b
    starclass = functions.total(totalred, totalgreen, totalblue)
    all = [red, orange, yellow, white, blue]
    stardata.append(functions.startype(all))
    print(str(stardata[a]) + '\n')



    

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