from . import views
from django.urls import path

urlpatterns = [
    path('admin/', views.admin_employees_site, name='admin_site'),
    path('employee/', views.employees_site, name='employees_site'),
    path('profile/<int:pk>/', views.employeeProfile, name='employee_profile'),
]