import random
numbers = random.randrange(1, 11, 1)
# With the random module imported, the selection of any number between 1 to 10 would be established.
# 
# In this exercise, it is more about guessing a possible number, by which "print(numbers)" is not going to be necessary, but it could be useful to prove the programm.
# Putting a number of Guesses is perfect to get a well idea in its creation and application.
guesses = 3
attempts_guesses = guesses
#
# For loop help us to state the commands according to our results in guessings, and considering the attempts that you could have. 
for i in range(guesses):
  answer = int(input("What is your number? (1-10)"))
  if (answer > numbers):
    attempts_guesses = attempts_guesses - 1
    print("Too High", attempts_guesses, '/', guesses, 'opportunities')

  elif (answer < numbers):
    attempts_guesses = attempts_guesses - 1
    print("Too low", attempts_guesses, '/', guesses, 'opportunities')
    
  elif (answer == numbers):
    print("Correct")
    break
    
 