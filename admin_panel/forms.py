from django import forms
from .models import Seller, Product, Buyer

class SellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = '__all__'

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class BuyerForm(forms.ModelForm):
    class Meta:
        model = Buyer
        fields = '__all__'
