from django.urls import path
from . import views

urlpatterns = [
        path('', views.home, name='home'),
        path('create', views.create, name='create'),
        path('<str:post_title>/edit', views.edit, name='edit'),
        path('<str:post_title>/delete', views.delete, name='delete'),
        path('<str:post_title>/', views.view, name='view'),
        ]
