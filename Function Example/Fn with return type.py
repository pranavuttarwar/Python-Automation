#Git repo for velocity: https://github.com/SanjayChetlure/8th-Nov-Python-2025.git
#Function with single return type

def add(a,b):
    return a+b
a=add(10,10)
b=add(20,20)
print("addition1:",a )
print("addition2:",b )

#Function with single return type

def name():
    return 'Pranav'

print("Name:",name())


print("---Function with multiple return type---")

def add(num1, num2):
    add=num1+num2
    mul=num1*num2
    return add,mul

Addition, Multiplication=add(10,20)
print("Addition:",Addition)
print("Multiplication:",Multiplication)
