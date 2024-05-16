import os
import django
from django.conf import settings
from datetime import date
from colorama import Fore, Style, init
import time

init(autoreset=True)

os.environ["DJANGO_SETTINGS_MODULE"] = "bike_project.settings"
django.setup()

from bike_app.models import *

def selections(user_menu_selection):
    if user_menu_selection == '1':
        print(Fore.YELLOW + "\n\tAll Vehicles:\n")
        vehicles = Vehicle.objects.all()
        for vehicle in vehicles:
            print(f"\t{vehicle}")
        print("\n")
        vehicle_type = input(Fore.CYAN + Style.BRIGHT + '\tWhat is the vehicle type? bicycle(1), unicycle(2), or tricycle(3): ')
        print("")
        stock = input(Fore.CYAN + Style.BRIGHT + '\tHow many would you like to add? ')

        try:
            vehicle_name = ""
            if vehicle_type == "1":
                vehicle_name = "bicycle"
            elif vehicle_type == "2":
                vehicle_name = "unicycle"
            elif vehicle_type == "3":
                vehicle_name = "tricycle"
            else:
                print(Fore.RED + "\tYou did not put in a valid vehicle reference number.")
                time.sleep(1)
                showMenu()
            vehicle = Vehicle.objects.get(type=vehicle_name)
            vehicle.number_in_stock += int(stock)
            vehicle.save()
            print(Fore.GREEN + f'''\n\tAdded {stock} {vehicle_name}(s),
            we now have {str(vehicle.number_in_stock)} total!''')
        except:
            print(Fore.RED + "\tCouldn't create vehicle, you did something wrong...")
        print(Fore.WHITE + Style.DIM + "\n" + "*" * 38 + "\n")
        time.sleep(1)
        showMenu()

    if user_menu_selection == '2':
        customers = Customer.objects.all()
        print(Fore.YELLOW + "\n\tAll Customers:\n")
        for customer in customers:
            print(f"\t{customer}")
        print("\n")
        name_input = input(Fore.CYAN + Style.BRIGHT + '\tWhat is the new customer\'s name? ')
        print(Fore.GREEN + f'''\n\tAdded {name_input} to customers!''')
        try:
            customer = Customer(name=name_input)
            customer.save()
        except:
            print(Fore.RED + "\tCouldn't create customer, you did something wrong...")
        print(Fore.WHITE + Style.DIM + "\n" + "*" * 38 + "\n")
        time.sleep(1)
        showMenu()

    if user_menu_selection == '3':
        customers = Customer.objects.all()
        print(Fore.YELLOW + "\n\tAll Customers:\n")
        for customer in customers:
            print(f"\t{customer}")
        print("\n")
        customer = input(Fore.CYAN + Style.BRIGHT + '\tWhich customer is making an order? (Capitalization matters): ')
        print("")
        order_id = input(Fore.CYAN + Style.BRIGHT + "\tWhat is your customer ID: ")
        print("")
        vehicles = input(Fore.CYAN + Style.BRIGHT + "\tWhich vehicle(s) are you buying? bicycle(1), unicycle(2), or tricycle(3)\n\t(if you are buying more than 1 type of vehicle, type the numbers back to back e.g., (123)): ")
        print("")
        is_paid = input(Fore.CYAN + Style.BRIGHT + "\tAre you paying up front? (Y/N): ").lower()
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
                emoji = ""
                if char == "1":
                    vehicle = "bicycle"
                    emoji = print(Fore.RED + '''                                             
              d$$$$$$$P"                  $    J
                  ^$.                     4r  "
                  d"b                    .db
                 P   $                  e" $
        ..ec.. ."     *.              zP   $.zec..
    .^        3*b.     *.           .P" .@"4F      "4
  ."         d"  ^b.    *c        .$"  d"   $         %
 /          P      $.    "c      d"   @     3r         3
4        .eE........$r===e$$$$eeP    J       *..        b
$       $$$$$       $   4$$$$$$$     F       d$$$.      4
$       $$$$$       $   4$$$$$$$     L       *$$$"      4
4         "      ""3P ===$$$$$$"     3                  P
 *                 $       """        b                J
  ".             .P                    %.             @
    %.         z*"                      ^%.        .r"
       "*==*""                             ^"*==*""   ''')
                elif char == "2":
                    vehicle = "unicycle"
                    emoji = print(Fore.RED + '''                                             
                       -   ,--_--.
               -           \      `.
                      -     "-_ _   |
     -                         / F   )
                   -     -    / / `--'
              -              / /
                   -        / /
            -            __/ /
                        /,-pJ
           -        _--"-L ||
                  ,"      "//
     -           /  ,-""".//|
                /  /     // J____
               J  /     // L/----|
   .           F J     //__//^---'
     `     ___J  F    '----| |
  `       J---|  F         F F
`   `. `   `--J  L        J  F
    .   .`     L J       J  F
       .  .    J  \    ,"  F
         .  `.` \  "--"  ,"
            ` ``."-____-"                  ''')
                elif char == "3":
                    vehicle = "tricycle"
                    emoji = print(Fore.RED + '''                                             
      __o
   _ _\\<_ _
  (_)/(_)/(_)
''')
                else:
                    print(Fore.RED + "\tYou did not put in a valid vehicle reference number.")
                    time.sleep(1)
                    showMenu()
                emoji
                amount_of_type = input(Fore.CYAN + Style.BRIGHT + f"\n\tHow many {vehicle}(s) do you want to buy? ")

                try:
                    vehicle_to_add = Vehicle.objects.get(type=vehicle)
                    new_order_detail = Order_Detail(order=new_order, vehicle=vehicle_to_add, amount=int(amount_of_type))
                    new_order_detail.save()
                    print(Fore.GREEN + f'''\n\tAdded {amount_of_type} {vehicle}(s) to your order!''')
                except:
                    print(Fore.RED + "\tCouldn't create customer order, you did something wrong...")
            print(Fore.GREEN + f'''\n\tOrder processed successfully! Here is your receipt:
            \t{new_order}''')
            print(Fore.WHITE + Style.DIM + "\n" + "*" * 38 + "\n")
            time.sleep(1)
            showMenu()
        else:
            print(Fore.RED + "\tYou selected too many vehicle types.")
            time.sleep(1)
            showMenu()  

    if user_menu_selection == '4':
        print(Fore.YELLOW + '\n\t************Full Vehicle Stock************\n')

        try:
            vehicles = Vehicle.objects.all()
            for vehicle in vehicles:
                print(f"\t{vehicle}")
            print("\n")
        except:
            print(Fore.RED + "\tSorry, we couldn't show you the full stock of vehicles...")
        print(Fore.WHITE + Style.DIM + "\n" + "*" * 38 + "\n")
        time.sleep(1)
        showMenu()

    if user_menu_selection == '5':  
        print(Fore.YELLOW + "\n\tAll Customer Orders:\n")
        orders = Order.objects.all()
        for order in orders:
            print(f"\t{order}")
        print('\n')
        order_id = input(Fore.CYAN + Style.BRIGHT + '\tWhat is your order ID? ')

        try:
            order = Order.objects.get(id=order_id)
            print(Fore.GREEN + f'''\n\tSuccessfully deleted order number {order_id}. Here is your receipt:
            \t{order}''')
            for detail in order.order_detail_set.all():
                vehicle = detail.vehicle
                vehicle.number_in_stock += detail.amount
                vehicle.save()
            order.delete()
        except:
            print(Fore.RED + "\tSorry we couldn't delete your order, you did something wrong...")
        print(Fore.WHITE + Style.DIM + "\n" + "*" * 38 + "\n")
        time.sleep(1)
        showMenu()

    if user_menu_selection == '6':
        print(Fore.YELLOW + "\n\tAll Customer Orders:\n")
        orders = Order.objects.all()
        for order in orders:
            print(f"\t{order}")
        print('\n')
        order_id = input(Fore.CYAN + Style.BRIGHT + '\tWhat is your order ID? ')
        confirm = input(Fore.CYAN + Style.BRIGHT + "\tConfirm that you paid for the vehicle (Y/N): ").lower()

        if confirm == "y":
            try:
                order = Order.objects.get(id=order_id)
                order.paid = True
                order.save()
                print(Fore.GREEN + f'''\n\tSuccessfully paid for order number {order_id}. Here is your receipt:
                \t{order}''')
            except:
                print(Fore.RED + "\tCouldn't create customer order, you did something wrong...")
            print(Fore.WHITE + Style.DIM + "\n" + "*" * 38 + "\n")
            time.sleep(1)
            showMenu()
    
def showMenu():
    print(Fore.YELLOW + """\n*****************MENU*****************""")
    print(Style.BRIGHT + '''
    -Add vehicle to database (1)
    -Add new customer (2)
    -Make a new order (3)
    -Display Inventory (4)
    -Cancel customer order (5)
    -Mark an order as paid (6)
                              ''')
    user_menu_selection = input(Fore.CYAN + Style.BRIGHT + "Choose an option: ")
    print(Fore.WHITE + Style.DIM + "\n" + "*" * 38 + "\n")
    time.sleep(1)
    selections(user_menu_selection)

showMenu()
