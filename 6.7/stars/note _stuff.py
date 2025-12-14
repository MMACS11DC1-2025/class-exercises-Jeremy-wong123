output =  '''
    name:{} 
    time: {:.2f}
    colour: {}
    colour percentage: {:.2f}
    similarity to sun: {}
    class: {}
    Temp: {}
    {}
    \n
    '''.format(names[a], tend-tstar, stardata[a][0], stardata[a][0], 'n/a', secondstardata[a][0], secondstardata[a][1], secondstardata[a][2])
print(output)
