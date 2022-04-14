from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone

# Create your models here.

class ModelContact(models.Model):
    name = models.CharField(max_length=200, default='', blank=True)
    email = models.EmailField(max_length=200, blank=False)
    number_phone = PhoneNumberField(blank=True)
    message = models.CharField(max_length=200, default="", blank=True, null=True)

    def __str__(self):
        return '{} {}'.format(self.name, self.email)


class ModelPago(models.Model):
    name = models.CharField(max_length=200, default='', blank=True)
    email = models.EmailField(max_length=200, blank=False)
    number_phone = PhoneNumberField(blank=True)
    message = models.CharField(max_length=200, default="", blank=True, null=True)
    country = models.CharField(max_length=200, default="", blank=True)

    def __str__(self):
        return '{} {}'.format(self.name, self.email)


class ModelBlog(models.Model):
    title = models.CharField(max_length=200, default="")
    author = models.CharField(max_length=200, default="")
    texto = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    texto_breve = models.CharField(max_length=200, default="")
    file_image = models.FileField(upload_to='images_post')

    def __str__(self):
        return '{} - {}'.format(self.author, self.created_date)


class ModelProduct(models.Model):
    name = models.CharField(max_length=200, default='', blank=True)
    price = models.DecimalField(
        max_digits=4,
        decimal_places=2,
    )
    description = models.TextField(default='', blank=True)
    file_image = models.FileField(upload_to='images_product')

    def __str__(self):
        return '{} {}'.format(self.name, self.price)
