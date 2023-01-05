from django.urls import re_path, path

from .views import index

urlpatterns = [
    path('', index, name='index'),
    re_path(r'^(\d+)', index, name='index')
]