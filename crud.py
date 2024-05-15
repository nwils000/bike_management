# Customer_Order.objects.bulk_create(
#     [
#         Customer_Order(customer = customers_to_add[0], order = vehicles_to_add[0], created_date = '5/12/2024', paid = True),
#         Customer_Order(customer = customers_to_add[1], order = vehicles_to_add[1], created_date = '4/3/2024', paid = True),
#         Customer_Order(customer = customers_to_add[2], order = vehicles_to_add[2], created_date = '2/22/2023', paid = True),
#         Customer_Order(customer = customers_to_add[3], order = vehicles_to_add[3], created_date = '12/10/2022', paid = True),
#     ]
# )

# the_customer = Customer.objects.get(name="Nathan Wilson")
# the_customer.name = "Bob Wilson"
# the_customer.save()

# Vehicle.objects.all().delete()