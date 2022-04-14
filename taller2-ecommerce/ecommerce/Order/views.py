from django.shortcuts import render, redirect
from django.views.generic import  View
from .models import *


class CrearOrden(View):
    def post(self, request):
        data = request.POST
        product_id = data.get('product-id')
        stock = data.get('product-stock')

        # if request.user.is_anonymous:
        #     return redirect('/accounts/login')
        
        obj_order, created = Orden.objects.get_or_create(user=request.user, status_order=False)

        OrdenProduct.objects.create(orden=obj_order, item_id=product_id, stock=stock)
        return redirect('/order/checkout')



class CheckoutView(View):
    def get(self, request):
        obj_store = Store.objects.last()

        cart_stock = 0
        total = 0
        if not request.user.is_anonymous:
            obj_order = Orden.objects.get(user=request.user, status_order=False)
            obj_orden = OrdenProduct.objects.filter(orden=obj_order)
            for item in obj_orden:
                cart_stock += item.stock
                total += item.item.price

        ctx = {
            'cart_stock': cart_stock,
            'store': obj_store,
            'obj_orden': obj_orden,
            'total': total
        }
        return render(request, 'checkout.html', ctx)


class CheckoutFinish(View):
    def post(self, request):
        user = request.user
        obj_store = Store.objects.last()
        data = request.POST
        username = data.get('username')
        email = data.get('email')
        phone = data.get('phone')
        city = data.get('city')
        zipcode = data.get('zipcode')
        adress = data.get('adress')
        country = data.get('country')

        obj_order = Orden.objects.get(user=request.user, status_order=False)
        obj_orden = OrdenProduct.objects.filter(orden=obj_order)


        obj_adrres =  Adress.objects.create(
            user=user,
            phone=phone,
            city=city,
            zip_code=zipcode,
            adress=adress,
            country=country
        )

        obj_checkout = Checkout.objects.create(
            address=obj_adrres,
            payment_type='Paypal',
        )

        for orden_product in obj_orden:
            obj_checkout.order_product.add(orden_product)
            print('agregando item al checkout')

        return redirect('/')
