class father:
    def home(self):
        print("method home in superclass")

class son(father):
    def home(self):
        super().home()  #used to call the parent(old) method from parent
        print("Method home in subclass")

s1=son()
s1.home()