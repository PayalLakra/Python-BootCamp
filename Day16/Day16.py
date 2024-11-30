'''
Topics to be Covered:
- OOPS - Classes, Objects
- Python Packages
'''

# OBJECT has : Attribute -> These are the variables belonging to an object or class and containing information about their properties or characteristics.
#              Methods -> These are the functions that belong to an object or class and are designed to perform actions involving the object's attributes.
# Example: car()

# CLASS : It is a template for creating objects that have similar properties and methods.
# Example: CarBluePrint()

from turtle import Turtle, Screen

# Object = Class()
jimmy =  Turtle()
print(jimmy)
jimmy.shape("turtle")        # Call shape method
jimmy._color("red")
jimmy.forward(200)
my_screen = Screen()         # Here also my_screen is a object & Screen is a class

# Object.attribute
my_screen.canvheight         # my_screen is object and after dot canvheight is the attribute of the object.
my_screen.canvwidth

# Object.method()
# my_screen.clear()          # my_screen is object and after dot clear is a method
my_screen.exitonclick()


#Packages - prettytable -> dispalys tabular data in ASCII format

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Name", ["A","B","C"])
table.add_column("Age", ["12","13","14"])

table.align = "l"    #By default table is centered aligned and now we change it to left aligned.
print(table)



# COFEE MACHINE - Using OOP

#Program Requirements - print report, check resources, process coins, check transaction successful, make coffee

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options})")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)