
import time
t0 = time.time()
print('Beginning program... \n \n')
from PIL import Image
import sunfunctions
t1 = time.time()


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
            if sunfunctions.yellow(r, g, b): 
                yellow += 1
            if sunfunctions.red(r, g, b):
                red += 1
            if sunfunctions.orange(r, g, b):
                orange += 1
            if sunfunctions.blue(r, g, b):
                blue += 1
            if sunfunctions.white(r, g, b):
                white += 1
    all = [red, orange, yellow, white, blue]

    startype = sunfunctions.startype(all)
    stardata.append(startype)
    secondstardata.append(sunfunctions.starclass(startype[0]))
    tend = time.time()
    output =  '''
    name:{} 
    time: {:.3f}s
    colour: {}
    colour percentage: {:.3f}%
    star type:{}
    Temp: {}
    {}
    \n
    '''.format(names[a], tend-tstar, stardata[a][0], stardata[a][1], secondstardata[a][0], secondstardata[a][1], secondstardata[a][2])
    print(output)
