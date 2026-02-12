import self


class function:
    def __init__(self,arg1,arg2):
        self.arg1=arg1  #private access specifier __
        self.arg2=arg2

    def __add(self):
        print(self.arg1+self.arg2)

    def sub(self):
        print(self.arg1-self.arg2)

    def call(self):
        print(self.__add())

fn=function(20,10)

#fn.add()
fn.sub()
fn.call()
print("Value1: ",fn.arg1)
print("Value2: ",fn.arg2)