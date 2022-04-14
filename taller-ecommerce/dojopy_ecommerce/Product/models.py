from django.db import models
from Home.models import CategoryStore


class Product(models.Model):
    START1 = 'START1'
    START2 = 'START2'
    START3 = 'START3'
    STARTS = [
        (START1, 'START1'),
        (START2, 'START2'),
        (START3, 'START3'),
    ]

    title = models.CharField(max_length=250, default='')
    category = models.ForeignKey(CategoryStore, on_delete=models.CASCADE)
    slug = models.SlugField()
    price = models.FloatField(default=0)
    price_offer = models.FloatField(default=0)
    description = models.TextField()
    rating = models.CharField(max_length=10, choices=STARTS, default=START1)
    image = models.ImageField(upload_to='product/')

    def __str__(self):
        return f'{self.title} - {self.price}'



class Variation(models.Model):
    title = models.CharField(max_length=250, default='')

    def __str__(self):
        return self.title
