import turtle
#
#
window = turtle.Screen() 
window.bgcolor('lightblue')
Tito = turtle.Turtle() 
Tito.color('green')
Tito.shape('turtle')
#
#
def drawEqShape(numbersides, side_length):
  angle = 360 / numbersides
  for i in [angle]*numbersides:
    Tito.forward(side_length)
    Tito.left(i)


numbersides = int(input("How many sides do you want create?:   "))
side_length = int(input("What would be your side length?:      "))
drawEqShape(numbersides, side_length)
window.exitonclick()