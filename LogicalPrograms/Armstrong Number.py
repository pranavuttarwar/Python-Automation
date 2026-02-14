num=123
sum=0
oriNum=num

while num>0:
    rem=num%10  #Get the last Number
    sum=sum+rem*rem*rem
    num=num//10  #Get the exact variable type instead of float

print(sum)
if oriNum==sum:
    print("The Number is Armstrong")
else:
    print("The Number is not Armstrong")