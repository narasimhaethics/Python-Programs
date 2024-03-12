from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.index, name="index"),
    path(r'login', views.login, name='login'),
    path(r'home', views.home, name='home'),
]