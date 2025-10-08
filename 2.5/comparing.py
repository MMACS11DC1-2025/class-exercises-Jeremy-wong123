"""
Create a program that uses comparison operators (< > <= >=).
You must use the class' datafile, 'responses.csv' and analyze it
    to make at least 2 interesting observations.
You may use user input to add interactivity to the program.
You must design your algorithm in English first, then translate it to Python code.
Test as you go! Describe in your comments what steps you took to test your code.
"""
""" My assignment
-I plan to make a program that take the user input in a 
suvery format. It will than compare the results with the list of users in the
database, find the person with the best matching items and print out the name.
1.)I first run a for loop to ask the user a bunch of questions
2.) I ask for the users name and I will omit the user if he/she is in the database
3.)I get a list of the users input
4.) I than get a for loop of the line and file so the program can sift through all lines in the file
5.) I than use a for loop for x in range(len(urlist)): so the program can sift through all options of 
the user input and see which line has a match
6.) If a match is found between the two lists, 1 is added to the tally
7.) Than if the tally is greater than the bestmatch or 0 bestmatch will be set to equal tally to continue a " best of the best" system
8.) It will then set a variable equal to the list of the best similar list
9.)The tally variable will be set 0 at the start of the for line in file loop to reset the tally each time an option comes out better
10.) in the end The program will print out the name of your best match

Code showcase:
What is your full name? jeremy wong
what is your favourite number?8
what is your favourite pet?cat
what is your favourite subject?math
what is your favourite sport to play?football
what is your favourite movie genre? Adventure
What is your favourite place to eat?Popeyes
Your best match is serene lee
You have a 4/8 similarity.
"""
file = open("2.4/responses.csv")
urlist = []
tally = 0
lq = ['What is your favourite number?', 'What is your favourite pet?', 'What is your favourite subject?', 'What is your favourite sport to play?', 'What is your favourite sport to watch?', 'What is your favourite genre of music?', 'What is your favourite movie genre?', 'What is your favourite place to eat?']
urlist = []
namer = input('what is your full name? ').lower().strip() 
for ques in lq:
    quest = input(ques).lower().strip()
    urlist.append(quest)
bestma = 0
bestpor = ""
junk = file.readline()
for line in file: 
    tally = 0
    for x in range(len(urlist)):
        theyline = line.lower().split(',')
        #print(tl)
        if namer in theyline:
            #print('your name is in the database')
            #exits the if ad continues the for loop skipping the line
            continue
        if urlist[x] in theyline:
            tally += 1
            #print("I've added one to the tally")
    if tally > bestma:
        bestma = tally
        bestpor = theyline

nam = bestpor[1]
                
print("Your best match is " + str(nam) + ".\n You two have a " + str(bestma) + "/8 similarity.")
#print(bestma)
#print(bestpor)

            
