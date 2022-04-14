from django.contrib import admin
from .models import *

admin.site.register(Orden)
admin.site.register(OrdenProduct)
admin.site.register(Adress)
admin.site.register(Checkout)