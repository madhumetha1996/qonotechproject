from django.shortcuts import render
from .models import Seller, Product, Buyer

def seller_list(request):
    sellers = Seller.objects.all()
    return render(request, 'adminpanel/seller_list.html', {'sellers': sellers})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'adminpanel/product_list.html', {'products': products})

def buyer_list(request):
    buyers = Buyer.objects.all()
    return render(request, 'adminpanel/buyer_list.html', {'buyers': buyers})
