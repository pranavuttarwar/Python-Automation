#rm -rf .gitprint armstrong number from 1 to 1000
for num in range(1,1001):
    sum=0
    org=num
    while org>0:
        rem=org%10
        sum=sum+rem*rem*rem
        org=org//10
    if sum==num:
        print("This Number is armstrong from 1 to 100: ",num)