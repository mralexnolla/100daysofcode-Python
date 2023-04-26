from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)
print("Welcome to the bid")

bidList = []

def bidCalculator():
  bidderName = ""
  firstBid = 0;
  for i in bidList:
    if i["bid"] > firstBid:
      bidderName = i["name"]
      firstBid = i["bid"]
  print(f"The winner is {bidderName} with a bid of ${firstBid}")
  

isBidOn = True;

while isBidOn:
  name = input("Enter your name: ")
  bid = int(input("Enter your bid $"))
  
  bidAdd = {}
  bidAdd["name"] = name
  bidAdd["bid"] = bid
  bidList.append(bidAdd)
  
  ask = input("Are there other bidder? 'yes' or 'no': ")
  ask = ask.lower()
  if ask == 'yes':
    clear()
    print(logo)
    isBidOn
  else:
    clear()
    print(logo)
    isBidOn = False;

bidCalculator()