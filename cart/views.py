from django.shortcuts import render, get_object_or_404, redirect
from .models import Cart
from .forms import CartForm

def cart_list(request):
    carts = Cart.objects.all()
    return render(request, 'cart_list.html', {'carts': carts})

def cart_detail(request, pk):
    cart = get_object_or_404(Cart, pk=pk)
    return render(request, 'cart_detail.html', {'cart': cart})

def cart_create(request):
    if request.method == 'POST':
        form = CartForm(request.POST)
        if form.is_valid():
            cart = form.save()
            return redirect('cart_detail', pk=cart.pk)
    else:
        form = CartForm()
    return render(request, 'cart_create.html', {'form': form})

def cart_update(request, pk):
    cart = get_object_or_404(Cart, pk=pk)
    if request.method == 'POST':
        form = CartForm(request.POST, instance=cart)
        if form.is_valid():
            cart = form.save()
            return redirect('cart_detail', pk=cart.pk)
    else:
        form = CartForm(instance=cart)
    return render(request, 'cart_update.html', {'form': form})
