class sample:
    def m1(self):
        print("m1 method non static method")
    def squareofnum(self, num):
        print("Square of", num ,"is", num*num)

    @staticmethod
    def m2():
        print("M2 method static method")
    @staticmethod
    def multi(n,k):
        print("Multiplication is:", n*k)

#Calling Non static method
s=sample()
s.m1()
s.squareofnum(5)

print("------------")
#calling static method
sample.m2()
sample.multi(4,5)
