from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('admin/', views.admin_dashboard, name='admin_dashboard'),
    path('shipping/', views.shipping_dashboard, name='shipping_dashboard'),
]
