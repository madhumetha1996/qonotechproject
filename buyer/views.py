from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import BuyerRegistrationForm
from .models import Buyer

@login_required
def create_buyer(request):
    if request.method == 'POST':
        form = BuyerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('buyer:list')
    else:
        form = BuyerRegistrationForm()
    return render(request, 'buyer/create.html', {'form': form})

@login_required
def update_buyer(request, pk):
    buyer = Buyer.objects.get(pk=pk)
    if request.method == 'POST':
        form = BuyerRegistrationForm(request.POST, instance=buyer)
        if form.is_valid():
            form.save()
            return redirect('buyer:list')
    else:
        form = BuyerRegistrationForm(instance=buyer)
    return render(request, 'buyer/update.html', {'form': form, 'buyer': buyer})

@login_required
def detail_buyer(request, pk):
    buyer = Buyer.objects.get(pk=pk)
    return render(request, 'buyer/detail.html', {'buyer': buyer})

@login_required
def list_buyer(request):
    buyers = Buyer.objects.all()
    return render(request, 'buyer/list.html', {'buyers': buyers})
