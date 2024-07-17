from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='admin.index'),
    path('temoignages/',ListTemoignage.as_view() ,name='admin.temoignage.list'),
]
