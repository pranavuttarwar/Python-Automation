from math import factorial

num=int(input("Enter any number for Factorial: "))
fact=1

for i in range(1,num+1):
    fact=fact*i

print("Your given number",num, "factorial is: ",fact)