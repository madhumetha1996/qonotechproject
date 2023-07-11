from django.shortcuts import render, redirect
from .models import Seller
from .forms import SellerForm

def seller_create(request):
    if request.method == 'POST':
        form = SellerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('seller_list')
    else:
        form = SellerForm()
    return render(request, 'seller/create.html', {'form': form})

def seller_list(request):
    sellers = Seller.objects.all()
    return render(request, 'seller/list.html', {'sellers': sellers})

def seller_update(request, pk):
    seller = Seller.objects.get(pk=pk)
    if request.method == 'POST':
        form = SellerForm(request.POST, instance=seller)
        if form.is_valid():
            form.save()
            return redirect('seller_list')
    else:
        form = SellerForm(instance=seller)
    return render(request, 'seller/update.html', {'form': form, 'seller': seller})

def seller_detail(request, pk):
    seller = Seller.objects.get(pk=pk)
    return render(request, 'seller/detail.html', {'seller': seller})
