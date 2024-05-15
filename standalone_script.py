import os
import django
from django.conf import settings

os.environ["DJANGO_SETTINGS_MODULE"] = "bike_project.settings"
django.setup()

print('****** SCRIPT STARTED ******')

from bike_app.models import *

vehicles = Vehicle.objects.all()
customers = Customer.objects.all()
customers_orders = Customer_Order.objects.all()

# Vehicle.objects.bulk_create(
#     [
#         Vehicle(type='bicycle', number_in_stock=5),
#         Vehicle(type='bicycle', number_in_stock=2),
#         Vehicle(type='unicycle', number_in_stock=1),
#         Vehicle(type='tricycle', number_in_stock=8)
#     ]
# )
        
# Customer.objects.bulk_create(
#     [
#         Customer(name="Nathan Wilson"),
#         Customer(name="Emily Johnson"),
#         Customer(name="Michael Smith"),
#         Customer(name="Jessica Taylor"),
#         Customer(name="James Anderson"),
#         Customer(name="Laura White"),
#         Customer(name="Robert Harris"),
#         Customer(name="Sarah Martin")
#     ]
# )

customers_to_add = Customer_Order.objects.all()

for customer in customers_to_add:
    print(customer)
# vehicles_to_add = Vehicle.objects.all()


# Customer_Order.objects.bulk_create(
#     [
#         Customer_Order(customer = customers_to_add[0], order = vehicles_to_add[0], created_date = '5/12/2024', paid = True),
#         Customer_Order(customer = customers_to_add[1], order = vehicles_to_add[1], created_date = '4/3/2024', paid = True),
#         Customer_Order(customer = customers_to_add[2], order = vehicles_to_add[2], created_date = '2/22/2023', paid = True),
#         Customer_Order(customer = customers_to_add[3], order = vehicles_to_add[3], created_date = '12/10/2022', paid = True),
#     ]
# )

# print(vehicles)

# print(customers_orders)





# Vehicle.objects.all().delete()