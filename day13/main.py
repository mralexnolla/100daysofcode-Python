
import random

def random_number_generator():
  ranList = []
  for number in range(1,101):
    ranList.append(number)
  return ranList

randNumb = random.choice(random_number_generator())

def dificulty_level():
  print("Welcome to the guess the number game")
  print("I am thinking of a number which i want you to guess")
  print(f"the number is {randNumb}")
  difChoice = input("Choose a difficulty level between 'easy' and 'hard': ")
  
  if difChoice == "easy":
    diffLevel = 10
  else:
    diffLevel = 5

  

  isWrongNumb = True

  while isWrongNumb:
    print(f" you have {diffLevel} chances to guess the number start")
    numb = int(input("guess the number "))
    if numb == randNumb:
      print("Correct Number")
      isWrongNumb = False
      
    if numb > randNumb:
      print("Too high")
    elif numb < randNumb:
      print("Too low")
    
    diffLevel -= 1
    
    if diffLevel == 0:
      print("You loose")
      print(f"The number is {randNumb}")
      isWrongNumb = False
    print("--------------------------------")
    

      
    
dificulty_level()


  
  



