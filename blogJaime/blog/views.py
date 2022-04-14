from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import  View
from .models import *
from django.shortcuts import get_object_or_404
from .form import FormContact

# Create your views here.

def home(request):
    if request.method == 'GET':
        objects_product =  Product.objects.all().order_by('start')[:10]

        return render(request, 'ecommerce/home_ecommerce.html', {'objects_product': objects_product})


class Blog(View):
    def get(self, request):
        data = BlogModel.objects.all().order_by('time_created')
        data = data[:10]

        return render(request, 'ecommerce/blog.html', {'obj_post': data})
    
    def post(self, request):
        return JsonResponse({'data': 1, 'message': 'ok'})


class BlogDetail(View):
    def get(self, request, slug):
        # data = BlogModel.objects.get(slug=slug)
        data = get_object_or_404(BlogModel, slug=slug)
        
        return render(request, 'ecommerce/blog_detail.html', {'post': data})


class ProductDetail(View):
    def get(self, request, slug):
        # print('slug es; ',slug)
        product = get_object_or_404(Product, slug=slug)
        return render(request, 'ecommerce/product.html', {'item': product})



class Contacto(View):
    def post(self, request):
        data = request.POST
        form = FormContact(data)
        if form.is_valid():
            email = form.cleaned_data['email']
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            consult = form.cleaned_data['consult']

            Contact.objects.create(
                email=email,
                name=name,
                phone=phone,
                consult=consult,
            )
            print('contacto guardado')
            return redirect('/')
        return redirect('/blog/contact')

    def get(self, request):
        return render(request, 'ecommerce/contact.html')

