import random

print("Banker Roulet - Who will pay the bill today")

nameString = input("Give me everybody's names, separated by a comma. ");

name = nameString.split(", ");

random_n = random.randint(0, len(name)-1);

personChoice = name[random_n]

print(f"{personChoice} is going to buy the meal today!")

