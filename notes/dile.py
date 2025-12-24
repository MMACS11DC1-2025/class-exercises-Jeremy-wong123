from passowrd import x
import re 

max = 99
min = 0
mid = 50
matches = re.findall(r'([a-zA-Z])(\d+)', text)
result = [(char, int(num)) for char, num in matches]

for i in range(len(result)):
    if result[i][0] == 'R'
        mid + 