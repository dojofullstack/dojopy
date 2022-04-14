from django.db import models
from django.utils import timezone


class ModelSaludo(models.Model):
    mensaje = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)
    mystack = models.ForeignKey('ModelConect', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {}'.format(self.mensaje, self.nombre)


class ModelConect(models.Model):
    stack = models.CharField(max_length=200)

    def __str__(self):
        return self.stack


class ModelBlog(models.Model):
    title = models.CharField(max_length=200, default="")
    author = models.CharField(max_length=200, default="")
    texto = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    url_image = models.CharField(max_length=200, default="")
    texto_breve = models.CharField(max_length=200, default="")

    def __str__(self):
        return '{} - {}'.format(self.author, self.created_date)


class ModelContact(models.Model):
    name = models.CharField(max_length=200, default='', blank=False)
    email = models.EmailField(max_length=200, blank=False)
    mensaje = models.CharField(max_length=200, default="")

    def __str__(self):
        self.email
