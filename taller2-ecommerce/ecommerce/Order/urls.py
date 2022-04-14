from django.urls import path
from .views import *


urlpatterns = [
        path('crear-orden/', CrearOrden.as_view(), name='crear-add'),
        path('checkout/', CheckoutView.as_view(), name='checkout'),
        path('checkout-finish/', CheckoutFinish.as_view(), name='checkout-finish'),
    ]