#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip Calculator")
bill = input("What was the total bill $\n");
bill  = float(bill);

tip = input("What percentatge tip would you like to give 10, 12, 15 ?\n");
tip = float(tip)/100

number_of_people = input("How many people to split the bill?\n");
number_of_people = int(number_of_people)

total_bill = (bill * (1 + tip))/number_of_people


print(f"Each person should pay: ${round(total_bill, 2)}")