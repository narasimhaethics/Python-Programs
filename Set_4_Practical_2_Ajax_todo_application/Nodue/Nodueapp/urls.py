# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_todo, name='add_todo'),
    path('toggle/', views.toggle_todo, name='toggle_todo'),
    path('delete/', views.delete_todo, name='delete_todo'),
]
