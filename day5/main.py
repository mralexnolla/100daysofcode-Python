import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
print("Welcome to the Rock, Paper, Scissors game with #thankU4Ex16");

item = ["rock", "paper", "scissors"]

yourCchoice = input("Enter your choice rock, paper, scissors ");
computerChoice = random.choice(item)

if yourCchoice == computerChoice:
  print("Tie");
elif yourCchoice == "rock" and computerChoice == "paper":
  print("You choose " + yourCchoice + "\n" + "Computer choose paper" + paper + "\n" + "computer Wins");
elif yourCchoice == "paper" and computerChoice == "scissors":
  print("You choose " + yourCchoice + "\n" + "Computer choose scissors" + scissors + "\n" + "computer Wins");
elif yourCchoice == "scissors" and computerChoice == "rock":
  print("You choose " + yourCchoice + "\n" + "Computer choose rock" + rock + "\n" + "computer Wins");
elif yourCchoice == "paper" and computerChoice == "rock":
  print("You choose " + yourCchoice + "\n" + "Computer choose rock" + rock + "\n" + "You Wins");
elif yourCchoice == "scissors" and computerChoice == "paper":
  print("You choose " + yourCchoice + "\n" + "Computer choose paper" + paper + "\n" + "You Wins");
elif yourCchoice == "rock" and computerChoice == "scissors":
  print("You choose " + yourCchoice + "\n" + "Computer choose scissors" + scissors + "\n" + "You Wins");
  
  





