print("1 to 5 Number: ")

#start from 1
# End till 5
#inc/dec by 1
# by Default 3rd parameter is:1

#Syntax for variable in range(start number, end number+1):

for n in range(1,6,1): #condition in backend n<6
    print(n,end=" ") #1 2 3 4 5 used to print in one line.

#Example 2 by user input
i=int(input("Enter any number to print from 1 to: "))

for i in range(1,i+1): #condition in backend n<6
    print(i)

#Print even number from 2 to 20 increment by 2

for k in range(2,20):
    print(k*2, end=" ")

#Syntax for Decrement: variable in range(start number, end number-1,-decnumber):

print("5 to 1 number")

for i in range(5,0,-1):
    print(i,end=" ")

#Print(odd number from 11)


#print odd number from 11 to 1
for i in range(11,0,-2):
    print(i, end ="  ")

print ("pranav Logic")

for i in range(11,0):  #11>0
    print(i-2, end=" ")

print("------Print HI message 5 Times----")

for i in range(1,6):
    print("HI")

#square of number from 1 to 15-> Assignment
#Pranav Logic
for i in range(1,17):
    n=i*i
    print(n, end=" ")
