from django.db import models

class Vehicle(models.Model):
    type = models.CharField(max_length=100)
    number_in_stock = models.PositiveIntegerField()
    def __str__(self):
        return f'type: {self.type}, number_in_stock: {self.number_in_stock}'

class Customer(models.Model):
    name = models.CharField(max_length=60)
    def __str__(self):
        return f'name: {self.name}'

class Customer_Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    created_date = models.CharField(max_length=100)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f'customer: {self.customer}, order: {self.order}, created_date: {self.created_date}, paid: {self.paid}'