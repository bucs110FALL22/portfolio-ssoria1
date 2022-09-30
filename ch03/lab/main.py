import turtle #1. import modules
import random
import pygame
import math

#Part A
window = turtle.Screen() # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle() # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up() # 4. Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)
michelangelo.pendown()
leonardo.pendown()
## 5. Your PART A code goes here
#michelangelo.forward(random.randrange(1,101,1))
#leonardo.forward(random.randrange(1,101,1))
for turn in range(50):
  michelangelo.forward(random.randrange(1, 10,1))
  leonardo.forward(random.randrange(1, 10, 1))

michelangelo.up()
leonardo.up()
michelangelo.setposition(-100,20)
leonardo.setposition(-100,-20)

window.exitonclick()


# PART B - complete part B here
pygame.init()
window = pygame.display.set_mode((500,500))

def drawShape(num_sides):
  coords = []
  offset = 100
  side_length = 50
  num_sides = num_sides
  
  for n in range(num_sides):
    thetha = (2.0 * math.pi * n) / num_sides
    x = side_length * math.cos(thetha) + offset
    y = side_length * math.sin(thetha) + offset
    coords.append([x,y])
    print(thetha)
    print('x=', x)
    print('y=', y)
  return coords
    

# Make a triangle, square, hexagon, nonagor and circle.
window.fill("white")
pygame.display.flip()

pygame.draw.polygon(window, 'green', drawShape(3))
pygame.display.flip()
pygame.time.delay(300)
#
window.fill("white")
pygame.display.flip()


pygame.draw.polygon(window, 'red', drawShape(4))
pygame.display.flip()
pygame.time.delay(300)
#
window.fill("white")
pygame.display.flip()


pygame.draw.polygon(window, 'blue', drawShape(6))
pygame.display.flip()
pygame.time.delay(300)
#
window.fill("white")
pygame.display.flip()


pygame.draw.polygon(window, 'yellow', drawShape(9))
pygame.display.flip()
pygame.time.delay(300)
#
window.fill("white")
pygame.display.flip()


pygame.draw.polygon(window, 'orange', drawShape(360))
pygame.display.flip()
pygame.time.delay(300)
#
window.fill("white")
pygame.display.flip()


#
#
