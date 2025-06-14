from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.login, name='login'),
     path('register/', views.register, name='register'),
     path('adminLogin/', views.admin_login, name='admin_login'),
     path('logout/', views.logout, name='logout'),
]