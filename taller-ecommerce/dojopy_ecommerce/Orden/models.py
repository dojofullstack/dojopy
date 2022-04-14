from django.db import models
from django.conf import settings
from Product.models import *


class OrdenCart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    status_order = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user} {self.status_order}'


class OrdenProduct(models.Model):
    orden = models.ForeignKey(OrdenCart, on_delete=models.CASCADE)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    stock = models.IntegerField(default=0)
    variation = models.ForeignKey(Variation, on_delete=models.CASCADE, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.orden} - {self.item}'