from django.urls import path
from . import views

app_name = 'habits'

urlpatterns = [
    path('', views.habit_list, name='habit_list'),
    path('add/', views.habit_add, name='habit_add'),
    path('log/<int:habit_id>/', views.habit_log, name='habit_log'),
    path('register/', views.register, name='register'),
    path('delete/<int:habit_id>/', views.habit_delete, name='habit_delete'),
]