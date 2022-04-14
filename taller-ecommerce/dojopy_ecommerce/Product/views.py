from django.shortcuts import render, redirect
from django.views.generic import View
from Product.models import *
from Home.models import *
from Orden.models import *
from django.shortcuts import get_object_or_404


class ProductDetail(View):
    def get(self, request, slug):
        obj_store = Store.objects.last()
        # obj_p = Product.objects.get(slug=slug)
        # obj_p = Product.objects.filter(slug=slug)
        obj_p = get_object_or_404(Product, slug=slug)

        obj_prod = Product.objects.filter(category=obj_p.category)[:3]

        cont_cart = 0
        if not request.user.is_anonymous:
            obj_cart = OrdenCart.objects.get(user=request.user)
            obj_orden = OrdenProduct.objects.filter(orden=obj_cart)
            for order in obj_orden:
                cont_cart += order.stock

        ctx = {
                'obj_store': obj_store,
                'obj_p': obj_p,
                'obj_prod': obj_prod,
                'cont_cart': cont_cart
        }
        return render(request, 'product_detail.html', ctx)