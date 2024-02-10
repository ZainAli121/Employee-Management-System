from . import views
from django.urls import path

urlpatterns = [
    path('', views.getRoutes, name='routes'),
    path('employees/', views.getEmployees, name='employees'),
    path('employees/<str:pk>/', views.getEmployee, name='employee'),
    path('attendence/', views.getAttList, name='attendence'),
    path('attendence/<str:pk>/', views.getAttEmp, name='att_emp'),
]