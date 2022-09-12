import turtle
my_turtle = turtle.Turtle()
my_turtle.color("green")
my_turtle.shape("turtle")
screen = turtle.Screen()
numbersides = int(input("Put the number of sides that you want:"))
length = int(input("Introduce the length:")) 
angle = 360 / numbersides
screen = turtle.Screen()
for i in [angle]*numbersides:
  my_turtle.forward(length)
  my_turtle.left(i)
screen.exitonclick()