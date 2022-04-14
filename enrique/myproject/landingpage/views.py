from django.shortcuts import render
from django.http import HttpResponse
from .models import (
    ModelForm,
    ModelHeader
    )
# Create your views here.


def landing(request):
    type = 1
    obj = ModelHeader.objects.filter(type_view=type)
    if obj:
        obj = obj.first()
    return render(request, 'index.html', {'data': obj})
