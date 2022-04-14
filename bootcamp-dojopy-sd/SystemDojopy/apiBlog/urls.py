from django.urls import path
from apiBlog.views import *


urlpatterns = [
    path('articles', ListPost.as_view()),   #  vista basada en clase
    path('articles/<int:id>', DetailPost.as_view()), 
    path('contact/', Contact.as_view())
]