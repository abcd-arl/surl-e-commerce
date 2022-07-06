from django.urls import path
from . import views

urlpatterns = [
    path('store/', views.store, name='store'),
    path('store/product/<int:id>/', views.product, name='product'),
    path('store/bag/', views.bag, name='bag'),
    path('store/checkout/', views.checkout, name='checkout'),
    path('store/thankyou/<int:id>', views.thankyou, name='thankyou'),
    path('ongoing/', views.ongoing, name='ongoing')
]
