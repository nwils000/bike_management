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
-Cancel customer order (5)
-Mark an order as paid (6)
                            
Choose an option: ''')
print(" ")
print("*" * 135)
print(" ")





if user_menu_selection == '1':
    print("All Vehicles: ")
    vehicles = Vehicle.objects.all()
    for vehicle in vehicles:
        print(vehicle)
    print(" ")
    vehicle_type = input('What is the vehicles type? (bicycle, unicycle, or tricycle) ')
    stock = input('How many would you like to add? ')

    try:
        vehicle = Vehicle.objects.get(type=vehicle_type)
        vehicle.number_in_stock += int(stock)
        vehicle.save()
        print(f'''
Added {stock} {vehicle_type}s, 
we now have {str(vehicle.number_in_stock)} total!''')
    except:
        print("Couldn't create vehicle, you did something in wrong...")
    print(" ")
    print("*" * 135)
    print(" ")

if user_menu_selection == '2':
    customers = Customer.objects.all()
    print("All Customers: ")
    for customer in customers:
        print(customer)
    print(" ")
    name_input = input('What is the new customers name? ')
    print(f'''
Added {name_input} to customers!''')
    try:
        customer = Customer(name=name_input)
        customer.save()
    except:
        print("Couldn't create customer, you did something in wrong...")
    print(" ")
    print("*" * 135)
    print(" ")

if user_menu_selection == '3':
    customers = Customer.objects.all()
    print("All Customers: ")
    for customer in customers:
        print(customer)
    print(" ")
    customer = input('Which customer is making an order? (Capitalization matters) ')
    order_id = input("What is your customer ID ")
    vehicle = input("What vehicle are they buying? (bicycle, unicycle, or tricycle) ")
    is_paid = input("Are you paying up front? (Y/N) ").lower()

    if is_paid == "y":
        is_paid = True
    else:
        is_paid = False

    try:
        vehicle_to_add = Vehicle.objects.get(type=vehicle)
        if vehicle_to_add.number_in_stock > 0:
            vehicle_to_add.number_in_stock -= 1
            vehicle_to_add.save()

            customer_to_add = Customer.objects.get(id=order_id, name=customer)
           
            order = Customer_Order(customer = customer_to_add, order = vehicle_to_add, created_date = str(date.today()), paid = is_paid)
            order.save()
            print(f'''
{customer} successfully made an order! Here is your receipt:
{order}''')
        else:
            print("Not enough vehicles in stock to make your order...")          
    except:
        print("Couldn't create customer order, you did something in wrong...")
    print(" ")
    print("*" * 135)
    print(" ")

if user_menu_selection == '4':
    print('\n\n************Full Vehicle Stock************\n')

    try:
        vehicles = Vehicle.objects.all()
        for vehicle in vehicles:
            print(vehicle)
        print("")
    except:
        print("Sorry, we couldn't show you the full stock of vehicles...")
    print(" ")
    print("*" * 135)
    print(" ")

if user_menu_selection == '5':  
    print("All Customer Orders: ")
    customer_orders = Customer_Order.objects.all()
    for order in customer_orders:
        print(order)
    print(' ')
    order_id = input('What is your order ID? ')

    try:
        order = Customer_Order.objects.get(id=order_id)
        order.delete()
        order.order.number_in_stock += 1
        order.order.save()
        print(f'''
successfully deleted order number {order_id}. Here is your receipt:
{order}''')
    except:
        print("Couldn't create customer order, you did something in wrong...")
    print(" ")
    print("*" * 135)
    print(" ")

if user_menu_selection == '6':
    print("All Customer Orders: ")
    customer_orders = Customer_Order.objects.all()
    for order in customer_orders:
        print(order)
    print(' ')
    order_id = input('What is your order ID? ')
    confirm = input("Confirm that you paid for the vehicle (Y/N)").lower()

    if confirm == "y":
        try:
            order = Customer_Order.objects.get(id=order_id)
            order.paid = True
            order.save()
            print(f'''
successfully paid for order number {order_id}. Here is your receipt:
{order}''')
        except:
            print("Couldn't create customer order, you did something in wrong...")
        print(" ")
        print("*" * 135)
        print(" ")

