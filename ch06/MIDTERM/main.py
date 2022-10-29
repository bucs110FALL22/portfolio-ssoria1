import turtle
# This program execute the drawing of an extinct amphibian called "Diplocaulus", by which I prefered to use the name Sally. 
window = turtle.Screen() 
window.bgcolor('gray')
Sally = turtle.Turtle() 
Sally.color('black')
Sally.shape('turtle')

# At measure, I was working with the drawing, I establish stand out every part separately.
#In Draw face, the face is conformed by two triangles and one diamond to get the true shape of the Amphibian, using commands of the turtle module. 
def face():
  Sally.fillcolor("dodgerblue4")
  Sally.begin_fill()
  Sally.left(25)
  Sally.forward(119)
  Sally.left(90)
  Sally.forward(91)
  Sally.left(90)
  Sally.forward(119)
  Sally.left(90)
  Sally.forward(92)
  Sally.end_fill()

  Sally.fillcolor("dodgerblue4")
  Sally.begin_fill()
  Sally.right(180)
  Sally.forward(221)
  Sally.right(149)
  Sally.forward(149)
  Sally.end_fill()

  Sally.fillcolor("dodgerblue4")
  Sally.begin_fill()
  Sally.penup()
  Sally.left(45)
  Sally.forward(44)
  Sally.pendown()
  Sally.forward(202) 
  Sally.right(156)
  Sally.forward(186)
  Sally.goto(0, 0)
  Sally.left(90)
  Sally.end_fill()

#For Draw neck, I implement the "For loop" commands to get a style unique, besides in the beginning I was thinking to keep it simple, but then while I was looking and proving, at final a neck with spikes is not bad. 
def star_neck():
  Sally.fillcolor("cadetblue3")
  Sally.begin_fill()
  spikes = 4
  application = spikes*[5]
  for neck in range(6):
    for forming in application:
      Sally.right(11)
      Sally.forward(5)
    Sally.left(90)
  Sally.end_fill()

# To Draw body, I allow to get a body using while loops to get to understand the process.
def body():
  times = 0
  times = times + 2
  Sally.fillcolor("deepskyblue4")
  Sally.begin_fill()
  while times == 2:
    for body in range(2):
      Sally.forward(97)
      Sally.left(104)
      Sally.forward(86)
      Sally.right(45)
      Sally.forward(77)
      Sally.left(120)

    break
  Sally.end_fill()

# Here I decided to work adding two little arms as two fins. 
def little_arms():
  Sally.penup()
  Sally.goto(-5, -65)
  Sally.pendown()
  Sally.left(90)
  Sally.fillcolor("greenyellow")
  Sally.begin_fill()
  Sally.right(60)
  Sally.forward(60)
  
  Sally.right(60)
  Sally.forward(60)
  Sally.left(80)
  
  Sally.end_fill()

  Sally.penup()
  Sally.goto(4, -70)
  Sally.fillcolor("greenyellow")
  Sally.pendown()
  Sally.right(90)
  Sally.begin_fill()
  Sally.left(90)
  Sally.forward(60)
  Sally.left(60)
  Sally.forward(60)
  Sally.right(80)
  Sally.circle(10,22)

  Sally.end_fill()


#And for to draw the tail, I used for loops to generate a dangerous and sharp tail.
def tail():
  Sally.goto(103, -173)
  Sally.pendown()
  Sally.fillcolor("cornflowerblue")
  Sally.begin_fill()
  for i in range(4):
    Sally.setheading(45)
    Sally.circle(66, 80)
    Sally.left(20)
    Sally.backward(60)

  Sally.right(34)
  Sally.circle(140,-170)
  Sally.end_fill()

# To avoid most common eye design with a simple circle, I decided to adding color that brings personality to Sally's eyes.
def eyes():
  Sally.fillcolor('hotpink')
  Sally.begin_fill()
  Sally.setpos(16,40)
  Sally.setheading(270)
  Sally.begin_fill()
  Sally.circle(15,180)
  Sally.forward(10)
  Sally.circle(15,180)
  Sally.forward(10)
  Sally.end_fill()

  Sally.fillcolor('white')
  Sally.begin_fill()

  Sally.circle(8,180)
  Sally.forward(5)
  Sally.circle(8,180)
  Sally.forward(5)
  Sally.end_fill()

  Sally.penup()
  Sally.goto(-18, 40)
  
  Sally.fillcolor('hotpink')
  Sally.begin_fill()
  
  Sally.setheading(270)
  Sally.begin_fill()
  Sally.circle(15,180)
  Sally.forward(10)
  Sally.circle(15,180)
  Sally.forward(10)
  Sally.end_fill()

  Sally.fillcolor('white')
  Sally.begin_fill()

  Sally.circle(8,180)
  Sally.forward(5)
  Sally.circle(8,180)
  Sally.forward(5)
  Sally.end_fill()
#
# At final, I put every function in a principal with precise coordinates to each part of the body of Sally, along with an additional print.  
def main():
  face()
  star_neck()
  Sally.penup()
  Sally.goto(69,-10)
  Sally.right(15)
  Sally.pendown()
  body()
  little_arms()
  Sally.penup()
  tail()
  Sally.penup()
  eyes()
  Sally.penup()
  Sally.forward(50)
  Explanation = print("Here is Sally the Diplocaulus, drawing made it by Sergio Soria.")
main()
#
window.exitonclick()
