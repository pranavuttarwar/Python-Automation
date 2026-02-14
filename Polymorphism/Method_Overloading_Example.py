class calc:
    def add(self,a=0,b=0,c=0,d=0):
        print('Addition is',a+b+c+d)

ca=calc()
ca.add()
ca.add(1,2)
ca.add(1,2,3)
ca.add(1,2,3,4)

print("---------------------")

class info:
    def data(self,name='ABC'):
        print('Your Info is:',name)

ina=info()
ina.data()
ina.data('Pranav')