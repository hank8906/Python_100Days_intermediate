from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# initiate object
menu = Menu()

latte = MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5)
espresso = MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5)
cappuccino = MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3)

coffeeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()


def coffee_machine():
    # first question

    ask_for_drink = input(f'What would you like? {menu.get_items()}: ')
    menu.find_drink(ask_for_drink)

    # Turn off the coffee machine

    if ask_for_drink == "off":
        exit()

    # Print report

    elif ask_for_drink == "report":
        coffeeMaker.report()
        moneyMachine.report()

    # Check resources sufficient
    # Process coins and Check transaction successful
    # report before and after the order

    elif ask_for_drink == "latte":
        if coffeeMaker.is_resource_sufficient(latte):
            moneyMachine.make_payment(latte.cost)
            coffeeMaker.report()
            moneyMachine.report()
            coffeeMaker.make_coffee(latte)
            coffeeMaker.report()
            moneyMachine.report()
            coffee_machine()
        else:
            coffee_machine()

    elif ask_for_drink == "espresso":
        if coffeeMaker.is_resource_sufficient(espresso):
            moneyMachine.make_payment(espresso.cost)
            coffeeMaker.report()
            moneyMachine.report()
            coffeeMaker.make_coffee(espresso)
            coffeeMaker.report()
            moneyMachine.report()
            coffee_machine()
        else:
            coffee_machine()

    elif ask_for_drink == "cappuccino":
        if coffeeMaker.is_resource_sufficient(cappuccino):
            moneyMachine.make_payment(cappuccino.cost)
            coffeeMaker.report()
            moneyMachine.report()
            coffeeMaker.make_coffee(cappuccino)
            coffeeMaker.report()
            moneyMachine.report()
            coffee_machine()
        else:
            coffee_machine()


# start the program
coffee_machine()






