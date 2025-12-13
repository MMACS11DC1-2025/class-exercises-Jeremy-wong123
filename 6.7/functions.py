from PIL import Image 

def blue(r, g, b):
    return (b > 150 and b > r + 50 and b > g + 50)

def red(r, g, b):
    return (r > 150 and r > g + 50 and r > b + 50)

def yellow(r, g, b):
    return (r > 150 and g > 150 and b < 100)

def orange(r, g, b):
    return(r > 150 and g > 100 and g < r and b < g)

def white(r, g, b):
    return(r > 200 and g > 200 and b > 200)



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
