print("Example of finally block")

num1=10
num2=0

try:
    print(num1/num2)

except ZeroDivisionError:
    print("Division by zero")
finally:
    print("Finally block Executed")

print("Program Ended")