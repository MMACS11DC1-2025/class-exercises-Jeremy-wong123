"""
Machines are good at crunching numbers - faster and more accurately than most 
humans! Create a small program that calculates something useful to you 
(making you smile is useful). It should take user input, at use at least one of the 
number operators we saw in class: + / * . You may modify one of your previous 
exercises to include calculations, if you wish.

Remember to design your algorithm in English first, then translate it to Python 
code. Test as you go!
"""
eq = int(input("first number "))
op = input("operation ")
eq2 = int(input("next number "))
out = 0
if( op == 'x' or op == 'X'):
    out = out + eq * eq2
elif(op == '/'):
    out = out + eq / eq2
elif(op == '+'):
    out = out + eq + eq2
elif(op == '-'):
    out = out + eq - eq2
else:
    print("Dawg what")
print(str(out))