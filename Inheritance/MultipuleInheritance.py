#superclass1

class A:
    def m1(self):
        print("Method m1 from superclass A")
#superclass2
class B:
    def m2(self):
        print("Method m2 from superclass B")

 #subclass
class C(A,B):
    def m3(self):
        print("Method m3 from subclass C")

sub=C()
sub.m1()
sub.m2()
sub.m3()