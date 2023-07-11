from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_list, name='cart_list'),
    path('<int:pk>/', views.cart_detail, name='cart_detail'),
    path('create/', views.cart_create, name='cart_create'),
    path('<int:pk>/update/', views.cart_update, name='cart_update'),
]
