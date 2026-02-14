#same local varibale can used for multiple methods

class cal:
    def __init__(self,num1, num2):
        self.num1=num1
        self.num2=num2

    def add(self):
        print("Addition:",self.num1+self.num2)

    def sub(self):
        print("Subtraction:",self.num1-self.num2)

    def mul(self):
        print("Multiplication:",self.num1*self.num2)

    def div(self):
        print("Division:",self.num1/self.num2)

ca=cal(20,10)
ca.add()
ca.sub()
ca.mul()
ca.div()