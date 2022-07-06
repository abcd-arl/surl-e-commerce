from django.urls import path
from . import views

urlpatterns = [
    path('store/<str:category>/', views.api_store, name='api-store'),
    path('product/<int:id>/', views.api_product, name='api-product'),
    path('inventory/', views.api_inventory, name='api-inventory'),
    path('notify/', views.api_notify, name='api-notify'),
    path('purchase/', views.api_purchase, name='api-purchase'),
    path('add-purchase-item/', views.api_add_purchase_item, name='api-add-purchase-item'),
]
