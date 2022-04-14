from django.db import models
from django.conf import settings
from Product.models import *

class Orden(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    status_order = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user} - {self.status_order}'


class OrdenProduct(models.Model):
    orden = models.ForeignKey('Orden', on_delete=models.CASCADE)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    stock = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.item} - {self.stock}'


class Adress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    adress = models.CharField(max_length=250, default="")
    country = models.CharField(max_length=250, default="")
    zip_code = models.CharField(max_length=250, default="")
    city = models.CharField(max_length=250, default="")
    phone = models.CharField(max_length=250, default="")
    email = models.EmailField()
    name = models.CharField(max_length=250, default="")

    def __str__(self):
        return self.adress


class Checkout(models.Model):
    PAYPAL = 'Paypal'
    ML = 'MercadoPago'
    PAYMENTS = (
        (PAYPAL, 'Paypal'),
        (ML, 'MercadoPago'),
    )

    address = models.ForeignKey(Adress, on_delete=models.CASCADE)
    order_product = models.ManyToManyField(OrdenProduct)
    payment_type = models.CharField(max_length=11 , choices=PAYMENTS, default=PAYPAL)
    date_order = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.date_order} - {self.completed}'