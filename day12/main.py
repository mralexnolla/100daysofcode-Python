
from art import logo
from replit import clear

import random



def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cards):
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
    
  return sum(cards)


def compare(user_score, computer_score):
  if user_score == computer_score:
    print("Its a Draw")
  elif computer_score == 0:
    print("You loose Computer has Blackjack")
  elif user_score == 0 and computer_score != 0:
    print("you win a Blackjack")
  elif user_score > 21:
    print("you loose")
  elif computer_score > 21:
    print("Computer loose")
  elif computer_score > user_score:
    print("You loose")
  else:
    print("you win")

def playGame():
  print(logo)
  user_cards = []
  computer_cards = []
  isGameEnd = False
  
  for i in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  
  while not isGameEnd:
  
    user_score = calculate_score(user_cards);
    computer_score = calculate_score(computer_cards);
    
    print(f"Your cards {user_cards} and score is {user_score}");
    print(f"Computer first cards {computer_cards[0]}")
    
    if user_score == 0 or computer_score == 0 or user_score > 21:
      isGameEnd = True
    else:
      question = input("Do you want another card 'y' for YES and 'n' form No ")
      if question == 'n':
        isGameEnd = True
      else:
        user_cards.append(deal_card())
    
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards);
    print(f"Computer cards {computer_cards} and score in {computer_score}")
    
  compare(user_score, computer_score)

playGame()
  

while input("Do you want play again 'yes' or 'no' ")=="yes":
  clear()
  playGame()
