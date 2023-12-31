from django.shortcuts import render, get_object_or_404
from .models import Order
from .forms import OrderForm

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'orders/order_list.html', {'orders': orders})

def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(request, 'orders/order_detail.html', {'order': order})

def order_create(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            # Add any additional logic or redirect
    else:
        form = OrderForm()
    return render(request, 'orders/order_create.html', {'form': form})

def order_update(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            # Add any additional logic or redirect
    else:
        form = OrderForm(instance=order)
    return render(request, 'orders/order_update.html', {'form': form})

def order_statistics(request):
    # Implement logic to calculate order statistics
    return render(request, 'orders/order_statistics.html')
