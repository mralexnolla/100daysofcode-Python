from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
my_coffee_maker = CoffeeMaker()
menu = Menu()


is_on = True


while is_on:
    choices = menu.get_items()
    choice = input(f"What will you like {choices}?: ")
    if choice == 'off':
        print("Shutting down \n .....power off")
        is_on = False
    elif choice == 'report':
        my_coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if my_coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                my_coffee_maker.make_coffee(drink)









