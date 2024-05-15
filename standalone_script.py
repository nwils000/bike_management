import os
import django
from django.conf import settings

os.environ["DJANGO_SETTINGS_MODULE"] = "bike_project.settings"
django.setup()

from bike_app.models import *

user_menu_selection = input('''\n\n************MENU************
-Add vehicle to database (1)
-Add new customer (2)
-Make a new order (3)
-Display Inventory (4)
                            
Choose an option: ''')

print(Customer.objects.all())

if user_menu_selection == '1':
    vehicle_type = input('What is the vehicles type? (bicycle, unicycle, or tricycle) ')
    stock = input('How many would you like to add? ')
    try:
        vehicle = Vehicle.objects.get(type=vehicle_type)
        vehicle.number_in_stock += int(stock)
        vehicle.save()
    except:
        "You typed something in wrong..."

if user_menu_selection == '2':
    name_input = input('What is the customers name? ')
    try:
        customer = Customer(name=name_input)
        customer.save()
    except:
        "You typed something in wrong..."


print(Customer.objects.all())
