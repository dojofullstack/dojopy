from django.db import models
from Home.models import *


class Product(models.Model):
    START1 = 1
    START2 = 2
    START3 = 3
    STARTS = [
        (START1, 1),
        (START2, 2),
        (START3, 3),
    ]

    title = models.CharField(max_length=200, default='')
    category = models.ForeignKey(CategoryStore, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    price = models.FloatField(default=0)
    price_offer = models.FloatField(default=0)
    description = models.TextField(default='')
    rating = models.IntegerField(choices=STARTS, default=START1)
    image = models.ImageField(upload_to='product')

    def __str__(self):
        return f'{self.title} - {self.price}'