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
database, find the top 3 people with the most matching results with the user


1.) I ask for the users name and I will omit the user if he/she is in the database
2.) I than ask the user a survey and put their results on a list
3.) I than get a for loop of the line and file so the program can sift through all lines in the file
4.) I than use a for loop for x in range(len(urlist)): so the program can sift through all options of 
the user input and see which line has a match
5.) If a match is found between the two lists, 1 is added to the tally
6.) Than if the tally is greater than the bestmatch or 0 bestmatch will be set to equal tally to continue a " best of the best" system
7.) It will then set a variable equal to the list of the best similar list
8.)The tally variable will be set 0 at the start of the for line in file loop to reset the tally each time an option comes out better
9.) in the end The program will print out the name of your best match and the ammount of similarities you two have

testcase:
What is your full name? jeremy wong
what is your favourite number?8
what is your favourite pet?cat
what is your favourite subject?math
what is your favourite sport to play?football
what is your favourite sport to watch?football
what is your favourite movie genre? Adventure
What is your favourite place to eat?Bubble waffle 
Your best match is serene lee
Your second best match is 
Your third best match is
You have a 4/8 similarity.
"""
file = open("2.4/responses.csv")
userlist = []
tally = 0
#creates a list of questions for a survey
survey = ['What is your favourite number?', 'What is your favourite pet?', 'What is your favourite subject?', 'What is your favourite sport to play?', 'What is your favourite sport to watch?', 'What is your favourite genre of music?', 'What is your favourite movie genre?', 'What is your favourite place to eat?']
urlist = []
#receives the name of the user it is important that the program doesn't match the user with itself if the user is in the database
name = input('what is your full name? ').lower().strip() 
#Asks the questions in the for loop individually and records the users response into a list 
for quesion in survey:
    question = input(quesion).lower().strip()
    urlist.append(question)
#sets the value for variables of the bestperson and bestmatchscore
bestmatchscore = 0
first = ''
second = ''
third = ''
rank = []
listofnames = []
best = []
#Discards the first line in the database
junk = file.readline()
for line in file: 
    tally = 0
    #initializes the tally to zero before checking for similarities between the two lists
    for x in range(len(urlist)):
        #creates a variable to store a list of a person's qualities in the database
        personlist = line.lower().split(',')
        #checks if the user's name is in the database
        if name in personlist:
            #exits the if ad continues the for loop skipping the line
            continue
        if urlist[x] in personlist:
            #compares the two list of traits between the user and theyline
            tally += 1
            #for each similarity between the two one is added to the tally
    rank.append(tally)
    listofnames.append(personlist[1])
print(str(rank))
score = -1
for i in rank:
    score += 1
    if i > bestmatchscore:
        bestmatchscore = i
first = listofnames[score]
best.append(first)
print(str(best))
#print("Your best match is " + str(nam) + ".\nYou two have a " + str(bestmatchscore) + "/8 similarity.")


            
