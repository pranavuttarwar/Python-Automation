num1=10
num2=0
print(num1,num2)

try:   # Add Risky Code in this block
    print(num1/num2)

except ZeroDivisionError:
    print("division by zero is not allowed")
    print(num1/1)

print("Hi")
print("Hello")
print("Program Ended")
