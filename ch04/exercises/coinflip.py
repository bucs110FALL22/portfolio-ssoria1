import turtle
import random
    

window = turtle.Screen() 
window.bgcolor('blue')
Tito = turtle.Turtle() 
Tito.color('green')
Tito.shape('turtle')

Tito.setpos(0,0)

distance = 50
angle = 90
in_screen = True 

while in_screen:
  coin = random.randrange(0, 2)
  if coin == 0:
    Tito.left(angle)
  else:
    Tito.right(angle)
  Tito.forward(distance)

  turtle_Xaxis = Tito.xcor()
  turtleY_Yaxis = Tito.ycor()

  range_of_x = window.window_width()/2
  range_of_y = window.window_height()/2



  if abs(turtle_Xaxis) > range_of_x or abs(turtleY_Yaxis) > range_of_y:
    in_screen = False


window.exitonclick()
