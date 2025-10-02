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

1.) I first get the user input and organize it into a list in lowercase and strip uneccessary spacing.
2.) I than get a for loop of the line and file so the program can sift through all lines in the file
3.) I than use a for loop for x in range(len(urlist)): so the program can sift through all options of 
the user input and see which line has a match
4.) If a match is found between the two lists, 1 is added to the tally
5.) Than if the tally is greater than the bestmatch or 0 bestmatch will be set to equal tally to continue a " best of the best" system
6.) It will then set a variable equal to the list of the best similar list
7.)The tally variable will be set 0 at the start of the for line in file loop to reset the tally each time an option comes out better
8.) in the end The program will print out the name of your best match

"""
file = open("2.4/responses.csv")

tally = 0
favnum = input("What is your favourite number?").lower().strip()
fapet = input("What is your favourite pet?").lower().strip()
fasub = input("What is your favourite subject?").lower().strip()
faspay = input("What is your favourite sport to play?").lower().strip()
fasport = input("What is your favourite sport to watch?").lower().strip()
fatunes = input("What is your favourite genre of music?").lower().strip()
famov = input("What is your favourite movie genre?").lower().strip()
fafoo = input("What is your favourite place to eat?").lower().strip()
nam = ""
urlist = [favnum, fapet, fasub, faspay, fasport, fatunes, famov, fafoo]
bestma = 0
bestpor = ""
for line in file: 
    tally = 0
    for x in range(len(urlist)):
        theyline = line.split(',')
        tl = list(map(str.lower, theyline))
        #print(tl)
        if urlist[x] in tl:
            tally += 1
            #print("I've added one to the tally")
    if tally > bestma:
        bestma = tally
        bestpor = tl

nam = bestpor[1]
                
print("Your best match is " + str(nam))
#print(bestma)
#print(bestpor)

            
