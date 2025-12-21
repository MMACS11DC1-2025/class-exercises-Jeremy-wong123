# from PIL import Image 

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
    

test = [5970, 0, 0, 76427, 501611]
#temporate testcase for the startype function

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

#Heat range of staars
#red: 2000-3500k, M
#orange: 3900-5300k K
#yellow: 5000-6500k G
#white: 10,000k-25,000k A 
#blue: 25,000k- 50,000k O

'''
testcase = []
x = ['red', 'orange' ,'yellow', 'white' , 'blue']
for i in range(len(x)):
    testcase.append(starclass(x[i]))
    print(testcase[i][2])
'''
def color_search(star_tuple, names, color):
    color_name = []
    color_stars = []
    for i in range(len(names)):
        if star_tuple[i][0] == color:
            color_stars.append(star_tuple[i])
            color_name.append(names[i])
    return color_stars, color_name

def star_score_sort(star_tuple, names):
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
    Searches the sorted stardata for a target_score.
    data format: [('blue', 98.2), ('yellow', 70.1), ...]
    """
    low = 0
    high = len(star_tuple)-1
    posclose = 10.0  # This defines the "closeness." 0.5% difference counts as a match.
    negclose = -10.0
    while low <= high:
        mid = int((low + high) / 2)
        difference = star_tuple[mid][1] - target_score
        # Check if the score is within the range
        if negclose < difference and difference < posclose and not star_tuple[mid][1] == target_score:
            return mid
        # Since your list is sorted Highest to Lowest (Descending):
        elif difference > posclose:
            high = mid - 1  # Target is larger, move toward the front
        else:
            low = mid + 1   # Target is smaller, move toward the back
    return -1

'''
[('red', 20.0), 
('white', 51.171593553055615), 
('orange', 52.60246875959962), 
('red', 57.74934400923267), 
('orange', 65.31544316373126), 
('red', 70.82974119361612), 
('white', 79.69808181863884), 
('red', 80.20062632551333), 
('white', 95.47169811320755), 
('red', 99.99972740995157)]
'''
'''
starda = [('red', 57.74934400923267), ('white', 79.69808181863884), ('orange', 52.60246875959962), ('red', 80.20062632551333), ('red', 99.99972740995157), ('white', 95.47169811320755), ('white', 51.171593553055615), ('red', 20.0), ('orange', 65.31544316373126), ('red', 70.82974119361612)]
names = ['notsun', 'vega', 'alpha_centauri_a', 'epilison', 'Mr_Chin', 'Naos', 'tau_ceti', 'sirius_a', 'proxima_centauri', 'antares']

search = color_search(starda, names, 'red')[0]
searched_names = color_search(starda, names, 'red')[1]
sorted = star_score_sort(search, searched_names)[0]
sorted_names = star_score_sort(search, searched_names)[1]
data = binary_stars(sorted, 100.0)

print(search)
print(searched_names)
print('\n')

if data == -1:
    print('no similar stars')
else:
    print(sorted_names[data])
'''