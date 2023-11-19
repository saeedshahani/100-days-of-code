import os
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def run_machine():
    """
    top level function to run coffee machine
    """
    os.system('cls||clear')
    machine_on = True
    coffeemaker = CoffeeMaker()
    menu = Menu()
    moneymachine = MoneyMachine()
    while machine_on:
        print(menu.get_items())
        drink_name = input("Select an item from the menu: ").lower()
        if drink_name == "off":
            machine_on = False
        elif drink_name == "report":
            coffeemaker.report()
            moneymachine.report()
        else:
            drink = menu.find_drink(drink_name)
            if drink != "":
                if coffeemaker.is_resource_sufficient(drink):
                    if moneymachine.make_payment(drink.cost):
                        coffeemaker.make_coffee(drink)
run_machine()