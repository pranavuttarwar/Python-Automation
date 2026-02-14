#Assignment print Even number from 1 to 100

#num=int(input("Enter a Number till you want to find Even number: "))
num=10
for i in range(1,num+1):
    if i % 2==0:
        print(i," is even")
    else:
        print(i," is odd")

print("-------Assignment print factorial from 1 to 10-----------")

num=10
fact=1
for i in range(1,num+1):
         fact=fact*i
         print(fact)

