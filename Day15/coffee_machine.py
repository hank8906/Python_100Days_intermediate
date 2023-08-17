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

ask_for_drink = input('What would you like? (espresso/latte/cappuccino): ')

# Turn off the coffee machine
if ask_for_drink == "off":
    exit()
elif ask_for_drink == "report":
    print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: $0")

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


print("Please insert coins.")

quarters = input("how many quarters?: ")
dimes = input("how many dimes?: ")
nickles = input("how many nickles?: ")
pennies = input("how many pennies?: ")



