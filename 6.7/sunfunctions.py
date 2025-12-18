from PIL import Image 

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

#selection sort function
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

def ordering(stardata):
    for i in range(len(stardata)):
        small = stardata[i]
        sma = i

        for b in range(i+1, len(stardata)):
            if stardata[b][1] > small[1]:
                small = stardata[b]
                sma = b
        stardata[sma], stardata[i] = stardata[i], stardata[sma]
    return stardata


def search(all, color):
    newlist = []
    for i in range(len(all)):
        if all[i][0] == color:
            newlist.append(all[i])
    return newlist

def sort(all):
    for i in range(len(all)):
        small = all[i][1]
        sma = i 
        for x in range(i+1, len(all)):
            if all[x][1] < small:
                small = all[x][1]
                sma = x
        all[sma], all[i] = all[i], all[sma]
    return all


def binary_search(newlist, query):
    rank = []
    print(newlist)
    start_index = 0
    end_index = len(newlist)-1

    while start_index <= end_index:
        mid = int((start_index+end_index)/2)
        if newlist[mid][1] == query:
            rank.append(newlist[mid][1])
        elif newlist[mid][1] < query:
            start_index = mid+1
        else: 
            end_index = mid-1
    return rank
"""
outsad = [('red', 57.74934400923267), ('white', 79.69808181863884), ('orange', 52.60246875959962), ('red', 80.20062632551333), ('red', 99.99972740995157), ('white', 95.47169811320755), ('white', 51.171593553055615), ('red', 20.0), ('orange', 65.31544316373126), ('red', 70.82974119361612)]

yes = ordering(outsad)


redlist = search(yes, 'red')
redsort = sort(redlist)
redrank = binary_search(redsort, 80.20062632551333)

print(redlist)
print(redsort)
print(redrank)
"""