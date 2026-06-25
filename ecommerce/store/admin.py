# store/admin.py
from django.contrib import admin

# Importamos directo de cada archivo de la carpeta models
from store.models.products import Products
from store.models.category import Category
from store.models.customer import Customer
from store.models.orders import Order

admin.site.register(Products)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Order)