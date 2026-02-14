import self


class function:
    def __init__(self,arg1,arg2):
        self.__arg1=arg1  #private access specifier __
        self.arg2=arg2

    def add(self):
        print(self.__arg1+self.arg2)

    def sub(self):
        print(self.__arg1-self.arg2)

fn=function(20,10)
fn.add()
fn.sub()
print("Value1: ",fn.arg1)
print("Value2: ",fn.arg2)