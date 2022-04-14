from django.urls import path
from apiBlog.views import *


urlpatterns = [
    path('articles', ApiListPost.as_view()),   #  vista basada en clase
    path('articles/<int:id>', GetPost.as_view()),   #  vista basada en clase
    path('form-contact/', FormContact.as_view()),   #  vista basada en clase
    path('conector-crm/', ConectorCRM.as_view())
]