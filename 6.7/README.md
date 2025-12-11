Project theme:      Planets

Purpose:
    My program observes the images of different planets and will identify wether it's mostly made up of ocean, rock or greenery in an attempt to find a planet that resembles earth. To do this, the program will search through the each image and identify blue pixels(Ocean), green pixels(greenery) and yellow/red pixels(rock). 
        (These are the conditions for 'Oean', 'greenery' & 'rock')
            Ocean - if the blue pigment in the rgb pixel is higher than the green and red pigment

            Greenery - if the green pigment in the rgb pixel is higher than the blue and red pigment

            rock - if the red pigment in the rgb pixel is higher than the blue and green pigment OR if the red and green pigment(yellow) is higher than the blue pigment



Challenges:
        I had difficulties figuring out how to rank the score of the planets on 3 different qualities because different planets had different percentages of ocean, rock and greenery & it was difficult to compare all those qualities to earth and produce a standardized score. To overcome this I decided to use an average of differences to generate a standarized score for the 3 qualities of the planet. I had to do some mind mapping to come up with this strategy.


