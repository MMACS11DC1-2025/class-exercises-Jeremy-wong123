My program:
I plan to make a program that ooks at pictures of stars and then generates a table of data for each star depending on the colour of the star. I am able to determine this with good knowledge of the stars and the HR diagram(Red stars are colder and blue stars are hottest). Therefore based on finding the colour majority of each star I can determine what type of star it is and then identify it's aproximate temperature and type.


1. 
I will use a nested for loop to iterate over the entire image checking if it's either yellow, red, orange, white or blue recording a total ammount of each pixel in a list called 'all'. I will then nest the nest forloop in a for loop that will run 10 times to iterate over 10 different images

2.
Then, using a helper function, I will use the list for each star and calculate the percent the image is made up of each colour( red, orange, yellow, white, blue) after turning the total pixel list into a list of percentages[20%, 50%, 5%, 2%, 23%] I will then use selection sort to find the highest percentage, recording it's value and index and using it's index to find the colour that the percentage represents. I then return the top colour and how much of it makes up the image. These two values will then allow me to compare it to our sun.

3.
Now, I plan to display all the data and information in a stat-chart like format with string formating to insert different values of strings and numbers into the output. I plan to include the name, time, heat, star type, color & similairity to the sun as well as a fun comment for each star type.

4.
To find stars similar to the sun, I will take the sun's values and record them, then using binary search, linear search and selection sort on the list 'stardata'. First I wil use linear search on the list to find tuples with the value 'red' adn put them into a list. Then using selection sort to sort the list of tuples and from least to greatest, I plan to find stars with most similairty to the sun based on colour and percentage as binary search can be used to find a specific quality but only on sorted lists


A major challenge was trying to get the quality detector to detect the color composition of different stars accurately. This was really difficult as I had to try and figure out why some yellow and blue stars would be considered red or white in my program. I had to keep the colour indicators accurate while also allowing them to have range and detect the desired colours smoothly. I tried to use if statments for all the indicators instead of elif because then all the colors could be harmoniously filled with their values, however yellow pixels would often overlap and check off red and orange indicators skewing the data. To overcome this problem, I organized the elif and if statements, making red and orange indicators elif statements of yellow indicators and making white an elif statement of blue. This would funnel more yellow and blue pixels to their respective variables while keeping other colour variables constant. This works as my red and orange indicators are broader than yellow. Now when my program ran, it would first check ifhte pixel is yellow before moving onto orange and red.

TESTING:

    There are 3 main features of this propgram: Generating the data for each star, finding a star that closely resembles the sun and 