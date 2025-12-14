1. 
I will use a nested for loop to iterate over the entire image checking if it's either yellow, red, orange, white or blue recording a total ammount of each pixel in a list called 'all'. I will then nest the nest forloop in a for loop that will run 10 times to iterate over 10 different images

2.
Then, using a helper function, I will use the list for each star and calculate the percent the image is made up of each colour( red, orange, yellow, white, blue) after turning the total pixel list into a list of percentages[20%, 50%, 5%, 2%, 23%] I will then use selection sort to find the highest percentage, recording it's value and index and using it's index to find the colour that the percentage represents. I then return the top colour and how much of it makes up the image. These two values will then allow me to compare it to our sun.

3.
Now, I plan to display all the data and information in a stat-chart like format with string formating to insert different values of strings and numbers into the output. I plan to include the name, time, heat, star type, color & similairity to the sun as well as a fun comment for each star type.

4.
To find stars similaR to the sun, I will take the sun's values and record them, then using binary search & selection sort on the list 'stardata' After using selection sort to sort the list of tuples on the scale(red, orang, yellow, white, blue) and from least to greatest, I plan to find stars with most similairty to the sun based on colour and percentage as binary search can be used to find a specific quality but only on sorted lists

A mjor challenge was trying to get the quality detector to detect the composition of different stars accurately. This was really difficult as I had to try and figure out why some real life yellow stars would appear as red stars in my program as well as ways I could fix it and make it more real-life based. I had to try to keep the colour indicators accurate while also allowing them to have range to be able  to detect the desired colours easier. I also had to try to use if statments instead of elif because I didn't want red indicators to overlap with yellow and orange indicators and vice versa. This problem is still not yet solved.