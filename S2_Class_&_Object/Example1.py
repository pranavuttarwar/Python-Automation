#non static/instance method
class sample:
    #member of class:
    #Methods
    #Variable
    #consturctor
    
    def show(self):
        print("Hello this is class and ibject example")

    def m1(self):
        print("This is method m2")

    def add(self, a,b):
        print(a+b)
    def sqaureofnum(self, num):
        print(num*num)

s1=sample()
s1.show()
s1.m1()
s1.add(10,20)
s1.sqaureofnum(2)