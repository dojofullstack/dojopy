from django.contrib import admin
from .models import (
        ModelContact,
        ModelBlog,
        ModelPago,
        ModelProduct
        )
# Register your models here.

admin.site.register(ModelContact)
admin.site.register(ModelBlog)
admin.site.register(ModelPago)
admin.site.register(ModelProduct)
