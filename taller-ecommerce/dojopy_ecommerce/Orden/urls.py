from django.urls import path
from .views import *


urlpatterns = [
    path('create', CreateOrder.as_view(), name='create_order'),
    path('checkout', Checkout.as_view(), name='checkout_order'),
]