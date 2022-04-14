# Generated by Django 3.0.6 on 2020-06-08 00:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0004_auto_20200523_2125'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelBlog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=200)),
                ('author', models.CharField(default='', max_length=200)),
                ('texto', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('texto_breve', models.CharField(default='', max_length=200)),
                ('file_image', models.FileField(upload_to='images_post')),
            ],
        ),
    ]
