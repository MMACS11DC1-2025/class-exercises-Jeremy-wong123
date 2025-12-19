# from PIL import Image 

#list of colour indicators
    #currently blue and yellow don't seem to work very well as stars 
    #that look blue and yellow are called otherwise by the program
def blue(r, g, b):
    return (b > 150 and g < 100 and b < 100)

def red(r, g, b):
    
    return (r > 150 and g < 100 and b < 100)

def yellow(r, g, b):

    return (r > 128 and g > 128 and b < 90)

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

def sort(outsad):
    for i in range(len(outsad)):
        small = outsad[i][1]
        index = i
        for j in range(i+1, len(outsad)):
            if outsad[j][1] < small:
                small = outsad[j][1]
                index = j
        outsad[index], outsad[i] = outsad[i], outsad[index]
    return outsad

def color_ex(outsad, x):
    star = 0
    end = len(outsad)-1
    while star <= end:
        mid = int((star + end)/2) 
        print(mid)
        if outsad[mid][1] == x:
            return names[mid], mid
        elif outsad[mid][1] < x:
            star = mid + 1
        else:
            star = mid - 1
    return -1
names = ['notsun', 'vega', 'alpha_centauri_a', 'epilison', 'Mr_Chin', 'Naos', 'tau_ceti', 'sirius_a', 'proxima_centauri', 'antares']
outsad = [('red', 57.74934400923267), ('white', 79.69808181863884), ('orange', 52.60246875959962), ('red', 80.20062632551333), ('red', 99.99972740995157), ('white', 95.47169811320755), ('white', 51.171593553055615), ('red', 20.0), ('orange', 65.31544316373126), ('red', 70.82974119361612)]


yes = sort(outsad)
print(yes)
print(color_ex(yes, 57.74934400923267))