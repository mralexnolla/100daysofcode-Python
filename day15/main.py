import random
from game_data import data
from replit import clear


def rand_account():
  randPer = random.choice(data)
  return randPer

def format_choice(formt):
  name = formt['name']
  description = formt['description']
  country = formt['country']
  return f"{name} a {description} from {country}"


def correctChoice(guess, pa_followers, pb_followers):
  if pa_followers > pb_followers:
    return guess == "a"
  else:
    return guess == "b"

def game():
  isCorrect = True
  score = 0
  
  personA = rand_account()
  personB = rand_account()

  choiceA = format_choice(personA)
  choiceB = format_choice(personB)

  def compare_message():
    print(f"Compare A: {choiceA} \n \n vs \n \n Against B: {choiceB}")

  while isCorrect:
    personA = personB
    personB = rand_account()

    while personA == personB:
      personB = rand_account()

      compare_message()
      
      guess = input("Who has more followers? Type 'A' or 'B': ")
      pa_followers = personA['follower_count']
      pb_followers = personB['follower_count']
      
      correctChoice(guess, pa_followers,pb_followers)

      if correctChoice:
        clear()
        score += 1
        print(f"score {score}")
      else:
        isCorrect = False
        print(f"Final score {score}")
      
game()