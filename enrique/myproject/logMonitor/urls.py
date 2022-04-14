from django.urls import path
from .views import list_log, update

urlpatterns = [
    path('list-log', list_log, name="list_log"),
    path('update', update, name="update")
]
