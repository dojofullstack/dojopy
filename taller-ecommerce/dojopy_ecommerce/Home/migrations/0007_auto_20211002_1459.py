# Generated by Django 3.2.7 on 2021-10-02 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0006_categorystore'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorystore',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='imagebanner',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='store',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
