# Generated by Django 4.0 on 2022-01-13 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_alter_contactmodel_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactmodel',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='contactmodel',
            name='date_updated',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]