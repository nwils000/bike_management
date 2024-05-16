import os
import django
from django.conf import settings
from datetime import date

os.environ["DJANGO_SETTINGS_MODULE"] = "bike_project.settings"
django.setup()

from bike_app.models import *

def selections(user_menu_selection):
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
            print("Couldn't create vehicle, you did something wrong...")
        print(" ")
        print("*" * 130)
        print(" ")
        showMenu()

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
            print("Couldn't create customer, you did something wrong...")
        print(" ")
        print("*" * 130)
        print(" ")
        showMenu()

    if user_menu_selection == '3':
        customers = Customer.objects.all()
        print("All Customers: ")
        for customer in customers:
            print(customer)
        print(" ")
        customer = input('Which customer is making an order? (Capitalization matters) ')
        order_id = input("What is your customer ID ")
        vehicles = input("Which vehicle(s) are you buying? bicycle(1), unicycle(2), or tricycle(3)\n (if you are buying more than 1 type of vehicle, type the numbers back to back e.g. (23)) ")
        is_paid = input("Are you paying up front? (Y/N) ").lower()
        if is_paid == "y":
            is_paid = True
        else:
            is_paid = False
        customer_to_add = Customer.objects.get(id=order_id, name=customer)
        new_order = Order(customer=customer_to_add, created_date=str(date.today()), paid=is_paid)
        new_order.save()
        if len(vehicles) <= 3:
            for char in vehicles:
                vehicle = ""
                if char == "1":
                    vehicle = "bicycle"
                elif char == "2":
                    vehicle = "unicycle"
                elif char == "3":
                    vehicle = "tricycle"
                else:
                    print("You did not put in a valid vehicle reference number")
                    showMenu()

                amount_of_type = input(f"How many {vehicle}s do you want to buy? ")

                try:
                    vehicle_to_add = Vehicle.objects.get(type=vehicle)
                    new_order_detail = Order_Detail(order=new_order, vehicle=vehicle_to_add, amount=int(amount_of_type))
                    new_order_detail.save()
                    print(f'''
Successfully added {amount_of_type} {vehicle}s to your order!''')
                except:
                    print("Couldn't create customer order, you did something wrong...")
            print(f'''
{customer}, we successfully created your order! Here is your receipt:
{new_order}''')
            print(" ")
            print("*" * 130)
            print(" ")
            showMenu()
        else:
            print("You selected too many vehicle types")
            showMenu()  

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
        print("*" * 130)
        print(" ")
        showMenu()

    if user_menu_selection == '5':  
        print("All Customer Orders: ")
        orders = Order.objects.all()
        for order in orders:
            print(order)
        print(' ')
        order_id = input('What is your order ID? ')

        try:
            order = Order.objects.get(id=order_id)
            order.delete()
            order.order.number_in_stock += 1
            order.order.save()
            print(f'''
successfully deleted order number {order_id}. Here is your receipt:
{order}''')
        except:
            print("Couldn't create customer order, you did something wrong...")
        print(" ")
        print("*" * 130)
        print(" ")
        showMenu()

    if user_menu_selection == '6':
        print("All Customer Orders: ")
        orders = Order.objects.all()
        for order in orders:
            print(order)
        print(' ')
        order_id = input('What is your order ID? ')
        confirm = input("Confirm that you paid for the vehicle (Y/N)").lower()

        if confirm == "y":
            try:
                order = Order.objects.get(id=order_id)
                order.paid = True
                order.save()
                print(f'''
successfully paid for order number {order_id}. Here is your receipt:
{order}''')
            except:
                print("Couldn't create customer order, you did something wrong...")
            print(" ")
            print("*" * 130)
            print(" ")
            showMenu()
    
def showMenu():
    user_menu_selection = input('''\n\t\t***************MENU***************

    \t\t-Add vehicle to database (1)
    \t\t-Add new customer (2)
    \t\t-Make a new order (3)
    \t\t-Display Inventory (4)
    \t\t-Cancel customer order (5)
    \t\t-Mark an order as paid (6)
        
    \t\tChoose an option: ''')
    print(" ")
    print("*" * 130)
    print(" ")
    selections(user_menu_selection)

        
showMenu()

