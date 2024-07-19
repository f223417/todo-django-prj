from django.contrib import admin
from django.urls import path
from tasks import views

urlpatterns = [
    path('update_task/<str:pk>/', views.updateTask, name='update_task'),
    path('', views.index, name='list'),
    path('delete/<str:pk>/', views.deleteTask, name='delete'),
]
