#Constuor without parameter

class sample:
    def __init__(self):
        print("This is constructor class")

    def add(self,a,b):
        return a+b

s=sample()
print(s.add(11,11))