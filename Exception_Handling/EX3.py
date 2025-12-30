print("Example of generic exception handling")

#I don't wish to terminate the code if you have no idea what exception will occure that time this will
#be useful

#super exception as exception calss

print("Program Started")
num1=10
num2=0

try:
    print(num1/num2)

except Exception:
    print("Generic exception handled")

print("Program Ended")

print("---------------------")

print("If you want to find the exception name then print e")

print("Program Started1")
num1=10
num2=0

try:
    print(num1/num2)

except Exception as e:
    print("Generic exception handled as: ",e)

print("Program Ended2")
