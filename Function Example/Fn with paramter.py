#Syntax def <function_Name>(Parameter1, Prameter2, .... , Parametermn)
  #<function Body>
  #<functiona_Name>(Parameter1, Prameter2, .... , Parametermn)

print("Function Example of with parameter")
#a=int(input("Enter First Number: "))
#b=int(input("Enter Second Number which smaller than first No: "))

def add(a,b):   #Function Declaration
    print(a+b)

print("Addition: ") #add(10,20) function Call
add(10,20)

def sub(a,b):
    print(a-b)

print("Subtraction: ")
sub(20,10)


def mul(a,b):
    print(a*b)

print("Multiplication: ")
mul(4,4)

def div(a,b):
    print(a/b)

print("Division: ")
div(20,10)


def whatsyourdetails(name,surname,age,email):
    print("Name: ", name)
    print("Surname: ", surname)
    print("Age: ", age)
    print("Email: ", email)


whatsyourdetails("Pranav","uttarwar",28,"email@g.com")
whatsyourdetails("Nikita","uttarwar",27,"email123@g.com")

