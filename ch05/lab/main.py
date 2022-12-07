import turtle

def seq3np1(n):
  count = 0
  while(n != 1):
    if(n % 2) == 0: 
      n = n // 2
    else: 
      n = n * 3 + 1
      count += 1
  return count

def drawingGraph(iterations):
  graph_line = turtle.Turtle() 
  graph_line.speed(0)
  graph_line.up()
  graph_line.goto(0,0)
  graph_line.down()

  sentence = turtle.Turtle()
  sentence.speed(0)

  windown = turtle.Screen()
  windown.setworldcoordinates(0, 0, 10, 10)

  max_so_far = 0

  for i in range(1, iterations + 1):
    result = seq3np1(i)
    print("The number " + str(i) + " has " + str(result) + " iterations.")

    if result > max_so_far:
      max_so_far = result
      sentence.clear()
      sentence.up()
      sentence.goto(i, max_so_far)
      sentence.write("Maximum so far: " + str(max_so_far))

    windown.setworldcoordinates(0, 0, i + 10, max_so_far + 10)
    graph_line.goto(i, result)

  windown.exitonclick()

def main():

  upper = int(input("Please enter an upper bound for the function: "))
  start = 1
  while (start < upper):
    start += 1
    count = seq3np1(start)
    print("The number " + str(start) + " has " + str(count) + " iterations.")
  drawingGraph(upper)

main()




  






