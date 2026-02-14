class Father:
    #@staticmethod
    def home(self):
        print("1BHK")

class son(Father):
    #@staticmethod
    def home(self):
        print("son class method home method Override now 2BHK")

s=son()
s.home()
