from django.urls import path
from . import views

urlpatterns = [
    path('store/<str:category>/', views.api_store, name='api-store'),
    path('product/<int:id>/', views.api_product, name='api-product'),
    path('inventory/', views.api_inventory, name='api-inventory'),
]
