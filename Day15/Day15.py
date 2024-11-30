'''
Topics to be Covered:
- Coffee machine Project
'''

# 3 Hot Flavours: Espresso(50ml W and 18g C - $1.50), Latte(200ml W 24g C and 150ml M - $2.50), Cappuccino(250ml W 24g C 100ml M - $3.00)
#Resources : 300ml W , 200ml M , 100g C
#Coin Operated: Penny - 1 cent , Nickel - 5 cents , Dime - 10 cents, Quarter - 25 cents

# TO DO -> report(how much resources left), check resources sufficient , Porcess coins, check transaction successful, make coffee , deduct resources.  

resources = {'water': 300, 'milk': 200, 'coffee': 100}

menu = {
    'espresso': {'ingredients': {'water': 50, 'coffee': 18}, 'cost': 1.5},
    'latte': {'ingredients': {'water': 200, 'coffee': 24, 'milk': 150}, 'cost': 2.5},
    'cappuccino': {'ingredients': {'water': 250, 'coffee': 24, 'milk': 200}, 'cost': 3.0}
}

is_on = True
profit = 0

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

def process_coins():
    """Returns the total calculated from coins."""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = menu.get(choice)
        if drink and is_resource_sufficient(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(choice, drink['ingredients'])
        elif not drink:
            print("Invalid choice. Please select a valid option.")