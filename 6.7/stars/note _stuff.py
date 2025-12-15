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



'''

    Used selection sort to determine the startype 
    will use binary search to find stars similar to the sun
'''

'''
-Program errors:
    Notsun- yellow/orange
    vega - blue
    alpha centauri -yellow
    epilison - orange
    Naos - blue
    tao-ceti - yellow
    sirius_a - white
Incorrect output:

    name:notsun 
    time: 4.12
    colour: red
    colour percentage: 57.75
    similarity to sun: n/a
    class: M
    Temp: 2100k-3400k
    About 5-9 times the boiling point of water!

    name:vega 
    time: 3.61
    colour: white
    colour percentage: 79.70
    similarity to sun: n/a
    class: A-B
    Temp: 72000k-30000k
    About one 66th of a Solar Corona!

    name:alpha_centauri_a 
    time: 0.40
    colour: orange
    colour percentage: 52.60
    similarity to sun: n/a
    class: K
    Temp: 3400k-4900k
    Around 2 times the melting point of Iron!

    name:epilison 
    time: 0.29
    colour: red
    colour percentage: 80.20
    similarity to sun: n/a
    class: M
    Temp: 2100k-3400k
    About 5-9 times the boiling point of water!

    name:Naos 
    time: 1.19
    colour: white
    colour percentage: 95.47
    similarity to sun: n/a
    class: A-B
    Temp: 72000k-30000k
    About one 66th of a Solar Corona!

    name:tau_ceti 
    time: 0.79
    colour: white
    colour percentage: 51.17
    similarity to sun: n/a
    class: A-B
    Temp: 72000k-30000k
    About one 66th of a Solar Corona!

    name:sirius_a 
    time: 0.24
    colour: red
    colour percentage: 20.00
    similarity to sun: n/a
    class: M
    Temp: 2100k-3400k
    About 5-9 times the boiling point of water!
'''


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
    '''.format(names[a], tend-tstar, stardata[a][0], stardata[a][1], 'n/a', secondstardata[a][0], secondstardata[a][1], secondstardata[a][2])
    print(output)