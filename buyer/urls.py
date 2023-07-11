from django.urls import path
from . import views

app_name = 'buyer'

urlpatterns = [
    path('create/', views.create_buyer, name='create'),
    path('update/<int:pk>/', views.update_buyer, name='update'),
    path('detail/<int:pk>/', views.detail_buyer, name='detail'),
    path('list/', views.list_buyer, name='list'),
]
