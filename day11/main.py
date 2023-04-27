from art import logo;
from replit import clear;


#Add
def add(n1, n2):
    return n1 + n2


#Subtract
def subtract(n1, n2):
    return n1 - n2


#multiply
def multiply(n1, n2):
    return n1 * n2


#Devide
def devide(n1, n2):
    return n1 / n2


operations = {"+": add, "-": subtract, "*": multiply, "/": devide}


def calculator():
    print(logo)
    num1 = float(input("Whats the first number "))

    for i in operations:
        print(i)

    symbol = input("pick an operation from the line above ")

    num2 = float(input("Whats the second number "))

    isContinuing = True

    while isContinuing:

        calcul = operations[symbol]
        answer = calcul(num1, num2)

        print(f"{num1} {symbol} {num2} = {answer}")

        quest = input(
            f"Do you want to perform another operation with the answe {answer} yes or no: "
        )
        if quest == "yes":
            num1 = answer
            symbol = input("pick an operation from the line above ")
            num2 = float(input("Enter the next number: "))
        else:
            isContinuing = False
            clear()
            calculator()

calculator()
