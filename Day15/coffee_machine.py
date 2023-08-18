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
    "money": 0
}


# calculate resource and money, then return them
def machine_calculate(drink):
    if drink == "espresso":
        resources['water'] -= MENU['espresso']['ingredients']['water']
        resources['coffee'] -= MENU['espresso']['ingredients']['coffee']
        resources['money'] += MENU['espresso']['cost']
    elif drink == "latte":
        resources['water'] -= MENU['latte']['ingredients']['water']
        resources['coffee'] -= MENU['latte']['ingredients']['coffee']
        resources['milk'] -= MENU['latte']['ingredients']['milk']
        resources['money'] += MENU['latte']['cost']
    elif drink == "cappuccino":
        resources['water'] -= MENU['cappuccino']['ingredients']['water']
        resources['coffee'] -= MENU['cappuccino']['ingredients']['coffee']
        resources['milk'] -= MENU['cappuccino']['ingredients']['milk']
        resources['money'] += MENU['cappuccino']['cost']
    return resources


# report the resource
def machine_report():
    print(
        f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\n"
        f"Coffee: {resources['coffee']}g"f"\nMoney: ${resources['money']}")


# coffee_machine
def coffee_machine():
    # first question
    ask_for_drink = input('What would you like? espresso($1.5)/ latte($2.5)/ cappuccino($3.0): ')

    # Turn off the coffee machine

    if ask_for_drink == "off":
        exit()
    elif ask_for_drink == "report":
        machine_report()

    # Check resources sufficient

    elif ask_for_drink == "espresso":
        if resources['water'] < MENU['espresso']['ingredients']['water']:
            print("Sorry there is not enough water.")
        elif resources['coffee'] < MENU['espresso']['ingredients']['coffee']:
            print("Sorry there is not enough coffee.")

    elif ask_for_drink == "latte":
        if resources['water'] < MENU['latte']['ingredients']['water']:
            print("Sorry there is not enough water.")
        elif resources['coffee'] < MENU['latte']['ingredients']['coffee']:
            print("Sorry there is not enough coffee.")
        elif resources['milk'] < MENU['latte']['ingredients']['milk']:
            print("Sorry there is not enough milk.")

    elif ask_for_drink == "cappuccino":
        if resources['water'] < MENU['cappuccino']['ingredients']['water']:
            print("Sorry there is not enough water.")
        elif resources['coffee'] < MENU['cappuccino']['ingredients']['coffee']:
            print("Sorry there is not enough coffee.")
        elif resources['milk'] < MENU['cappuccino']['ingredients']['milk']:
            print("Sorry there is not enough milk.")

    # Process coins

    print("Please insert coins.")

    quarters = int(input("how many quarters(0.25)?: "))
    dimes = int(input("how many dimes(0.1)?: "))
    nickles = int(input("how many nickles(0.05)?: "))
    pennies = int(input("how many pennies(0.01)?: "))

    total_money = (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)

    # Check transaction successful

    if total_money < MENU[ask_for_drink]['cost']:
        print("Sorry that's not enough money. Money refunded")

        # ask for another drink
        ask_another_drink = input("Do you want another drink?Enter 'y' to keep ordering or any key to exit: ")
        if ask_another_drink == "Y" or ask_another_drink == "y":
            coffee_machine()
        else:
            exit()

    else:
        # show change
        change = float(total_money - MENU[ask_for_drink]['cost'])
        print(f"Here is ${change} dollars in change")

        # show the original report
        print("report before purchasing latte:")
        machine_report()

        # show the finial report
        machine_calculate(ask_for_drink)
        print("report after purchasing latte:")
        machine_report()

        # ask for another drink
        ask_another_drink = input("Do you want another drink?Enter 'y' to keep ordering or any key to exit: ")
        if ask_another_drink == "Y" or ask_another_drink == "y":
            coffee_machine()
        else:
            exit()


# start program
coffee_machine()
