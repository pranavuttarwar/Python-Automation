#Approch 1

import Animal,Bird

Animal.fly()
Animal.walk()

print("-----------")

Bird.fly()
Bird.walk()

print("---approch-2----")

#from Module_And_Pacakages import Animal,Bird


from Bird import *
from Animal import *
fly()
walk()