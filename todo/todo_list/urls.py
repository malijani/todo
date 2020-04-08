""" URLs configuration of todo app """
from django.urls import path
from . import views

app_name = 'todo_list'

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:list_id>/', views.delete, name='delete'),
    path('cross_of/<int:list_id>/', views.cross_off, name='cross_off'),
    path('uncross/<int:list_id>/', views.uncross, name='uncross'),
    path('edit/<int:list_id>/', views.edit, name='edit')
    ]
