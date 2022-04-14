from django.shortcuts import render
from django.views import View
from .models import *


class Home(View):
    def get(self, request):

        obj_contact = Contact.objects.all()

        ctx = {
            'name': 'antony',
            'age': '20',
            'contactos': obj_contact
        }
        return render(request, 'blog/index.html', ctx)