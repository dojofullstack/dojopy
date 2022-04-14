from django.urls import path
from Product.views import ProductDetail


urlpatterns = [
    path('<slug:slug>', ProductDetail.as_view(), name='product_detail')
]

