from django.contrib import admin
from .models import (
    ModelForm,
    ModelHeader
    )
# Register your models here.

admin.site.register(ModelForm)
admin.site.register(ModelHeader)
