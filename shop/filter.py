import django_filters
from .models import Product

class ProductFilter(django_filters.FilterSet):
    # Add filters based on your requirements
    class Meta:
        model = Product
        fields = {
            'name': ['icontains'],
            'category': ['exact'],
            'seller': ['exact'],
        }
