class father:
    name='balaji'

class son(father):
    name='pranav'
    def son(self):
        print("subclass name variable: ",self.name)
        print("SuperClass name varibale: ",super().name)

s1=son()
s1.son()