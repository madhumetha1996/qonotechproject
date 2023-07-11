from django.urls import path
from . import views

app_name = 'adminpanel'

urlpatterns = [
    path('sellers/', views.seller_list, name='seller_list'),
    path('products/', views.product_list, name='product_list'),
    path('buyers/', views.buyer_list, name='buyer_list'),
]
