# Generated by Django 3.1.2 on 2021-09-25 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_imagebanner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagebanner',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagebanner_store', to='Home.store'),
        ),
    ]