
#list of colour indicators
    #currently blue and yellow don't seem to work very well as stars 
    #that look blue and yellow are called otherwise by the program
def blue(r, g, b):
    return (b > 150 and g < 100 and r < 100)

def red(r, g, b):
    
    return (r > 150 and g < 70 and b < 70)

def yellow(r, g, b):

    return (r > 150 and g > 150 and b < 100)

def orange(r, g, b):

    return(r > 150 and g > 100 and g < r and b < g)

def white(r, g, b):
    return(r > 200 and g == r and b == r)



all = [red, orange, yellow, white, blue]

#selection sort combined with a percentage generator. 
#gives variables to each list and divides it by the 
#total number of coloured pixels creating a percentage for each color 
#Uses selection sort to find the highest color composition in the list
def startype(all):
    r = all[0]
    o = all[1]
    y = all[2]
    w = all[3]
    b = all[4]
    total = r + o + y + b + w
    redperc, orgperc, yelperc, whiperc, bluperc = (r/total * 100), (o/total * 100), (y/total * 100), (w/total * 100), (b/total * 100)
    totallist = [redperc, orgperc, yelperc, whiperc, bluperc]
    startyp = ['red', 'orange', 'yellow', 'white', 'blue']
    for i in range(len(totallist)):
        highestscore = totallist[i]
        highestindex = i

        for j in range(i+1, len(totallist)):
            if totallist[j] > highestscore:
                highestscore = totallist[j]
                highestindex = j
        startyp[highestindex], startyp[i] = startyp[i], startyp[highestindex]
        totallist[highestindex], totallist[i] = totallist[i], totallist[highestindex]
    return startyp[0], totallist[0]

#function to generate additional data based on star-color 
def starclass(x): 
    if x == 'red':
        return 'M', '2100k-3400k', 'About 5-9 times the boiling point of water!'
    elif x == 'orange':
        return 'K', '3400k-4900k', 'Around 2 times the melting point of Iron!'
    elif x == 'yellow': 
        return 'G', '4900k-5700k', "That's about the surface temperature of our sun!"
    elif x == 'white':
        return 'A-B', '72000k-30000k', "About one 66th of a Solar Corona!" 
    elif x == 'blue':
        return 'O', '30000k+', "3000th of a hydrogen bomb!"

'''
testcase = []
x = ['red', 'orange' ,'yellow', 'white' , 'blue']
for i in range(len(x)):
    testcase.append(starclass(x[i]))
    print(testcase[i][2])
'''
def color_search(star_tuple, names, color):
    #finds stars with the user inputed color
    #ex. [('red', 90.0), ('red', 50.0), ('red', 100.0), ('red', 60)]
    color_name = []
    color_stars = []
    for i in range(len(names)):
        if star_tuple[i][0] == color:
            color_stars.append(star_tuple[i])
            color_name.append(names[i])
    return color_stars, color_name

def star_score_sort(star_tuple, names):
    #sorts the color-searched stars/tuples based on percentage from least to highest
    #ex. [('red', 20.0), ('red', 30.0)...]
    for i in range(len(star_tuple)):
        smallest = star_tuple[i][1]
        index = i 
        for x in range(i+1, len(star_tuple)):
            if star_tuple[x][1] < smallest:
                smallest = star_tuple[x][1]
                index = x
        star_tuple[index], star_tuple[i] = star_tuple[i], star_tuple[index]
        names[index], names[i] = names[i], names[index]
    return star_tuple, names


def binary_stars(star_tuple, target_score):
    """
    Searches the color_searched and sorted data for a target_score(percentage).
    
    list format: [('blue', 98.2), ('yellow', 70.1), ...]
    output: 6
    """
    low = 0
    high = len(star_tuple)-1
    posclose = 10.0 #These valeus are the range of difference acceptable by the function
    negclose = -10.0
    while low <= high:
        mid = int((low + high) / 2)
        difference = star_tuple[mid][1] - target_score
        #check if the score is within range
        if negclose < difference and difference < posclose and not star_tuple[mid][1] == target_score:
            return mid
        elif difference > posclose:
            high = mid - 1
        else:
            low = mid + 1 
    return -1
