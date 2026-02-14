class father:
    def home(self):
        print("Father class from home method (superclass)")

class son1(father):
    def mobile(self):
        print("Mobile is subclass from son1")

class son2(father):
    def laptop(self):
        print("laptop is subclass form son2")

s1=son1()
s1.home()
s1.mobile()
s2=son2()
s2.home()
s2.laptop()