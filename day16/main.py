MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

gain = 0;

def is_enough(ingredients):
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry not enough {ingredients[item]}")
            return False
        return True

def process_coins():
    print("Please insert the coinst ")
    tot = int(input("howmany Cedis:? ")) * 0.25
    tot += int(input("howmany Pessewas:? ")) * 0.1
    # tot += int(input("howmany nikles:? ")) * 0.05
    # tot += int(input("howmany penies:? ")) * 0.01
    return tot

def is_successfull_transaction(cash_received, drink_cost):
    if cash_received >= drink_cost:
        change = round(cash_received - drink_cost, 2)
        print(f"Collect your Ceids {change} in change")
        global gain
        gain += drink_cost
        return True
    else:
        print("Sorry thats is not enough money: Money refunded")
        return False

def make_coffee(drink, ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f" Your drink {drink} is served")


is_on = True

while is_on:
    choice = input('What would you like? (espresso/latte/cappuccino): ').lower()
    if choice == "off":
        print("Power Off");
        is_on = False;
    elif choice == "report":
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}ml")
    else:
        drink = MENU[choice]
        if is_enough(drink['ingredients']):
            payment = process_coins()
            if is_successfull_transaction(payment, drink['cost']):
                make_coffee(choice, drink['ingredients'])

