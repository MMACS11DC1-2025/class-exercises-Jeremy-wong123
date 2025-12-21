My program:
I plan to make a program that ooks at pictures of stars and then generates a table of data for each star depending on the colour of the star. I am able to determine this with good knowledge of the stars and the HR diagram(Red stars are colder and blue stars are hottest). Therefore based on finding the colour majority of each star I can determine what type of star it is and then identify it's aproximate temperature and type. It will display the generated data and ask the user about the color and color percentage of the star they want to find and then outputing the name of the star that fits the user's description accordingly.


1.MAIN LOOP (overall skeleton of the program)
I will use a nested for loop to iterate over the entire image checking if it's either yellow, red, orange, white or blue recording a total ammount of each pixel in a list called 'all'. I will then nest the nest forloop in a for loop that will run 10 times to iterate over 10 different images

2.FUNCTIONS (Muscle/organs)
Then, using a helper function, I will use the list for each star and calculate the percent the image is made up of each colour( red, orange, yellow, white, blue) after turning the total pixel list into a list of percentages[20%, 50%, 5%, 2%, 23%] I will then use selection sort to find the highest percentage, recording it's value and index and using it's index to find the colour that the percentage represents. I then return the top colour and how much of it makes up the image. These two values will then allow me to compare it to our sun.

3.OUTPUT
Now, I plan to display all the data and information in a stat-chart like format with string formating to insert different values of strings and numbers into the output. I plan to include the name, time, heat, star type, color & similairity to the sun as well as a fun comment for each star type.

4.
This program will aslo focus on finding a star that matches the the user input of color and color percentage. To do this, the program will use 3 main functions: a linear search function to find tuples/stars of the specific color, a selection sort funciton to sort tuples/stars from lowest percent to highest percent and a binary search function to find the star that best matches the user description.

5.CHALLENGES
A major challenge was trying to get the quality detector to detect the color composition of different stars accurately. This was really difficult as I had to try and figure out why some yellow and blue stars would be considered red or white in my program. I had to keep the colour indicators accurate while also allowing them to have range and detect the desired colours smoothly. I tried to use if statments for all the indicators instead of elif because then all the colors could be harmoniously filled with their values, however yellow pixels would often overlap and check off red and orange indicators skewing the data. To overcome this problem, I organized the elif and if statements, making red and orange indicators elif statements of yellow indicators and making white an elif statement of blue. This would funnel more yellow and blue pixels to their respective variables while keeping other colour variables constant. This works as my red and orange indicators are broader than yellow. Now when my program ran, it would first check ifhte pixel is yellow before moving onto orange and red.

6.TESTING:

    There are 2 main features of this propgram: Generating the data for each star, finding a star that closely resembles the user dscription.

    To test the program, I woulkd run it and it should output the star's data with this format for each of the 10 stars:

        name:tau_ceti 
        time: 0.789s
        colour: white
        colour percentage: 51.260%
        star type:A-B
        Temp: 72000k-30000k
        About one 66th of a Solar Corona!

    After the data is printed out, the program will then ask the user for the color of the star they want to find and the color percentage, the program's output should look something like this:


        What type of star would you like to find?(red, orange, yellow, white, blue)white
        What color percentage is your star?90.0
        >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


        The star that matches your description is sirius_a, it took 0.000 to find.


7.PERFORMANCE ANALYSIS:
    Often the time to process all 10 images would take the longest with the time taken to find the user-desired star to be the least as we see in this example output:

        >>TIME REPORT<<
        time taken to import modules: 0.040
        time taken to process stars: 10.759
        time taken to find desired star: 0.000

    As aditional data, the program also outputs the ammount of time taken to process each individaul star:

        name:Naos 
        time: 1.192s
        colour: blue
        colour percentage: 99.546%
        star type:O
        Temp: 30000k+
        3000th of a hydrogen bomb!


