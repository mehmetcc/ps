from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path(r'', views.post_list, name='post_list'),
    path(r'post/<slug:slug>/', views.post_detail, name='post_detail'),
    path(r'category/<slug:slug>/', views.categories_detail, name='category_detail'),
    path(r'about.html', views.about, name='about'),
]
