#
#
#
score = 0

def percentage_to_letter(score):
  if (score >= 90):
    return "A"
  elif (80 <= score < 90):
    return "B"
  elif (70 <= score < 80):
    return "C"
  elif (60 <= score < 70):
    return "D"
  elif (score < 60):
    return "F"


#
#
#
def is_passing(score):
  if score == "A":
    score = True
    print("Your score is A")
  elif score == "B":
    score = True
    print("Your score is B")
  elif score == "C":
    score = True
    print("Your score is C")
        
  else:
    print("You failed, but you can do it")



#
#
#
def main():
  YSC = int(input("What is your score?:  "))
  let = percentage_to_letter(YSC)
  is_passing(let)

main()
#
#
#
#



