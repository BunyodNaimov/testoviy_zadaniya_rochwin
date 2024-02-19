from django.contrib import admin

from my_project.models import Employee, Product, Order, Client


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('full_name',)


@admin.register(Client)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('full_name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('client', 'employee', 'price')
