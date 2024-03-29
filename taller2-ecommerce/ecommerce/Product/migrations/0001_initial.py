# Generated by Django 3.2.7 on 2021-10-04 02:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=200)),
                ('slug', models.SlugField()),
                ('price', models.FloatField(default=0)),
                ('price_offer', models.FloatField(default=0)),
                ('description', models.TextField(default='')),
                ('rating', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3)], default=1)),
                ('image', models.ImageField(upload_to='product')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.categorystore')),
            ],
        ),
    ]
