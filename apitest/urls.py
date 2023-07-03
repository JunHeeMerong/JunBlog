from django.urls import path

from . import views

app_name = 'apitest'

urlpatterns = [
    path('', views.mapleapi,name='bloghome'),
]