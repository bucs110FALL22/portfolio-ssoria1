import random
import math
import pygame
#
#
# Part A
# Establish and set the Circle 
pygame.init()
window = pygame.display.set_mode()
windowsize = pygame.display.get_window_size()
#
#
window.fill('aquamarine')
center_x = windowsize[0] / 2
center_y = windowsize[1] / 2
Radius = center_y
pygame.draw.circle(window, 'pink', (center_x, center_y), Radius)
pygame.draw.line(window, 'black', [0, center_y], [windowsize[0], center_y])
pygame.draw.line(window, 'black', [center_x, 0], [center_x, windowsize[1]])
print(windowsize[0])
print(windowsize[1])
#
#
#
#
# Part B and C, where the cordinates has to be settled
x = random.randrange(0, windowsize[0])
y = random.randrange(0, windowsize[1])
#
distance_from_center = math.hypot( windowsize[0] / 2 - x, windowsize[1] / 2 - y)
print(distance_from_center)

# In this case, consider P1 and P2 as player 1 and player 2
P1 = 0
P2 = 0
P1_color = 'orange'
P2_color = 'darkcyan'


# The input is important to show what are we going to see when all dart were performed.
Response = int(input("Choose between P1 or P2, putting the number of the player, either be 1 or 2:  "))
is_in_circle = distance_from_center <= Radius
print(is_in_circle)

for i in range(10):
  # Turn of the player number 1
  x = random.randrange(0, windowsize[0])
  y = random.randrange(0, windowsize[1])
  distance_from_center = math.hypot( windowsize[0] / 2 - x, windowsize[1] / 2 - y)
  
  if distance_from_center < Radius:
   pygame.draw.circle(window, P1_color, (x,y), 2)
   P1 += 1 
  else:
   pygame.draw.circle(window, 'mediumblue', (x,y), 2)

  # Turn of the player number 2   
  x = random.randrange(0, windowsize[0])
  y = random.randrange(0, windowsize[1])
  pygame.draw.circle(window, 'gray', (x,y), 2)
  distance_from_center = math.hypot( windowsize[0] / 2 - x, windowsize[1] / 2 - y)
  if distance_from_center < Radius:
   pygame.draw.circle(window, P2_color, (x,y), 2)
   P2 += 1
  else:
   pygame.draw.circle(window, 'mediumblue', (x,y), 2)  
  pygame.display.flip() 
if P1 > P2:
 print("You are the winner Player 1 :)") if Response == 1 else print("Sorry too bad")
elif P1 < P2:
 print("You are the winner Player 2 :)") if Response == 2 else print("Sorry too bad")

elif P1 == P2:
 print("Well, we have a tie today")

pygame.time.wait(11000)

#
#
#