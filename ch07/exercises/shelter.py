from datetime import datetime
from time import gmtime, strftime
import random 
#
#
#
class Shelter:
  def __init__(self, name, type):
    self.name = name
    self.type = type


Animal_1 = Shelter('Scott', 'dog')
date_arrived_one = datetime(2013, 4, 19, 10, 55, 23)
date_adopted_one = datetime(2016, 7, 2, 14, 10, 47)
#
Animal_2 = Shelter('Karin', 'cat')
date_arrived_two = datetime(2010, 9, 5, 18, 21, 4)
date_adopted_two = datetime(2018, 5, 24, 11, 31, 10)
#
Animal_3 = Shelter('Rodrigo', 'bird')
date_arrived_three = datetime(2015, 11, 24, 9, 42, 47)
date_adopted_three = datetime(2021, 9, 18, 17, 2, 59)
   


def main():
  print("Name:", Animal_1.name,  "Type:", Animal_1.type)
  Animal_1_ID = print("ID: ", id(Animal_1))
  Animal_1_arrived = print("Date Arrived: ", date_arrived_one.strftime('%Y/%m/%d'))
  Animal_1_adopted = print("Adopted Date: ", date_adopted_one.strftime('%Y/%m/%d'))
  #
  print("Name:", Animal_2.name,  "Type:", Animal_2.type)
  Animal_2_ID = print("ID: ", id(Animal_2))
  Animal_2_arrived = print("Date Arrived: ", date_arrived_two.strftime('%Y/%m/%d'))
  Animal_2_adopted = print("Adopted Date: ", date_adopted_two.strftime('%Y/%m/%d'))
  #
  print("Name:", Animal_3.name,  "Type:", Animal_3.type)
  Animal_3_ID = print("ID: ", id(Animal_3))
  Animal_3_arrived = print("Date Arrived: ", date_arrived_three.strftime('%Y/%m/%d'))
  Animal_3_adopted = print("Adopted Date: ", date_adopted_three.strftime('%Y/%m/%d'))

  
main()

