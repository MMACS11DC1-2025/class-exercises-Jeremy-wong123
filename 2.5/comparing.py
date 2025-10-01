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
database, find the perso with the best matching items and print out the name.
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
for x in range(len(urlist)):
    for line in file:
        theyline = line.split(',')
        print(str(theyline))
        tl= list(map(str.lower, theyline))
        if urlist[x] in line:
            tally += 1
            print("I've added one to the tally")
            if tally > bestma:
                bestma = tally
                bestpor = theyline
                nam = bestpor[1]
print(nam)
print(bestma)
print(bestpor)

            
