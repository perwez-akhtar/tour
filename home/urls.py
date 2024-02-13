from django import views
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('register/', views.register, name='register'),
    path('packages/', views.packages, name='packages'),
    path('services/', views.services, name='services'), 
    path('book/', views.book, name='book'), 
    path('pack/', views.pack, name='pack'), 
    path('starting/', views.starting, name='starting'), 
    path('flight/', views.flight, name='flight'), 
    path('about/', views.about, name='about') ,
    # path('', views.index, name='index'),
]
