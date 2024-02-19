from django.db import models
from django.db.models import Sum


class Employee(models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    middle_name = models.CharField(max_length=55)
    birth_of_date = models.DateField()

    def full_name(self):
        return f"{self.first_name} {self.last_name} {self.middle_name}"

    def __str__(self):
        return self.full_name()


class Client(models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    middle_name = models.CharField(max_length=55)
    birth_of_date = models.DateField()

    def full_name(self):
        return f"{self.first_name} {self.last_name} {self.middle_name}"

    def __str__(self):
        return self.full_name()


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='orders')
    products = models.ManyToManyField(Product)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    @property
    def total_price(self):
        return self.products.aggregate(total=Sum('price')).get('total' or 0) or 0

    def __str__(self):
        return f"Order {self.client}, Date {self.date}"
