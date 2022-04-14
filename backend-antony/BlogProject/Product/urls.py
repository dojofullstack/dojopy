from .views import *
from django.urls import path


urlpatterns = [
    path('list-product', ListProduct.as_view(), name='ListProduct')
]