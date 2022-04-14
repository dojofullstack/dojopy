from django.shortcuts import render
from django.views.generic import View
from .models import *
from Product.models import *
from Orden.models import *
# Create your views here.


class Home(View):
    def get(self, request):
        obj_store = Store.objects.last()
        obj_banner = obj_store.imagebanner_store.all()
        obj_ctg = CategoryStore.objects.all()
        obj_prod = Product.objects.all()[:3]
        
        # alternativa de query
        # obj_banner = ImageBanner.objects.filter(store=obj_store)
        # print(obj_banner)

        obj_r = list(enumerate(obj_banner))
    

        cont_cart = 0
        if not request.user.is_anonymous:
            obj_cart = OrdenCart.objects.get(user=request.user)
            obj_orden = OrdenProduct.objects.filter(orden=obj_cart)
            for order in obj_orden:
                cont_cart += order.stock

        ctx = {
                'obj_store': obj_store,
                'obj_banner': obj_r,
                'obj_ctg': obj_ctg,
                'obj_prod': obj_prod,
                'cont_cart': cont_cart
                }
        return render(request, 'home.html', ctx)