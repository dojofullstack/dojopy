from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=250, verbose_name="Categoría")

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=250, verbose_name="Nombre de Producto")
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name="Categoría")
    slug = models.SlugField()
    price = models.FloatField(verbose_name="Precio")
    discount_price = models.FloatField(verbose_name="Precio con Descuento")
    description = models.TextField(verbose_name='Detalle de Producto')
    image_product = models.ImageField(upload_to='products/', verbose_name="Imagen de producto")
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
