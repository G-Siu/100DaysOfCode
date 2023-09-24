from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffee = CoffeeMaker()
money = MoneyMachine()


def process():
    # Keep running until off
    on = True
    while on:
        # Prompt user for an input
        order = input(f"What would you like? {menu.get_items()}: ").lower()
        # Turns machine off
        if order == "off":
            on = False
        # Prints resources available in machine
        elif order == "report":
            coffee.report()
            money.report()
        # Check selection exists in menu
        else:
            drink = menu.find_drink(order)
            # Check resources available
            if coffee.is_resource_sufficient(drink) and money.make_payment(drink.cost):
                coffee.make_coffee(drink)


def main():
    process()


main()
