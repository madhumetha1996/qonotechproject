from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.seller_create, name='seller_create'),
    path('list/', views.seller_list, name='seller_list'),
    path('update/<int:pk>/', views.seller_update, name='seller_update'),
    path('detail/<int:pk>/', views.seller_detail, name='seller_detail'),
]
