from django.shortcuts import render
from django.http import HttpResponse
from .models import ModelSaludo, ModelBlog
from django.shortcuts import redirect
from .forms import RegistrarContacto
# Create your views here.

def home(request):
    # obj = ModelSaludo.objects.all()
    # obj = obj.values()
    # return HttpResponse('<h1> ¿hola te gusta mi pagina? </h1>')
    return render(request, 'index.html')
    # return redirect('blog')



def contactos(request):
    # obj = ModelSaludo.objects.all()
    # obj = obj.values()
    # return HttpResponse('<h1> ¿hola te gusta mi pagina? </h1>')
    return render(request, 'index.html')
    # return redirect('blog')




def blog(request):
    obj = ModelBlog.objects.all()
    obj = obj.values()
    return render(request, 'blog/blog.html', {'data': obj})

def post(request, pk):
    obj = ModelBlog.objects.get(id=pk)
    return render(request, 'blog/articulo.html', {'data': obj})


def contact(request):
    if request.method == 'POST':
        register_form = RegistrarContacto(request.POST)
        if register_form.is_valid():
            success = register_form.registrar_contact()
            return redirect('blog')
    else:
        register_form = RegistrarContacto()
        return render(request, 'blog/contacto.html', {'register_form': register_form})
