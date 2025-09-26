"""
Create a program that uses comparison operators (< > <= >=).
You must use the class' datafile, 'responses.csv' and analyze it
    to make at least 2 interesting observations.
You may use user input to add interactivity to the program.
You must design your algorithm in English first, then translate it to Python code.
Test as you go! Describe in your comments what steps you took to test your code.
"""
file = open("2.4/responses.csv")

tally = 0
favnum = input("What is your favourite number?")
fapet = input("What is your favourite pet?")
fasub = input("What is your favourite subject?")
faspay = input("What is your favourite sport to play?")
fasport = input("What is your favourite sport to watch?")
fatunes = input("What is your favourite genre of music?")
famov = input("What is your favourite movie genre?")
fafoo = input("What is your favourite place to eat?")

urlist = [favnum, fapet, fasub, faspay, fasport, fatunes, famov, fafoo]

for line in file:
    for line in file:
        if favnum in line.lower(): 
            tally +=1
        elif fapet in line.lower(): 
            tally +=1
        elif fasub in line.lower(): 
            tally +=1
        elif fasport in line.lower(): 
            tally +=1
        elif fatunes in line.lower(): 
            tally +=1
        elif famov in line.lower(): 
            tally +=1
        elif fafoo in line.lower(): 
            tally +=1

