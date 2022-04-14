from django.shortcuts import render
from django.views import View
from .models import *
from Product.models import *
from Order.models import *

# def home(request):
#     if request.method == 'GET':
#         return render(request, 'home.html')
#     elif request.method == 'POST':
#         return ''


class Home(View):
    def get(self, request):
        obj_store = Store.objects.last()
        obj_category = CategoryStore.objects.all()
        obj_banner = ImageBanner.objects.all()
        obj_banner = list(enumerate(obj_banner))
        obj_products = Product.objects.all()[:3]

        cart_stock = 0
        total = 0
        if not request.user.is_anonymous:
            obj_order = Orden.objects.get(user=request.user, status_order=False)
            obj_orden = OrdenProduct.objects.filter(orden=obj_order)
            for item in obj_orden:
                cart_stock += item.stock

        ctx = {
            'store': obj_store,
            'category': obj_category,
            'banner': obj_banner,
            'product': obj_products,
            'cart_stock': cart_stock,
            'total': total
        }
        return render(request, 'home.html', ctx)