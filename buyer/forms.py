from django import forms
from .models import Buyer

class BuyerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Buyer
        fields = ['username', 'email']
