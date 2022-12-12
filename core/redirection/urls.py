from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('link/<str:slug>/', views.redirector, name='redirector'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.signin, name='signin'),
    path('profile/', views.profile, name='profile'),
]