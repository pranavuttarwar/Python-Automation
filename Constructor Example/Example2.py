#Constructor with single parameter

class demo:
    def __init__(self,num):
        self.num1=num


    def mul(self):
        print(self.num1*self.num1)

    def cubeofnum(self):
        print(self.num1*self.num1*self.num1)


d=demo(4)
d.mul()
d.cubeofnum()