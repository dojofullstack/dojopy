from django.shortcuts import render, get_object_or_404
from django.views import View
from Home.models import *
from Order.models import *
from .models import *


class ProductDetail(View):
    def get(self, request, slug):
        obj_store = Store.objects.last()
        obj_category = CategoryStore.objects.all()
        # obj_product = Product.objects.get(slug=slug)
        # obj_product = Product.objects.filter(slug=slug)
        obj_product = get_object_or_404(Product, slug=slug)
            

        cart_stock = 0
        if not request.user.is_anonymous:
            obj_order = Orden.objects.get(user=request.user, status_order=False)
            obj_orden = OrdenProduct.objects.filter(orden=obj_order)
            for item in obj_orden:
                cart_stock += item.stock

        ctx = {
            'store': obj_store,
            'category': obj_category,
            'product': obj_product,
            'cart_stock': cart_stock
        }
        return render(request, 'product_detail.html', ctx)