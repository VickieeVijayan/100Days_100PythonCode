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
    "water": 1000,
    "milk": 1000,
    "coffee": 500,
}

profit = 0

def money():
    """Take the coin and validates whether coins are sufficient for the drink. If sufficient money is inserted,
    function moves on to resource deduction"""
    redo = True
    while redo:
        print("Please insert coins.")
        quarter = 0.25 * int(input("How many quarters =  "))
        dimes = 0.1 * int(input("How many dimes =  "))
        nickles = 0.05 * int(input("How many nickles =  "))
        pennies = 0.01 * int(input("How many pennies =  "))

        total_money = quarter + dimes + nickles + pennies
        total_money = round(total_money, 2)
        a_cost = drink["cost"]
        if total_money > a_cost:
            print(f"Here is ${round(total_money - a_cost, 2)} in change.")
            global profit
            profit += a_cost
            resource_deduction()
            redo = False
        elif total_money < a_cost:
            print(f"Sorry ${total_money} not enough money as drink cost is ${a_cost}. Money is refunded. ReDo")

def res_compare():
    """Checks whether there is sufficient resources to prepare the user choice's drink."""
    for item in drink["ingredients"]:
        if resources[item] < drink["ingredients"][item]:
            print(f"Sorry there is not enough {item}")
            return False
        else:
            return True

def resource_deduction():
    """deduct user's drink resources from actual resource left and provides the drink to user."""
    for ingredients in drink["ingredients"]:
        resources[ingredients] -= drink["ingredients"][ingredients]
    print(f"Here is your {choice}🍵🍵. Enjoy!")
    return resources

def report():
    """Provides latest resource report"""
    for each in resources:
        print(f"{each}: {resources[each]}")
    print(f"Money: ${profit}")

prompt = False
while not prompt:
    choice = input("What would you like? (espresso/latte/cappuccino):  ").lower()
    if choice == "report":
        report()
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        drink = MENU[choice]
        if res_compare():
            money()
    elif choice == "off":
        prompt = True
    else:
        print("Kindly select drink from the given option.")

