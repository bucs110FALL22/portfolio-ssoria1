import random
#Part A
# In the first part, having account the data of weeks, number of classes and tuition, it has to carry out the cost per week through the division between tuition by classes and that result divided by the number of weeks
weeks = 16
print(weeks, type(weeks))
classes = 5
print(classes, type(classes))
tuition = 6000
print(tuition, type(tuition))
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week)
# If we consider that the class per week are three times so it is necessary to calculate a cost per class
class_per_week = 3
print(class_per_week, type(class_per_week))
cost_per_class = cost_per_week/class_per_week
print("So the cost per class for you would be an estimated of:", cost_per_class)
#
#
#Part B
# With the support of the "random module", it has to perform a list with the command choice by this module.
# So in this case, I decided to create a list with different variables between colors, numbers and symbols to its creation.
list = [5,'purple','x',9,'red']
Variable = random.choice(list)
print(Variable)