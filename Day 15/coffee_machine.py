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

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def machine_report():
    """
    prints a report of the current resources
    """
    for resource in resources:
        print(f"{resource}: {resources[resource]}")
    print(f"Profit: ${profit}")

def make_coffee(drink_name):
    """
    2nd level function to make coffee; first checks available resources,
    second processes payment, third makes coffee
    :param drink_name:
    :return:
    """

    if resources_deduct(drink_name, False):
        if process_payment(drink_name):
            resources_deduct(drink_name, True)
            print(f"Here is your {drink_name}. Enjoy!")

def process_payment(drink_name):
    """
    User inserts payment, check if sufficient and deduct, return boolean for sufficient payment
    :param drink_name:
    :return:
    """
    paid_amount = 0
    cost = MENU[drink_name]["cost"]
    print(f"{drink_name} costs {cost}. Please insert coins.")
    quarter = input("how many quarters?")
    dime = input("how many dimes?")
    nickle = input("how many nickels?")
    penny = input("how many pennies?")
    coins = {
        quarter: 0.25,
        dime: 0.10,
        nickle: 0.05,
        penny: 0.01,
    }
    for coin in coins:
        paid_amount += float(coin) * coins[coin]
    global profit
    if paid_amount >= cost:
        profit += cost

        change = round(paid_amount - cost,2)
        if change > 0:
            print(f"Here is {change} in change.")
            
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def resources_deduct(drink_name, deduct):
    """
    check if sufficient resources and deduct if deduct boolean instruction is true
    :param drink_name:
    :param deduct:
    :return:
    """
    for ingredient in MENU[drink_name]["ingredients"]:
        if resources[ingredient] >= MENU[drink_name]["ingredients"][ingredient]:
            if deduct:
                resources[ingredient] -= MENU[drink_name]["ingredients"][ingredient]
            else:
                return True
        else:
            print(f"Sorry there is not enough {ingredient}.")
            return False

def run_machine():
    """
    top level function to run coffee machine
    """
    machine_on = True
    while machine_on:
        drink_name = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if drink_name == "off":
            machine_on = False
        elif drink_name == "report":
            machine_report()
        else:
            make_coffee(drink_name)

run_machine()