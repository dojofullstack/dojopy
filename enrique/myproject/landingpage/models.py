from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class ModelForm(models.Model):
    name = models.CharField(max_length=200, default='', blank=True)
    email = models.EmailField(max_length=200, blank=False)
    mensaje = models.CharField(max_length=200, default='', blank=True)

    def __str__(self):
        return '{} {}'.format(self.name, self.email)


class ModelHeader(models.Model):
    type_view = models.IntegerField(default=0,
                                validators=[MinValueValidator(1), MaxValueValidator(10)])
    title = models.CharField(max_length=200, default='', blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return f'{self.type_view}, {self.title}'
