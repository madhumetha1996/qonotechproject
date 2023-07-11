from django.contrib import admin
from .models import Seller, Category, Product, Order, Cart

admin.site.register(Seller)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Cart)
