import turtle
import random

heads = 0 
tails = 0

window = turtle.Screen() 
window.bgcolor('blue')
Tito = turtle.Turtle() 
Tito.color('green')
Tito.shape('turtle')

Tito.setpos(0,0)

coin_flip = random.choices(['Heads', 'Tails'], [5, 5])[0]
flip = print(coin_flip)



flip = 1
while flip != coin_flip:
  if coin_flip == 'Heads':
    Tito.left(90)
    Tito.forward(50)
    Tito.pendown()
    break
    flip = coin_flip + 1
    
   
  elif coin_flip == 'Tails': 
    Tito.right(90)
    Tito.forward(50)
    Tito.pendown()
    break
    flip = coin_flip + 1
    
    


  




window.exitonclick()
