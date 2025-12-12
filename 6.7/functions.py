from PIL import Image 

def blue(r, g, b):
    preferred = 0
    prefergreen = 0
    preferblue = 255
    preferred - 
    return (r < b and g < b and b > 128)

def red(r, g, b):
    preferred = 255
    prefergreen = 0
    preferblue = 0
    return (r > 128 and g < r and b < r)

def yellow(r, g, b):
    preferred = 255
    prefergreen = 255
    preferblue = 0
    return (r > b and g > b and b < 128)

def orange(r, g, b):
    preferred = 255
    prefergreen = 128
    preferblue = 0
    return(r > g and g > 128 and b < g)

def white(r, g, b):
    preferred = 255
    prefergreen = 255
    preferblue = 255
    return(r > 230 and g > 230 and b > 230)

def black(r, g, b):
    return not (r == 0 and g == 0 and b == 0)

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
    startyp = [1, 2, 3, 4, 5]
    mostcolor = []
    topercent = []
    for i in range(len(totallist)):
        highestscore = totallist[i]
        highestindex = i

        for j in range(i+1, len(totallist)):
            if totallist[j] > highestscore and totallist not in topercent:
                highestscore = totallist[j]
                highestindex = j
                topercent.append(totallist[highestindex])
                mostcolor.append(startyp[highestindex])
    return (mostcolor[0], topercent[0])

#use ideal pallete
#compare the color to the pallete generating a percentage 
def total(totalred, totalgreen, totalblue, weight, image):
    r = 0
    o = 0
    y = 0
    w = 0
    b = 0
    if red(totalred, totalgreen, totalblue): 
        
        return 1
    elif orange(totalred, totalgreen, totalblue):
        o += totalred + totalgreen + totalblue
        return 2
    elif yellow(totalred, totalgreen, totalblue):
        return 3 
    elif white(totalred, totalgreen, totalblue):
        return 4
    elif blue(totalred, totalgreen, totalblue):
        return 5
    


        


        