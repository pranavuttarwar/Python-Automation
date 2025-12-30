print("Correct way of generic exception handling")

print("Program Started")
num1=10
num2=0

try:
    print(num1/num2)
except ValueError:
    print("Value error")
except EncodingWarning:
    print("Encoding error")
# except ZeroDivisionError:
#     print("Division error handled")
except Exception as e:
    print("Generic exception handled",e)

print("Program Ended")