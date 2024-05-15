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

customer = Customer.objects.get(name = "Nathan Wilson")

# Customer_Order.objects.bulk_create(
#     [

#     ]
# )

# print(vehicles)
print(customer)
# print(customers_orders)





# Vehicle.objects.all().delete()