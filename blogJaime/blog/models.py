from django.db import models
from taggit.managers import TaggableManager
from django.utils import timezone


class BlogModel(models.Model):
    titulo = models.CharField(max_length=200, default='')
    imagen = models.ImageField(upload_to='imagenes/')
    slug = models.SlugField()
    description = models.TextField()
    tags = TaggableManager()
    autor = models.CharField(max_length=200, default='')
    time_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo


class Product(models.Model):
    titulo = models.CharField(max_length=200, default='')
    imagen = models.ImageField(upload_to='imagenes/')
    slug = models.SlugField()
    description = models.TextField()
    time_created = models.DateTimeField(default=timezone.now)
    price = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    price_promocion = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    start = models.IntegerField(default=0)

    def __str__(self):
        return self.titulo


class Contact(models.Model):
    name = models.CharField(max_length=200, default='')
    email = models.EmailField(max_length=200, default='')
    phone = models.CharField(max_length=200, default='')
    consult = models.TextField()
    time_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email

