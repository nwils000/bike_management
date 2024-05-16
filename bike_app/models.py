from django.db import models

# Class that represents each type of vehicle and how many we have in stock
class Vehicle(models.Model):
    type = models.CharField(max_length=100)
    number_in_stock = models.PositiveIntegerField()
    def __str__(self):
        return f'type: {self.type}, number_in_stock: {self.number_in_stock}'

# Class that represents each customer
class Customer(models.Model):
    name = models.CharField(max_length=60)
    def __str__(self):
        return f'id: {self.id}, name: {self.name}'

# Class that represents the customers order
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    # order_details is telling Django that every order can have many details (the vehicle and amount)
    # Through is telling django that Order_Detail will serve as an intermediary class to connect Vehicles to the order

    # Order can have many types of vehicles, each type of vehicle can have many orders
    order_details = models.ManyToManyField(Vehicle, through="Order_Detail")
    created_date = models.CharField(max_length=100)
    paid = models.BooleanField(default=False)

    def the_details(self):
            details = []
            for detail in self.order_detail_set.all():
                details.append(f"{detail.amount} {detail.vehicle.type}s")
            return " | ".join(details)

    def __str__(self):
        return f'''
            Name: {self.customer.name}
            Order ID: {self.id}
            Date: {self.created_date}
            Paid: {"Yes" if self.paid else "No"}
            Vehicle(s): {self.the_details()}'''

# Class that represents order details for each type of bike they purchased in their single order
class Order_Detail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True,) 
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, null=True) 
    amount = models.PositiveIntegerField()

    def __str__(self):
        return f'id: {self.id}, order id: {self.order.id}, vehicle: {self.vehicle.type}, Qqantity: {self.quantity}'