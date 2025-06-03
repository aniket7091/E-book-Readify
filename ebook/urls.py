from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.upload_book, name='upload_book'),
    path('book/<int:pk>/', views.book_detail, name='book_detail'),

]
