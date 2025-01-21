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

money = 0

while True:
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if order == "off":
        break
    elif order == "report":
        print(f"""Water: {resources["water"]}ml
Milk: {resources["milk"]}ml
Coffee: {resources["coffee"]}g
Money: ${money}""")
    elif order in MENU:
        drink = MENU[order]
        ingredients = drink["ingredients"]

        # Check if resources are sufficient
        can_make = True
        for item in ingredients:
            if ingredients[item] > resources.get(item, 0):
                print(f"Sorry, there is not enough {item}.")
                can_make = False
                break

        # Process transaction if resources are sufficient
        if can_make:
            cost = drink["cost"]
            print(f"The cost of {order} is ${cost}. Please insert coins.")
            quarters = int(input("How many quarters? ")) * 0.25
            dimes = int(input("How many dimes? ")) * 0.10
            nickels = int(input("How many nickels? ")) * 0.05
            pennies = int(input("How many pennies? ")) * 0.01
            total = quarters + dimes + nickels + pennies

            if total >= cost:
                change = round(total - cost, 2)
                if change > 0:
                    print(f"Here is ${change} in change.")
                money += cost
                for item in ingredients:
                    resources[item] -= ingredients[item]
                print(f"Here is your {order}. Enjoy!")
            else:
                print("Sorry, that's not enough money. Money refunded.")
    else:
        print("Invalid selection. Please choose espresso, latte, or cappuccino.")
