import time 
import random 

identification = id("dog")
date = time.strftime("%x, %X, %y, %Y")

#
class Shelter:
  def __init__(self, name, type, id = id("dog"), day = date):
    self.name = "name"
    self.type = "type"
    #self.id = id + 1 
    #self.day = date

#
Dog_1 = Shelter()
print(Dog_1.name, Dog_1.type, Dog_1.id, Dog_1.day, type(Dog_1))
#
Dog_1.name = "Fido"
Dog_1.type = "dog"
Dog_1.id = id("dog")
Dog_1.day = time.strftime()

print(Dog_1.name, Dog_1.type, Dog_1.id, Dog_1.day, type(Dog_1))
