#Method with return type

class sample:
    def add(self,a,b):
        return a+b

s=sample()
addition=s.add(2,3)
print("addition", addition)

print("-----method 2-----")
print(s.add(10,3))