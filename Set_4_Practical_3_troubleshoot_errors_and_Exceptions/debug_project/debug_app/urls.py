# debug_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.error_view, name='error_view'),
]
