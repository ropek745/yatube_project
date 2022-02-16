# posts/urls.py
from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='posts_global'),
    path('group/<slug:slug>/', views.group_posts, name='posts_slug')
]  