from django.urls import path

from . import views

# This project has a single page and thus only one URL path
urlpatterns = [
    path('', views.index, name='index'),
]
