import pygame
import math
import time
#
#
#
pygame.init()
display = pygame.display.set_mode()
iters = {}  
n = int(input("Introduce your number  : "))
print(int(n))
upper_limit = 20
y_count = 1
start = 2 


for i in range(start, upper_limit + 1):
  count = 0
  y_count = 1

while n != 1:
  if (n % 2 == 0):
    n = n // 2
    print(n)
  else:
    n = 3 * n +1
    print(n)
  count = count + 1
  iters[n] = (count)
  
print(iters)
c00rdinates = list(iters.items())
print(c00rdinates)
pygame.draw.lines(display, 'black' , False , c00rdinates)
#
type(c00rdinates[0])
new_display = pygame.transform.flip(display, False, True)
display.blit( new_display , c00rdinates[2] )
font = pygame.font.Font(None, 130)
msg = font.render("msg", True , 'green')
display.blit(msg, (300,300))


pygame.display.flip()
time.sleep(100)





