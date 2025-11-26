#Function Without Parameter
#syntax def <function_name>:
    #function body
print("Function Example of without parameter")
a=int(input("Enter First Number: "))
b=int(input("Enter Second Number which smaller than first No: "))

def add():              #Function Declaration
    return a+b
print("Addition: ",add())

def sub():
    return a-b

print("Substraction: ",sub())

def mul():
    return a*b

print("Multiplication: ",mul())

def div():
    return a/b

print("Division: ",div())


