"""SystemDojopy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
# from blog.views import blog, blogGeneral
from blog.views import *


urlpatterns = [
    path('', Blog.as_view(), name='blog'),   #  vista basada en clase
    path('post/<slug:myslug>', Article.as_view(), name='post'),   #  vista basada en clase
    path('contact/', Contact.as_view()),
    # path('post/<slug:slug>', blog)    vista basada en funciones
]
