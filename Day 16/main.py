from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def run_machine():
    """
    top level function to run coffee machine
    """
    machine_on = True
    coffee_maker = CoffeeMaker()
    menu = Menu()
    money_machine = MoneyMachine()
    while machine_on:
        print(menu.get_items())
        drink_name = input("Select an item from the menu: ").lower()
        if drink_name == "off":
            machine_on = False
        elif drink_name == "report":
            coffee_maker.report()
            money_machine.report()
        else:
            drink = menu.find_drink(drink_name)
            if drink is not None:
                if coffee_maker.is_resource_sufficient(drink):
                    if money_machine.make_payment(drink.cost):
                        coffee_maker.make_coffee(drink)
run_machine()