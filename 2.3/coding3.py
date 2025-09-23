"""
Write a McDoland's program that takes your order and outputs the total cost.

It first asks if you want a burger for $5. It then asks if you want fries for $3. It outputs the total with 14% tax.

The program should accept Yes/No or yes/no.

Example:

Would you like a burger for $5? (Yes/No)
> yes
Would you like fries for $3? (Yes/No)
> yes
Your total is $9.12

Would you like a burger for $5? (Yes/No)
> yes
Would you like fries for $3? (Yes/No)
> no
Your total is $5.699999999999999

Would you like a burger for $5? (Yes/No)
> no
Would you like fries for $3? (Yes/No)
> yes
Your total is $3.42
"""
bur = input(" Would you like a burger for 5$?").lower().strip()
fri = input("Would you like fries for 3$?").lower().strip()
cost = 0
if(bur == 'yes' and fri == 'no'):
    cost = cost + 5 * 1.14
    print("Your total is $" + str(cost))
elif(bur == 'yes' and fri == 'yes'):
    cost = cost + (5 + 3) * 1.14
    print("Your total is $" + str(cost))
elif(bur == 'no' and fri == 'yes'):
    cost = cost + 3 * 1.14
    print("Your total is $" + str(cost))
else:
    print("Your total is $0")
