from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import (
        ModelContact,
        ModelBlog,
        ModelProduct
        )
from .forms import (
        RegistrarContacto,
        RegistrarPago
        )
from django.db.models import F

# Create your views here.

def home(requests):
    return render(requests, 'index.html', {})
    # obj = ModelContact.objects.all()
    # return HttpResponse('<h1> hola </h1> {}'.format(obj.values()))
    # return HttpResponse(obj[0].email)

def blog(requests):
    obj = ModelBlog.objects.all()
    obj = obj.order_by('created_date')
    return render(requests, 'blog.html', {'posts': obj})


def post_detail(requests, pk):
    obj = ModelBlog.objects.filter(id=pk)
    is_bot = requests.user_agent.is_bot

    if obj.exists():
        if is_bot is False:
            obj.update(count=F('count') + 1)
        obj = obj.first()

    return render(requests, 'post.html', {'post': obj})


def contact(requests):
    # form = RegistrarContacto()
    if requests.method == 'GET':
        return render(requests, 'contacto.html')
    elif requests.method == 'POST':
        print(requests.POST)
        register_form = RegistrarContacto(requests.POST)
        print(register_form.is_valid())
        if register_form.is_valid():
            success = register_form.registrar_contact()

        return render(requests, 'contacto.html')


def payment_view(requests, pk):
    if requests.method == 'GET':
        obj = ModelProduct.objects.filter(id=pk)
        if obj:
            obj = obj.first()
        else:
            return redirect('/')
        return render(requests, 'form_payment.html', {'obj': obj})
    elif requests.method == 'POST':
        print(requests.POST)
        register_form = RegistrarPago(requests.POST)
        print(register_form.is_valid())
        if register_form.is_valid():
            success = register_form.registrar_pago()

        return render(requests, 'form_payment.html')
