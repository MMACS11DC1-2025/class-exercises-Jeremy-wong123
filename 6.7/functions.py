from PIL import Image 

def blue(r, g, b):
    return (r < b and g < b and b > 128)

def red(r, g, b):
    return (r > 128 and g < r and b < r)

def yellow(r, g, b):
    return (r > b and g > b and b < 128)

def orange(r, g, b):
    return(r > g and g > 128 and b < g)

def white(r, g, b):
    return(r > 230 and g > 230 and b > 230)

all = [red, orange, yellow, blue, white]

def startype(all):
    r = all[0]
    o = all[1]
    y = all[2]
    b = all[3]
    w = all[4]
    total = r + o + y + b + w
    redperc, orgperc, yelperc, bluperc, whiperc = (r/total * 100), (o/total * 100), (y/total * 100), (b/total * 100), (w/total * 100)
    totallist = [redperc, orgperc, yelperc, bluperc, whiperc]
    sortedlist = []
    for i in range(len(totallist)):
        highestscore = totallist[i]
        highestindex = i

        for j in range(i+1, len(totallist)):
            if totallist[j] > highestscore and totallist not in sortedlist:
                highestscore = totallist[j]
                highestindex = j
                sortedlist.append(totallist[highestindex])
    return sortedlist[0]

        


        