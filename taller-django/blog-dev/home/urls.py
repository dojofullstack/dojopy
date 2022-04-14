from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contactos', views.home, name='home'),
    path('blog', views.blog, name='blog'),
    path('contact', views.contact, name='contact'),
    path('post/<int:pk>', views.post, name='post'),
]
