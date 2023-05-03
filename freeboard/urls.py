from django.urls import path

from . import views

app_name = 'freeboard'

urlpatterns = [
    path('', views.freeboardhome,name='freeboardhome'),
    path('<int:freepost_id>/',views.free_detail,name='free_detail'),
    
    path('post/create/',views.free_post_create,name='free_post_create'),
    path('post/modify/<int:freepost_id>/', views.free_post_modify, name='free_post_modify'),
    path('post/delete/<int:freepost_id>/',views.free_post_delete, name='free_post_delete'),
    
    path('comment/create/<int:freepost_id>/',views.free_comment_create, name='free_comment_create'),
    path('comment/modify/<int:comment_id>/',views.free_comment_modify, name='free_comment_modify'),
    path('comment/delete/<int:comment_id>/',views.free_comment_delete, name='free_comment_delete'),
]