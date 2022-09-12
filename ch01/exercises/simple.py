# First, It had to carry out some operation to know and recognize more about our programm as our second exercise.
a = print(10 * 5)
b = print(10 ** 2)
c = print(15 / 10)
d = print(15 // 10)
e = print(-15 // 10)
f = print(15 % 10)
g = print(10 % 15)
h = print(10 % 10)
i = print(0 % 10)
j = print(10 / 15)
#
#
#
# The second part is about try to convert Euros to Dollars, by which it was necessary to take account an amount of Euros and the Rate that you would get through exchange. Therefore a total would be displayed according to an estimated fee of 3 dollars. 
x = input("What amount of euros do you have?")
Amount = float(x)
y = input("What is the rate of Euros that you want in dollars?")
Rate = float(y)
Total = Amount * Rate
Result = Total - 3
print(Result)