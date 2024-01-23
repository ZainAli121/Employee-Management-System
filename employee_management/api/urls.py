from . import views
from django.urls import path

urlpatterns = [
    path('', views.getRoutes, name='routes'),
    path('employees/', views.getEmployees, name='employees'),
]