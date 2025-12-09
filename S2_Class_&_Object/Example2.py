#method with static method

class demo:
    @staticmethod
    def m1():
        print("M1 mehtod")
    def m2():
        print("M2 mehtod")

    def add(a,b):
        print(a+b)

demo.m1()
demo.m2()
demo.add(10,10)