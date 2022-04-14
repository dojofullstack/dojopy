
from django.urls import path
from .views import (
    home,
    blog,
    contact,
    post_detail,
    payment_view
    )

from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('', home, name='home'),
    path('blog', blog, name='blog'),
    path('post/<int:pk>', post_detail, name='post-detail'),
    path('contact', contact, name='contact'),
    path('payment/<int:pk>', payment_view, name='payment'),
]
