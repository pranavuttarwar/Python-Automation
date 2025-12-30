print("Multiple Except block example")
print("Program Stared")
num1=10
num2=0

try:
    print(num1/num2)  #riskay code

except ValueError:
    print("ValueError")
except ZeroDivisionError:
    print("ZeroDivisionError")
# except ZeroDivisionError:
#     print("ZeroDivisionError")
print("Program Ended")
