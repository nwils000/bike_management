import os
import django
from django.conf import settings
from datetime import date

os.environ["DJANGO_SETTINGS_MODULE"] = "bike_project.settings"
django.setup()

from bike_app.models import *

user_menu_selection = input('''\n\n************MENU************
-Add vehicle to database (1)
-Add new customer (2)
-Make a new order (3)
-Display Inventory (4)
                            
Choose an option: ''')

print(Customer_Order.objects.all())

if user_menu_selection == '1':
    vehicle_type = input('What is the vehicles type? (bicycle, unicycle, or tricycle) ')
    stock = input('How many would you like to add? ')
    try:
        vehicle = Vehicle.objects.get(type=vehicle_type)
        vehicle.number_in_stock += int(stock)
        vehicle.save()
    except:
        print("Couldn't create vehicle, you typed something in wrong...")

if user_menu_selection == '2':
    name_input = input('What is the customers name? ')
    try:
        customer = Customer(name=name_input)
        customer.save()
    except:
        print("Couldn't create customer, you typed something in wrong...")


if user_menu_selection == '3':
    customer = input('Which customer is making an order? (Capitalization matters) ')
    vehicle = input("What vehicle are they buying? (bicycle, unicycle, or tricycle) ")
    is_paid = input("Are you paying up front? (Y/N)")

    if is_paid == "Y":
        is_paid = True
    else:
        is_paid = False

    try:
        customer_to_add = Customer.objects.get(name=customer)
        vehicle_to_add = Vehicle.objects.get(type=vehicle)
        order = Customer_Order(customer = customer_to_add, order = vehicle_to_add, created_date = str(date.today()), paid = is_paid)
        order.save()
    except:
        print("Couldn't create customer order, you typed something in wrong...")

if user_menu_selection == '4':
    print('\n\n************Full Vehicle Stock************\n')
    try:
        vehicles = Vehicle.objects.all()
        for vehicle in vehicles:
            print(vehicle)
        print("")
    except:
        print("Sorry, we couldn't show you the full stock of vehicles...")
