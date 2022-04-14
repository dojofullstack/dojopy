# Generated by Django 3.1.2 on 2021-11-05 04:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Categoría')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Nombre de Producto')),
                ('slug', models.SlugField()),
                ('price', models.FloatField(verbose_name='Precio')),
                ('discount_price', models.FloatField(verbose_name='Precio con Descuento')),
                ('description', models.TextField(verbose_name='Detalle de Producto')),
                ('image_product', models.ImageField(upload_to='products/', verbose_name='Imagen de producto')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Product.category', verbose_name='Categoría')),
            ],
        ),
    ]
