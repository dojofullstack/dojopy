from django.db import models
from django.conf import settings


class Store(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    name = models.CharField(max_length=200, default='')
    description = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='logo/')
    email = models.EmailField()
    address = models.CharField(max_length=200, default='')
    phone = models.CharField(max_length=200)
    facebook_url = models.URLField(max_length=200)
    instagram_url = models.URLField(max_length=200)

    def __str__(self):
        return f'{self.user} - {self.name}'


class CategoryStore(models.Model):
    title = models.CharField(max_length=200, default='')
    banner = models.ImageField(upload_to='category')

    def __str__(self):
        return self.title


class ImageBanner(models.Model):
    banner = models.ImageField(upload_to='banner')
    title = models.CharField(max_length=200, default='')
    store = models.ForeignKey(Store, on_delete=models.CASCADE)

    def __str__(self):
        return self.title