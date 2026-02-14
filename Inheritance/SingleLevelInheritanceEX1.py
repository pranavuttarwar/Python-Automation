#Single Level Inheritance

class father:
    def car(self):
        print("Car: Skoda")

    def home(self):
        print("Home: 3BHK")

    def money(self):
        print("money: 10L")

class son(father):
    def mobile(self):
        print("Mobile: Iphone15")


s=son()
s.car()
s.money()
s.home()
s.mobile()