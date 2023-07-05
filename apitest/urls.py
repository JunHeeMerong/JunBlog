from django.urls import path

from . import views

app_name = 'apitest'

urlpatterns = [
    path('practice/',views.apitest),
    path('mapleapi/',views.mapleapitest),
    path('', views.cubeapi),
    path('cubeinfo/',views.cubeinfo,name='cubeinfo'),
    path('update/',views.cubeupdate,name='update'),
]