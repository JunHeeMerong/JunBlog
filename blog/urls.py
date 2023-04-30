from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.bloghome,name='bloghome'),
    path('<int:post_id>/',views.detail,name='detail'),
    path('post/create/',views.post_create,name='post_create')
]