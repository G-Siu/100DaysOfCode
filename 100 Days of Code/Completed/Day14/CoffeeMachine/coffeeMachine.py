import sys
import report


def off():
    """Check input to decide further action."""
    print("Turning off.")
    sys.exit(0)


def resources_check(choice):
    print("Please insert coins.")
    resources_remaining = report.resources
    recipe = report.MENU[choice]["ingredients"]
    for resource in recipe:
        if not resources_remaining[resource] / recipe[resource] >= 1:
            print(f"Sorry, there is not enough {resource}")
            return False
    return True


def coins(choice):
    price = report.MENU[choice]["cost"]
    # Quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    """Calculate coins inserted"""
    total = (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)
    return total, price


def coins_check(total, price):
    """If check determines enough resources, prompt user for coins"""
    """Check coins inserted is enough to purchase drink"""
    if total < price:
        print(f"Sorry, that's not enough money. Money refunded.")
        return False
    else:
        return True


def inside_machine():
    """If user types 'report' in prompt, report should be shown with current resources available"""
    for stored in report.resources:
        if stored == "water" or stored == "milk":
            print(f"{stored}: {report.resources[stored]} ml")
        elif stored == "coffee":
            print(f"{stored}: {report.resources[stored]} g")
        else:
            print(f"{stored}: ${report.resources[stored]}")


def coffee(choice):
    recipe = report.MENU[choice]["ingredients"]
    for stored in recipe:
        report.resources[stored] -= recipe[stored]
    return report.resources


while True:
    selection = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if selection == "off":  # Ends execution after 'off' is typed
        off()
    elif selection == "report":
        inside_machine()
    # After user chooses drink, it should check if resources are available to make drink
    elif selection == "espresso" or selection == "latte" or selection == "cappuccino":
        if resources_check(selection):
            total_coins, cost = coins(selection)
            if coins_check(total_coins, cost):
                report.resources["money"] = cost
                # The machine should add the cost to report if it was profit and return change if too much inserted.
                if total_coins > cost:
                    # The change should round to 2 decimal points.
                    print(f"Here is ${give_back:.2f} in change.")
                report.resources = coffee(selection)
                print(f"Here is your {selection} ☕. Enjoy!")
                # Serve next customer by looping again
                continue
            else:
                continue
        else:
            continue
