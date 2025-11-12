Idea>>>
    I wanted to create something holiday themed I, learned to make the famous koch snowflake and wanted to make a program that would draw it in random places to create a 'snowing' effect


Approach>>>
    inputs>>>>
        This program uses 2 user inputs, it gets a number between 1-15 from the user and asks if the user was good, bad or ehh

        -if either valid did not fit the conditions set by the program, the program will ask the user these conditions again for however many times

    dictionary color pallete>>>>
        1. to change snowflakes based on if the user was good, bad, or ehh
        2. used a dictionary to house 3 different lists of different color palletes for each snowflake to be everytime a snowflake was drawn
        3.Got user input and depending on the user input a color pallete would be selected from the dictionary and used to draw the snowflakes 
        4.entering 'good' would make the pallete blue, cyan & white
        5.entering 'ehh' would make the pallete white
        6. entering 'bad' or anything else would make the pallete red, yellow, and orange

    Koch snowflake>>>>
        1. A koch snowflake is a triangle where it's sides form smaller triangles, this pattern of triangles forming on sides goes on and on.
        2.Used recursive function 'flake()' to draw a side of the snowflake, it would emulate this 'triangle with triangle sides' pattern. Would repeat the pattern 3 times and turn left each time to complete the snowflake
        3. To draw the snow flake i used ' if depth > 0' as a base case condition that would make the turtle draw forward if the depth was 0
        4. The recursive part of the function is in the else where the turtle will turn lefft and right to form triangles on the sides as well as recall the function with the same variables that slowly work towards depth being equal to 0

    Random coords>>>>
        1. used a random number generate for both x and y coordinates
        (350 is max, -175 is min) this creates a range of coordinates to be chosen randomly
        2. I order the turtle to go to the chosen coordinates each time a koch snowflake is drawn

    Random form>>>>
        1. I wanted to make each snowflake random and vary in size and length 
        2.Used a random number generator with a range of 50-25 for the length 
        3.Used a random number generator with a range of 4-2 for the depth
        
    christmas tree>>>>
        2. Created a specific function to draw the tree 
        3. Commanding the turtle itself to go forward, back, or turn to draw the layers and the stem of the tree
        4. Result is an outline of the tree with it's respective green and brown colors 

    return>>>>
        1. After program is finnished drawing it's snowflakes it will print out the number of times the flake function was called
        2. Each time the program runs the number is randomized and can vary from time to time


Koch snowflake conditions>>>
     1.For depth a good range was 2-4; over than 4 would be too complicated(10 would most certainly crash the program) and take too long to draw and less than 2 is too simple

     2.Length, I tried to keep from 25-50 to keep aesthetics and make the program run smoothly while ensuring a majority of the screen won't be covered by a single snowflake

     3.Chose a random starting point to draw snowflakes from 175 to -175 for both x and y. This is optimal for snowflakes inside the visible window but still having range to draw randomly accross the screen
    

possible bugs>>>
    -No case scenario for the program to crash
    -if user does not follow valid input set by the program(not 'good', 'bad' or 'ehh') &(not a number from 1-15) the user must re-enter a suitable value
    -Some cases where a snowflake may be drawn partially outside the window
    -Scenarios where snowflakes clutter in a specfic area
    -If the user inputs a string as the ammount of desired snowflakes
    the program will have an error since it's trying to turn a string of letters into an integer



Peer review>>>
Ashar-
    He really enjoyed the different snowflake colours 
    He suggested I add a case for invalid input other than (good, bad, or ehh)

test cases>>>
    The predicted output is a window with a black background and an outline of a christmas tree with random snowflakes in random places.
    The snowflake ammount and the color of the snowflakes are based on user input with a range of 0-15 and from ('good', ehh, or 'bad')
        - The snowflakes will be either blue, cyan, or white if the input is 'good'
        - the snowflakes will be either red, orange, or yellow if the input is anything other than 'good' or 'ehh'
        - the snowflakes will be all white if the input is 'ehh'
        
    -When the program finishes running it will print the total number of times the recursive function was called 


    Images>>
        
