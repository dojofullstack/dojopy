from django.shortcuts import render, redirect
from django.views.generic import View
from .models import *


class CreateOrder(View):
    def post(self, request):
        request.user
        data = request.POST
        product_id  = data.get('product-id', '')
        stock  = data.get('product-stock', '')
        variation  = data.get('product-variation', '')

        if request.user.is_anonymous:
            return redirect('/accounts/login/')

        obj_cart, created = OrdenCart.objects.get_or_create(user=request.user)

        obj_atrib = Variation.objects.get(title=variation)

        OrdenProduct.objects.create(
            orden=obj_cart,
            item_id=product_id,
            stock=stock,
            variation=obj_atrib
        )
        return redirect('/order/checkout')



class Checkout(View):
    def get(self, request):
        return render(request, 'cart.html', {})