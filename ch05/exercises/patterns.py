#
#
#
def star_pyramid():
 stars = int(input("Introduce your number of rows: "))
 count = 0
 while count <= stars:
   print('*'*count)
   count = count + 1     
star_pyramid()






def rstar_pyramid():
 stars = int(input("Introduce your number of rows: "))
 count = stars
 while count >= 0:
   print('*'*count)
   count = count -1     
rstar_pyramid()


#
#
#


