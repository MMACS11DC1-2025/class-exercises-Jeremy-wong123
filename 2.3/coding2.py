"""
Write an Olympic Judging program that outputs the average scores from 5 different judges. 

Each score is out of 10 points maximum. Half points are allowed (e.g. 7.5)

The program should take 5 inputs and output the final average score.

Example:

Judge 1: 5.5
Judge 2: 10
Judge 3: 7
Judge 4: 8.5
Judge 5: 9
Your Olympic score is 8.0
"""
import random
print("Your score is from 0-10, half marks are allowed")
ra = input(" What is Judge 1 score?(0-10)")
rt = input(" What is Judge 2 score?(0-10)")
re = input(" What is Judge 3 score?(0-10)")
ri = input(" What is Judge 4 score?(0-10)")
rn = input(" What is Judge 5 score?(0-10)")

avg = (int(ra) + int(rt) + int(re) + int(ri) + int(rn))/5

print("Your average score is: " + str(avg))