from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('link/<str:slug>/', views.redirector, name='redirector'),
    path('link/<str:slug>/delete', views.delete_link, name='delete_link'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.signin, name='signin'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/create/', views.create_link, name='create'),
    path('profile/gettoken/', views.create_token),
    path('api/v1/links/', views.links_api),
    path('api/v1/links/<str:slug>', views.detail_links_api)
]
