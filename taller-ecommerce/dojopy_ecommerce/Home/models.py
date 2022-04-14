from django.db import models
from django.conf import settings


class Store(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=250, default='')
    resume = models.TextField(default='')
    logo = models.ImageField(upload_to='store/')
    email = models.EmailField()
    address = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)
    facebook_url = models.URLField(max_length=250)
    instagram_url = models.URLField(max_length=250)

    def __str__(self):
        return f'{self.user} - {self.name}'


class ImageBanner(models.Model):
    banner = models.ImageField(upload_to='banner/')
    store = models.ForeignKey('Store', on_delete=models.CASCADE, related_name="imagebanner_store")
    name = models.CharField(max_length=250, default='')

    def __str__(self):
        return f'{self.store} - {self.banner}'



class CategoryStore(models.Model):
    banner = models.ImageField(upload_to='banner/')
    title = models.CharField(max_length=250, default='')

    def __str__(self):
        return self.title